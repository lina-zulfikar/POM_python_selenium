import os
import ast

# Daftar library atau modul yang ingin dikecualikan dari perhitungan MOA
EXCLUDED_LIBRARIES = {"selenium", "singleton", "DriverManager", "EC", "WebDriverWait"}

class MOACalculator(ast.NodeVisitor):
    def __init__(self):
        # Inisialisasi jumlah MOA dan set untuk modul yang diimpor
        self.moa_count = 0
        self.imported_modules = set()

    def visit_Import(self, node):
        # Menambahkan setiap modul yang diimpor ke dalam set imported_modules
        for alias in node.names:
            # Menyimpan hanya bagian pertama dari nama modul yang diimpor
            self.imported_modules.add(alias.name.split('.')[0])
        self.generic_visit(node)  # Melanjutkan ke elemen lain dari node

    def visit_ImportFrom(self, node):
        # Menambahkan modul yang diimpor menggunakan 'from ... import ...' ke imported_modules
        if node.module:
            self.imported_modules.add(node.module.split('.')[0])
        self.generic_visit(node)

    def visit_Assign(self, node):
        # Mengecek apakah ada instansiasi objek dalam penugasan (assignment)
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
            # Mendapatkan nama fungsi yang dipanggil
            func_name = node.value.func.id

            # Mengecek apakah nama fungsi tersebut bukan dari library yang dikecualikan
            if func_name not in EXCLUDED_LIBRARIES and func_name not in self.imported_modules:
                # Jika bukan, tambahkan ke perhitungan MOA
                self.moa_count += 1

        self.generic_visit(node)

    def calculate_moa(self, code):
        # Mengatur ulang jumlah MOA sebelum perhitungan baru
        self.moa_count = 0
        # Mengonversi kode Python menjadi Abstract Syntax Tree (AST)
        tree = ast.parse(code)
        # Memulai proses pengunjung AST untuk menghitung MOA
        self.visit(tree)
        return self.moa_count

def calculate_moa_for_directory(directory_path):
    # Inisialisasi total MOA untuk direktori
    total_moa = 0
    # Melakukan iterasi untuk setiap file dalam direktori dan subdirektori
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Memeriksa apakah file adalah file Python
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Membaca isi file Python
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    calculator = MOACalculator()
                    # Menghitung MOA untuk kode yang dibaca
                    moa_count = calculator.calculate_moa(code)
                    # Menambahkan hasil MOA ke total MOA
                    total_moa += moa_count
                    # Menampilkan jumlah MOA untuk setiap file
                    print(f"File: {file_path}, MOA count: {moa_count}")
    # Menampilkan total MOA untuk seluruh direktori
    print(f"Total MOA count for directory '{directory_path}': {total_moa}")

# Ganti path berikut sesuai dengan path direktori yang akan dihitung MOA-nya
directory_path = '../pages/'
# Memanggil fungsi untuk menghitung MOA dalam direktori yang ditentukan
calculate_moa_for_directory(directory_path)
