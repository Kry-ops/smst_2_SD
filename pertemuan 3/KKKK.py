class Manusia:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
    
    def perkenalan(self):
        return f"Nama : {self.nama}, Jenis kelamin : {self.jenis_kelamin}."

class Mahasiswa(Manusia):
    def __init__(self, nama, jenis_kelamin, NPM, nilai):
        super().__init__(nama, jenis_kelamin)
        self.NPM = NPM
        self.nilai = nilai
    
    def deskripsi(self):
        return f"Nama : {self.nama}, NPM = {self.NPM}, Nilai ujian = {self.nilai}."
    
    def ubah_NPM(self, ubah_npm):
        self.NPM = ubah_npm
        return f"NPM Baru = {self.NPM}."
    
    def tambah_nilai(self, nilai_tambah):
        self.nilai += nilai_tambah
        return f"Nilai Baru = {self.nilai}."

# Contoh penggunaan
mahasiswa1 = Mahasiswa("Gevaldo wiratmal putra pratama lay", "Laki-laki", "5240411141", 80)
print(mahasiswa1.perkenalan())
print(mahasiswa1.deskripsi())
print(mahasiswa1.ubah_NPM("1411140425"))
print(mahasiswa1.tambah_nilai(10))
