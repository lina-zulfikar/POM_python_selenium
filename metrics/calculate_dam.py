import ast
import os
from collections import defaultdict

# Class untuk menelusuri dan mengumpulkan informasi tentang atribut kelas.
class DAMVisitor(ast.NodeVisitor):
    def __init__(self):
        # Menyimpan jumlah total, privat, dan protected attributes untuk setiap kelas.
        # Menggunakan defaultdict untuk menginisialisasi dictionary secara otomatis.
        self.class_attributes = defaultdict(lambda: {'total': 0, 'private': 0, 'protected': 0})

    # Method ini dipanggil setiap kali ditemukan definisi kelas (ClassDef) dalam AST.
    def visit_ClassDef(self, node):
        # Simpan nama kelas saat ini.
        current_class = node.name
        # Iterasi melalui setiap statement dalam tubuh kelas.
        for stmt in node.body:
            # Cek apakah statement tersebut adalah assignment (penugasan atribut).
            if isinstance(stmt, ast.Assign):
                # Iterasi melalui setiap target dari penugasan (atribut yang didefinisikan).
                for target in stmt.targets:
                    # Cek apakah target adalah nama (atribut).
                    if isinstance(target, ast.Name):
                        # Tambahkan satu ke jumlah total atribut untuk kelas ini.
                        self.class_attributes[current_class]['total'] += 1
                        # Jika atribut dimulai dengan '__' (tapi tidak diakhiri '__'), anggap sebagai private.
                        if target.id.startswith('__') and not target.id.endswith('__'):
                            self.class_attributes[current_class]['private'] += 1
                        # Jika atribut dimulai dengan satu '_', anggap sebagai protected.
                        elif target.id.startswith('_'):
                            self.class_attributes[current_class]['protected'] += 1
        # Lanjutkan penelusuran untuk node lainnya dalam kelas.
        self.generic_visit(node)

# Fungsi untuk menghitung DAM dari file Python tertentu.
def calculate_dam_in_file(file_path, visitor):
    # Baca isi file Python dan parse menjadi AST.
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    # Kunjungi setiap node dalam AST untuk mengumpulkan informasi atribut.
    visitor.visit(tree)

# Fungsi untuk menghitung DAM dari semua file Python dalam direktori.
def calculate_dam_in_directory(directory):
    # Buat objek DAMVisitor untuk menelusuri semua atribut.
    visitor = DAMVisitor()
    # Iterasi melalui setiap file dalam direktori.
    for root, _, files in os.walk(directory):
        for file in files:
            # Jika file berakhiran .py, berarti itu adalah file Python.
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Hitung DAM untuk file ini.
                calculate_dam_in_file(file_path, visitor)
    
    # Kembalikan informasi atribut yang dikumpulkan.
    return visitor.class_attributes

# Fungsi untuk menghitung nilai DAM dari informasi atribut yang dikumpulkan.
def calculate_dam(class_attributes):
    dam_values = {}
    # Iterasi melalui setiap kelas dan atributnya.
    for cls, attrs in class_attributes.items():
        # Hitung DAM hanya jika jumlah total atribut lebih dari 0.
        if attrs['total'] > 0:
            # Hitung DAM sebagai (jumlah private + protected) / jumlah total atribut.
            dam = (attrs['private'] + attrs['protected']) / attrs['total']
        else:
            # Jika kelas tidak memiliki atribut, DAM diset ke 0.
            dam = 0
        # Simpan nilai DAM untuk kelas ini.
        dam_values[cls] = dam
    return dam_values

# Fungsi untuk mencetak nilai DAM dari setiap kelas dan menghitung total DAM.
def print_dam(dam_values, class_attributes):
    total_dam = 0
    for cls, dam in dam_values.items():
        # Tampilkan DAM meskipun nilainya adalah 0, serta atribut yang dihitung.
        attrs = class_attributes[cls]
        print(f"Class: {cls}, Total Attributes: {attrs['total']}, Private: {attrs['private']}, Protected: {attrs['protected']}, DAM: {dam:.2f}")
        total_dam += dam

    # Menampilkan total DAM (rata-rata dari semua kelas)
    num_classes = len(dam_values)
    if num_classes > 0:
        average_dam = total_dam / num_classes
        print(f"\nTotal DAM across all classes: {total_dam:.2f}")
        print(f"Average DAM across all classes: {average_dam:.2f}")
    else:
        print("No classes found to calculate DAM.")

# Bagian utama untuk menjalankan perhitungan DAM.
if __name__ == "__main__":
    directory = "../tests/"  # Ganti dengan path ke direktori proyek Anda
    # Hitung atribut kelas dari semua file dalam direktori.
    class_attributes = calculate_dam_in_directory(directory)
    # Hitung nilai DAM untuk setiap kelas.
    dam_values = calculate_dam(class_attributes)
    # Cetak hasil DAM dari setiap kelas.
    print_dam(dam_values, class_attributes)
