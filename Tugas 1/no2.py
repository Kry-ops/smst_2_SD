angka1 = int(input("Masukan angka 1 = "))
angka2 = int(input("Masukan angka 2 = "))

penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian = angka1 * angka2
pembagianA = angka1 // angka2
pembagianB = angka1/angka2
sisa_pembagian = angka1%angka2

if sisa_pembagian !=0 :
    print(f"penjumlahan {angka1}+{angka2}={penjumlahan}")
    print(f"pengurangan {angka1}-{angka2}={pengurangan}")
    print(f"perkalian {angka1}*{angka2}={perkalian}")
    print(f"pembagian {angka1}/{angka2}={pembagianB}")
    print(f"dengan sisa pembagian = {sisa_pembagian}")
else:
    print(f"penjumlahan {angka1}+{angka2}={penjumlahan}")
    print(f"pengurangan {angka1}-{angka2}={pengurangan}")
    print(f"perkalian {angka1}*{angka2}={perkalian}")
    print(f"pembagian {angka1}//{angka2}={pembagianA}")
