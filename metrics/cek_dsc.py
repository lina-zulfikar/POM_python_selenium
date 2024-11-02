import os
import ast

def count_classes_in_file(file_path):
    """
    Menghitung jumlah kelas dalam satu file Python.
    
    Args:
    file_path (str): Jalur ke file Python.
    
    Returns:
    int: Jumlah kelas yang ditemukan di file tersebut.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())
        return sum(isinstance(node, ast.ClassDef) for node in tree.body)

def count_classes_in_directory(directory_path):
    """
    Menghitung total jumlah kelas di semua file Python dalam direktori.
    
    Args:
    directory_path (str): Jalur ke direktori proyek Python.
    
    Returns:
    int: Jumlah total kelas yang ditemukan di direktori.
    """
    total_classes = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                total_classes += count_classes_in_file(file_path)
    return total_classes

# Menghitung jumlah kelas dalam direktori 'pages' dan 'tests'
pages_directory = "../../POM_tests"
tests_directory = "../tests"

total_classes_pages = count_classes_in_directory(pages_directory)
total_classes_tests = count_classes_in_directory(tests_directory)

# Print hasil dari kedua direktori
print(f"Total jumlah kelas dalam direktori 'pages': {total_classes_pages}")
print(f"Total jumlah kelas dalam direktori 'tests': {total_classes_tests}")

# Total keseluruhan dari kedua direktori
total_classes = total_classes_pages + total_classes_tests
print(f"Total jumlah kelas dari kedua direktori: {total_classes}")
