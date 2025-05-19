
# def keranjang():


Keranjang = []

def aplikasi_sederhana():

    menu = input("Silahkan memilih menu (Menambah barang), (Melihat barang),  (Menghapus barang), (Keluar) : ")

    if menu == "Menambah barang":
        tambah = input("Silahkan menambah barang : ")
        Keranjang.append (tambah)
        print(f"Berhasil menambahkan barang = {Keranjang}")
        return aplikasi_sederhana()
    
    elif menu == "Melihat barang" :
        print(f"Daftar barang = {Keranjang}")
        return aplikasi_sederhana()
        
    elif menu == "Menghapus barang" :
        print(f"Daftar barang = {Keranjang}")
        hapus = int(input("Masukan index barang yang mau dihapus (dimulai dari index[0]) : "))
        Keranjang.pop(hapus)
        print(f"Barang berhasil dihapus = {Keranjang}")
        return aplikasi_sederhana()
       
    elif menu == "Keluar":
        exit()
    else:
        print("Tolong masukan sesuai menu")
        return aplikasi_sederhana()
    

Keranjang = aplikasi_sederhana()
    
