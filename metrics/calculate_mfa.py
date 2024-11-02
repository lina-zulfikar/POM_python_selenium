import ast
import os
from collections import defaultdict

class InheritanceVisitor(ast.NodeVisitor):
    def __init__(self):
        self.class_parents = defaultdict(list)
        self.class_methods = defaultdict(list)

    def visit_ClassDef(self, node):
        current_class = node.name
        for base in node.bases:
            if isinstance(base, ast.Name):
                parent_class = base.id
                self.class_parents[current_class].append(parent_class)
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef):
                self.class_methods[current_class].append(stmt.name)
        self.generic_visit(node)

def calculate_mfa_in_file(file_path, visitor):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    visitor.visit(tree)

def calculate_mfa_in_directory(directory):
    visitor = InheritanceVisitor()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                calculate_mfa_in_file(file_path, visitor)
    
    return visitor.class_parents, visitor.class_methods

def calculate_mfa(class_parents, class_methods):
    mfa_values = {}
    for cls, methods in class_methods.items():
        inherited_methods = set()
        for parent in class_parents[cls]:
            if parent in class_methods:
                inherited_methods.update(class_methods[parent])
        if methods:
            mfa = len(inherited_methods) / len(methods)
        else:
            mfa = 0
        mfa_values[cls] = mfa
    return mfa_values

def print_mfa(mfa_values):
    total_mfa = sum(mfa_values.values())
    average_mfa = total_mfa / len(mfa_values) if mfa_values else 0
    print("\nMFA for each class:")
    for cls, mfa in mfa_values.items():
        print(f"Class: {cls}, MFA: {mfa:.2f}")
    print(f"\nTotal MFA: {total_mfa:.2f}")
    print(f"Average MFA: {average_mfa:.2f}")

if __name__ == "__main__":
    directory = "../tests/"  # Ganti dengan path ke direktori proyek Anda
    class_parents, class_methods = calculate_mfa_in_directory(directory)
    mfa_values = calculate_mfa(class_parents, class_methods)
    print_mfa(mfa_values)
