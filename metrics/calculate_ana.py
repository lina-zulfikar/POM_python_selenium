import os
import ast

class SystemObject:
    def __init__(self, classes):
        """
        Inisialisasi SystemObject dengan daftar kelas yang ada dalam sistem.
        
        Args:
        classes (list): Daftar objek ClassObject yang ada dalam sistem.
        """
        self.classes = classes

    def get_class_objects(self):
        """
        Mengembalikan daftar kelas dalam sistem.
        
        Returns:
        list: Daftar objek ClassObject.
        """
        return self.classes

class ClassObject:
    def __init__(self, name, ancestors):
        """
        Inisialisasi objek ClassObject.
        
        Args:
        name (str): Nama kelas.
        ancestors (list): Daftar kelas leluhur (ancestors).
        """
        self.name = name
        self.ancestors = ancestors

    def get_name(self):
        """
        Mengembalikan nama kelas.
        
        Returns:
        str: Nama kelas.
        """
        return self.name

class DIT:
    def __init__(self, system):
        """
        Inisialisasi objek DIT dengan sistem yang diberikan.
        
        Args:
        system (SystemObject): Sistem yang berisi semua kelas.
        """
        self.system = system

    def DIT_calculation(self, system, class_object):
        """
        Menghitung jumlah leluhur (DIT) untuk kelas tertentu.
        
        Args:
        system (SystemObject): Sistem yang berisi semua kelas.
        class_object (ClassObject): Kelas yang ingin dihitung jumlah leluhurnya.
        
        Returns:
        int: Jumlah leluhur kelas.
        """
        return len(class_object.ancestors)

class ANA:
    def __init__(self, system):
        """
        Inisialisasi objek ANA dan hitung nilai ANA (Average Number of Ancestors).
        
        Args:
        system (SystemObject): Sistem yang berisi semua kelas.
        """
        self.ana_value = 0.0
        self.m_sys = system
        self.class_map = {}  # Peta nama kelas ke jumlah leluhurnya
        self.calc_ana()

    def calc_ana(self):
        """
        Menghitung nilai ANA (rata-rata jumlah leluhur) untuk setiap kelas.
        """
        classes = self.m_sys.get_class_objects()
        dit = DIT(self.m_sys)
        dit_value = 0.0

        for c in classes:
            DIT_count = dit.DIT_calculation(self.m_sys, c)
            dit_value += DIT_count
            self.class_map[c.get_name()] = DIT_count

        # Hitung rata-rata jumlah leluhur
        if len(classes) > 0:
            self.ana_value = dit_value / len(classes)

    def get_ANA(self):
        """
        Mengembalikan nilai ANA yang sudah dihitung.
        
        Returns:
        float: Nilai ANA.
        """
        return self.ana_value

    def __str__(self):
        """
        Mengembalikan nilai ANA dalam bentuk string.
        
        Returns:
        str: Representasi string dari nilai ANA.
        """
        return f" {self.ana_value}"

    def to_string2(self):
        """
        Mengembalikan string dengan nama kelas dan jumlah leluhurnya.
        
        Returns:
        str: String yang berisi nama kelas dan jumlah leluhurnya.
        """
        result = []
        for class_name, dit_count in self.class_map.items():
            result.append(f"{class_name}\t{dit_count}")
        return "\n".join(result)

def get_classes_from_file(file_path):
    """
    Mengambil daftar kelas dari file Python.
    
    Args:
    file_path (str): Jalur file Python.
    
    Returns:
    list: Daftar objek ClassObject yang berisi nama kelas dan leluhurnya.
    """
    classes = []
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                ancestors = [base.id for base in node.bases if isinstance(base, ast.Name)]
                classes.append(ClassObject(class_name, ancestors))
    return classes

def get_classes_from_directory(directory_path):
    """
    Mengambil semua kelas dari file Python dalam direktori.
    
    Args:
    directory_path (str): Jalur direktori.
    
    Returns:
    list: Daftar semua ClassObject dari direktori.
    """
    all_classes = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                all_classes.extend(get_classes_from_file(file_path))
    return all_classes

# Contoh penggunaan:
# Cari kelas di direktori ../pages
directory_path = "../tests/"
classes_in_directory = get_classes_from_directory(directory_path)

# Buat objek SystemObject dari kelas-kelas yang ditemukan
system = SystemObject(classes_in_directory)

# Hitung nilai ANA
ana = ANA(system)

# Cetak nilai ANA
print("ANA Value:", ana.get_ANA())

# Cetak rincian setiap kelas dan jumlah leluhurnya
print("Detail kelas dan leluhurnya:")
print(ana.to_string2())
