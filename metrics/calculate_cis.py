import ast
import os
from collections import defaultdict

class CISVisitor(ast.NodeVisitor):
    def __init__(self):
        self.class_methods = defaultdict(list)

    def visit_ClassDef(self, node):
        current_class = node.name
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef):
                # Hanya menghitung metode yang tidak diawali dengan _ (public)
                if not stmt.name.startswith('_'):
                    self.class_methods[current_class].append(stmt.name)
                    # Debug print untuk melihat metode yang dianggap public
                    print(f"Class: {current_class}, Public Method: {stmt.name}")
        self.generic_visit(node)

def calculate_cis_in_file(file_path, visitor):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read())
    visitor.visit(tree)

def calculate_cis_in_directory(directory):
    visitor = CISVisitor()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                calculate_cis_in_file(file_path, visitor)
    
    return visitor.class_methods

def calculate_cis(class_methods):
    cis_values = {}
    for cls, methods in class_methods.items():
        cis = len(methods)
        cis_values[cls] = cis
        # Debug print untuk melihat jumlah metode public dalam setiap kelas
        print(f"Class: {cls}, CIS: {cis}")
    return cis_values

def print_cis(cis_values):
    total_cis = 0
    for cls, cis in cis_values.items():
        print(f"Class: {cls}, CIS: {cis}")
        total_cis += cis
    print(f"Total CIS: {total_cis}")

if __name__ == "__main__":
    directory = "../tests/"  # Ganti dengan path ke direktori proyek Anda
    class_methods = calculate_cis_in_directory(directory)
    cis_values = calculate_cis(class_methods)
    print_cis(cis_values)
