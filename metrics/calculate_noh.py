import ast
import os

def build_inheritance_map(directory):
    inheritance_map = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef):
                            # Mendapatkan nama kelas
                            class_name = node.name
                            # Mendapatkan nama superclass (jika ada)
                            base_classes = [base.id for base in node.bases if isinstance(base, ast.Name)]
                            # Menyimpan informasi kelas dan superclass
                            inheritance_map[class_name] = base_classes

    return inheritance_map

def count_noh(inheritance_map):
    noh_count = 0
    subclass_map = {}

    # Membangun peta subclass untuk setiap kelas
    for cls, bases in inheritance_map.items():
        for base in bases:
            if base in subclass_map:
                subclass_map[base].append(cls)
            else:
                subclass_map[base] = [cls]

    # Menghitung jumlah akar hierarki
    for cls, bases in inheritance_map.items():
        # Kelas dianggap sebagai akar hierarki jika:
        # - Tidak memiliki superclass (bases kosong)
        # - Memiliki setidaknya satu subclass dalam subclass_map
        if not bases and cls in subclass_map:
            noh_count += 1

    return noh_count

# Contoh penggunaan
directory_path = '../tests/'
inheritance_map = build_inheritance_map(directory_path)
noh = count_noh(inheritance_map)
print(f"Number of Hierarchies (NOH): {noh}")
