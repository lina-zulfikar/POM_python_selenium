import os
import ast

# Daftar library atau modul yang ingin dikecualikan dari perhitungan aggregation
EXCLUDED_LIBRARIES = {"Service","GeckoDriverManager","sys","DriverManager","pytest","selenium", "webdriver", "By", "EC", "WebDriverWait", "time", "ActionChains", "random", "NoSuchElementException","expected_conditions","Select"}

class ClassObject:
    def __init__(self, name, bases):
        self.name = name
        self.bases = set(bases)  # Menggunakan set untuk menghindari duplikasi

    def get_name(self):
        return self.name

    def get_bases(self):
        return self.bases

class DCC:
    def __init__(self, classes):
        self.classes = classes
        self.class_map = {}
        self.dcc_value = 0.0
        self.calculate_coupling()

    def calculate_coupling(self):
        total_coupling = 0
        for class_obj in self.classes:
            coupling_count = self.calculate_class_coupling(class_obj)
            total_coupling += coupling_count
            self.class_map[class_obj.get_name()] = coupling_count
            print(f"{class_obj.get_name()}: {coupling_count} direct couplings")

        if len(self.classes) > 0:
            self.dcc_value = total_coupling / len(self.classes)
        print(f"Total DCC Value: {self.dcc_value}")

    def calculate_class_coupling(self, class_obj):
        # Menghitung coupling dari bases dan imports
        coupling_count = 0
        bases = class_obj.get_bases()

        # Gunakan set untuk menghindari perhitungan duplikat
        unique_bases = set(bases)

        for base in unique_bases:
            if base not in EXCLUDED_LIBRARIES:
                coupling_count += 1
                print(f"  - Coupling via inheritance or import from: {base}")

        return coupling_count

    def to_string(self):
        result = []
        for class_name, coupling_value in self.class_map.items():
            result.append(f"{class_name}: {coupling_value} direct couplings")
        return "\n".join(result)

def get_classes_from_file(file_path):
    classes = []
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

        imported_classes = set()
        for node in ast.walk(tree):
            # Mengumpulkan nama kelas dari 'import' dan 'from ... import'
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_classes.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    for alias in node.names:
                        imported_classes.add(alias.name)

        # Memproses kelas dalam file
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                bases = [base.id for base in node.bases if isinstance(base, ast.Name)]
                # Menambahkan kelas yang diimpor ke daftar basis
                bases += [cls for cls in imported_classes if cls not in EXCLUDED_LIBRARIES]
                classes.append(ClassObject(class_name, bases))
                print(f"Analyzing Class: {class_name}\n  Bases: {bases}")
    return classes

def get_classes_from_directory(directory_path):
    all_classes = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                classes = get_classes_from_file(file_path)
                all_classes.extend(classes)
    return all_classes

# Ganti path dengan direktori yang ingin Anda analisis
directory_path = "../tests/"
classes_in_directory = get_classes_from_directory(directory_path)

# Hitung nilai DCC
dcc = DCC(classes_in_directory)

# Cetak rincian coupling per kelas
print(dcc.to_string())
