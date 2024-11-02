import ast
import os
from collections import defaultdict

class PolymorphismVisitor(ast.NodeVisitor):
    def __init__(self):
        self.class_methods = defaultdict(set)
        self.class_parents = defaultdict(list)

    def visit_ClassDef(self, node):
        current_class = node.name

        # Mendapatkan semua parent classes dari class saat ini
        for base in node.bases:
            if isinstance(base, ast.Name):
                self.class_parents[current_class].append(base.id)

        # Menyimpan semua method dalam class saat ini, kecuali konstruktor (__init__)
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef) and stmt.name != '__init__':
                self.class_methods[current_class].add(stmt.name)

        self.generic_visit(node)

def calculate_nop_in_file(file_path, visitor):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    visitor.visit(tree)

def calculate_nop_in_directory(directory):
    visitor = PolymorphismVisitor()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                calculate_nop_in_file(file_path, visitor)
    
    return visitor.class_methods, visitor.class_parents

def calculate_nop(class_methods, class_parents):
    nop_values = {}
    for cls, methods in class_methods.items():
        poly_methods = set()
        
        # Mencari subkelas yang mewarisi class ini
        for subclass, parents in class_parents.items():
            if cls in parents:
                # Cek apakah subclass meng-override metode dari parent
                for method in class_methods[subclass]:
                    if method in methods:
                        poly_methods.add(method)
        
        # Menyimpan jumlah metode polimorfik untuk setiap class
        nop_values[cls] = len(poly_methods)
    
    return nop_values

def print_nop(nop_values):
    total_nop = 0
    for cls, nop in nop_values.items():
        print(f"Class: {cls}, NOp: {nop}")
        total_nop += nop
    print(f"Total NOp: {total_nop}")

if __name__ == "__main__":
    directory = "../tests/"  # Ganti dengan path ke direktori proyek Anda
    class_methods, class_parents = calculate_nop_in_directory(directory)
    nop_values = calculate_nop(class_methods, class_parents)
    print_nop(nop_values)
