nama = str(input("Masukan nama lengkap : "))

from datetime import datetime

tanggal = int(input("Masukkan tanggal lahir : "))
bulan = int(input("Masukkan bulan lahir : "))
tahun = int(input("Masukkan tahun lahir : "))

tanggal_lahir = datetime(tahun, bulan, tanggal)
hari_ini = datetime(2025, 2, 12)
usia = (hari_ini - tanggal_lahir)
usia_dalam_tahun = (usia.days)//365

print(f"Hai, {nama}! pada hari ini Rabu 12 Februari 2025 Anda berumur {usia_dalam_tahun} tahun. Selamat belajar Struktur Data")