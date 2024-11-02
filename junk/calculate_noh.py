import ast
import os

class HierarchyCounter(ast.NodeVisitor):
    def __init__(self):
        self.inheritance_map = {}
        self.hierarchy_count = 0

    def visit_ClassDef(self, node):
        class_name = node.name
        base_classes = [base.id for base in node.bases if isinstance(base, ast.Name)]
        self.inheritance_map[class_name] = base_classes
        self.generic_visit(node)

    def count_hierarchies(self):
        visited = set()

        def visit_class(class_name):
            if class_name in visited:
                return
            visited.add(class_name)
            for base in self.inheritance_map.get(class_name, []):
                visit_class(base)

        for class_name in self.inheritance_map:
            if class_name not in visited:
                self.hierarchy_count += 1
                visit_class(class_name)

def count_hierarchies_in_file(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())

    hierarchy_counter = HierarchyCounter()
    hierarchy_counter.visit(tree)
    hierarchy_counter.count_hierarchies()

    return hierarchy_counter.hierarchy_count

def count_hierarchies_in_directory(directory):
    total_hierarchies = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                total_hierarchies += count_hierarchies_in_file(file_path)
    return total_hierarchies

if __name__ == "__main__":
    directory = "../tests/"  # Ganti dengan path ke direktori proyek Anda
    total_hierarchies = count_hierarchies_in_directory(directory)
    print(f"Total number of hierarchies: {total_hierarchies}")
