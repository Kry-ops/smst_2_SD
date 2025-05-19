class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            print("Linked List kosong.\n")
            return
        temp = self.head
        print("Linked List saat ini:")
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None\n")

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        print(f"Node {value} berhasil ditambahkan!\n")

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            print(f"Node di indeks {index} berhasil diubah menjadi {value}!\n")
            return True
        print("Indeks tidak valid!\n")
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Indeks tidak valid!\n")
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        print(f"Node {temp.value} berhasil dihapus dari indeks {index}!\n")
        return temp.value

    def pop_first(self):
        if self.length == 0:
            print("Linked List kosong!\n")
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        print(f"Node {temp.value} berhasil dihapus dari awal!\n")
        return temp.value

    def pop(self):
        if self.length == 0:
            print("Linked List kosong!\n")
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        print(f"Node {temp.value} berhasil dihapus dari akhir!\n")
        return temp.value


# Menu utama
def menu():
    linked_list = LinkedList(1)  # Mulai dengan satu node awal
    while True:
        print("\n=== Menu Linked List ===")
        print("1. Tambah Node (Akhir)")
        print("2. Tampilkan Linked List")
        print("3. Ubah Node")
        print("4. Hapus Node (Indeks tertentu)")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            try:
                value = int(input("Masukkan nilai node baru: "))
                linked_list.append(value)
            except ValueError:
                print("Masukkan harus berupa angka!\n")

        elif pilihan == "2":
            linked_list.print_list()

        elif pilihan == "3":
            try:
                index = int(input("Masukkan indeks node yang ingin diubah: "))
                value = int(input("Masukkan nilai baru: "))
                linked_list.set_value(index, value)
            except ValueError:
                print("Masukkan harus berupa angka!\n")

        elif pilihan == "4":
            try:
                index = int(input("Masukkan indeks node yang ingin dihapus: "))
                linked_list.remove(index)
            except ValueError:
                print("Masukkan harus berupa angka!\n")

        elif pilihan == "5":
            print("Program selesai. Terima kasih!\n")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi!\n")


# Menjalankan menu
menu()
