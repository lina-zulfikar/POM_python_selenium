import ast
import os
from collections import defaultdict

class CAMVisitor(ast.NodeVisitor):
    def __init__(self):
        self.class_methods = defaultdict(list)
        self.current_class = None
        self.current_method = None

    def visit_ClassDef(self, node):
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = None

    def visit_FunctionDef(self, node):
        if self.current_class:
            self.current_method = node.name
            self.class_methods[self.current_class].append((self.current_method, set()))
            self.generic_visit(node)
            self.current_method = None

    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name) and self.current_method:
            if self.current_class:
                method_list = self.class_methods[self.current_class]
                for method in method_list:
                    if method[0] == self.current_method:
                        method[1].add(node.attr)
        self.generic_visit(node)

def calculate_cam_in_file(file_path, visitor):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    visitor.visit(tree)

def calculate_cam_in_directory(directory):
    visitor = CAMVisitor()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                calculate_cam_in_file(file_path, visitor)
    
    return visitor.class_methods

def calculate_cam(class_methods):
    cam_values = {}
    for cls, methods in class_methods.items():
        num_methods = len(methods)
        if num_methods <= 1:
            cam_values[cls] = 1.0
            continue
        
        total_shared = 0
        total_pairs = 0

        # Menghitung jumlah pasangan metode yang berbagi atribut
        for i in range(num_methods):
            for j in range(i + 1, num_methods):
                total_shared += len(methods[i][1].intersection(methods[j][1]))
                total_pairs += 1

        # Hitung nilai CAM untuk kelas ini
        cam_values[cls] = total_shared / total_pairs if total_pairs > 0 else 0.0
    return cam_values

def print_cam(cam_values):
    total_cam = 0
    for cls, cam in cam_values.items():
        print(f"Class: {cls}, CAM: {cam:.2f}")
        total_cam += cam
    
    # Menampilkan total CAM
    num_classes = len(cam_values)
    if num_classes > 0:
        average_cam = total_cam / num_classes
        print(f"Total CAM across all classes: {total_cam:.2f}")
        print(f"Average CAM across all classes: {average_cam:.2f}")
    else:
        print("No classes found to calculate CAM.")

if __name__ == "__main__":
    directory = "../tests/"  # Ganti dengan path ke direktori proyek Anda
    class_methods = calculate_cam_in_directory(directory)
    cam_values = calculate_cam(class_methods)
    print_cam(cam_values)
