def hitung_simulasi_kredit(harga_barang, uang_muka, bunga_tahunan, tahun_kredit): 

    jumlah_pinjaman =  harga_barang-uang_muka 

    bunga_bulanan = (bunga_tahunan / 100) /12 

    jumlah_cicilan_bulanan = jumlah_pinjaman*(bunga_bulanan / (1 - (1 + bunga_bulanan)**(-tahun_kredit*12))) 

    total_pembayaran = jumlah_cicilan_bulanan * tahun_kredit * 12 

    return total_pembayaran, jumlah_cicilan_bulanan

harga_iphone = 32999000 
uang_muka = 5000000 
bunga_tahunan = 4+1 #no 2
tahun_kredit = 2 #no 1
total_pembayaran, jumlah_cicilan_bulanan = hitung_simulasi_kredit(harga_iphone, uang_muka, bunga_tahunan, tahun_kredit) 
print(f"Total yang harus dibayar: Rp {round(total_pembayaran):,}") #no 4
print(f"Cicilan bulanan yang harus dibayar selama {tahun_kredit} tahun dengan suku bunga {bunga_tahunan}% : Rp {round(jumlah_cicilan_bulanan):,}") #no 3 dan no 4
