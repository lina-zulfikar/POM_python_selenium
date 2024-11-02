import ast
import os
from collections import defaultdict

class MethodCounterVisitor(ast.NodeVisitor):
    def __init__(self):
        self.class_methods = defaultdict(int)
        self.methods_details = defaultdict(list)

    def visit_ClassDef(self, node):
        class_name = node.name
        method_count = 0

        # Iterasi setiap elemen di dalam kelas
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef):
                # Menambah ke hitungan metode, termasuk __init__
                method_count += 1
                self.methods_details[class_name].append(stmt.name)

        self.class_methods[class_name] = method_count
        self.generic_visit(node)

def calculate_nom_in_file(file_path, visitor):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read())
    visitor.visit(tree)

def calculate_nom_in_directory(directory):
    visitor = MethodCounterVisitor()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                calculate_nom_in_file(file_path, visitor)
    
    return visitor.class_methods, visitor.methods_details

def print_nom_results(nom_values, methods_details):
    print("Debugging Output:")
    for cls, nom in nom_values.items():
        print(f"Class: {cls}, Number of Methods: {nom}")
        print(f"  Methods: {methods_details[cls]}")

if __name__ == "__main__":
    directory = "../tests/"  # Ganti dengan path ke direktori proyek Anda
    nom_values, methods_details = calculate_nom_in_directory(directory)
    print_nom_results(nom_values, methods_details)
    total_nom = sum(nom_values.values())
    print(f"Total Number of Methods (NOM) across all classes: {total_nom}")
