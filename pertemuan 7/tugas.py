class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True
    
    def hapus_paling_akhir(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def hapus_paling_pertama(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
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
            
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        if temp.next:  
            temp.next.prev = prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


menu = DoublyLinkedList()
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