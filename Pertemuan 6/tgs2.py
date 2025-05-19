class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def lihat_barang(self):
        temp = self.head
        index = 0
        while temp is not None:
            print(f"{index}. {temp.value}")
            temp = temp.next
            index += 1
    
    def tambah_barang(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def hapus_paling_akhir(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def hapus_paling_pertama(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def ubah_barang(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def hapus_barang(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.hapus_paling_pertama()
        if index == self.length - 1:
            return self.hapus_paling_akhir()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


menu = LinkedList()
while True:
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Ubah Barang")
    print("4. Hapus Barang")
    print("5. Keluar Program")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        barang = input("Masukkan nama barang: ")
        menu.tambah_barang(barang)

    elif pilihan == "2":
        menu.lihat_barang()

    elif pilihan == "3":
        menu.lihat_barang()
        index = int(input("Masukkan index barang: "))
        barang_baru = input("Masukkan nama barang baru: ")
        menu.ubah_barang(index, barang_baru)

    elif pilihan == "4":
        menu.lihat_barang()
        index = int(input("Masukkan index barang: "))
        menu.hapus_barang(index)
        
    elif pilihan == "5":
        print("Keluar.")
        break
    else:
        print("Pilihan menggunakan angka (1,2,3,4,5)")
