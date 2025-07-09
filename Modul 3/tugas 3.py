# Kelas Node untuk linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Kelas Stack dengan kapasitas
class Stack:
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity
        self.count = 0

    # 1. Fungsi menambah elemen ke stack
    def push(self, data):
        if self.is_full():
            print("Stack sudah penuh!")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"Stack: {self.display()}")

    # 2. Fungsi menghapus elemen dari stack
    def pop(self):
        if self.top is None:
            print("Stack kosong, tidak bisa hapus.")
            return
        removed_data = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(f"Data {removed_data} berhasil dihapus.")
        print(f"Stack: {self.display()}")

    # 3. Fungsi cek ukuran stack saat ini
    def size(self):
        print(f"Ukuran stack saat ini: {self.count}")

    # 4. Fungsi cek elemen paling atas
    def peek(self):
        if self.top is None:
            print("Stack kosong.")
        else:
            print(f"Elemen puncak stack: {self.top.data}")

    # 5. Fungsi cek apakah stack penuh
    def is_full(self):
        return self.count == self.capacity

    # Fungsi bantu menampilkan isi stack
    def display(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result[::-1]  # Supaya urut dari bawah ke atas


# Program utama
print("===== PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST =====")
kapasitas = int(input("Tentukan berapa kapasitas stack: "))
stack = Stack(kapasitas)

while True:
    print("\nPilih menu berikut ini:")
    print("1. Menambah isi stack")
    print("2. Menghapus isi stack")
    print("3. Cek Ukuran Stack saat ini")
    print("4. Cek Puncak Stack")
    print("5. Cek Stack Full")
    print("6. Keluar")
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == "1":
        while True:
            if stack.is_full():
                print("Stack sudah penuh, tidak bisa menambah lagi.")
                break
            isi = input("Masukkan isi stack: ")
            stack.push(isi)
            lagi = input("Menambah isi Stack Pilih [Ya/Tidak]: ")
            if lagi.lower() != "ya":
                break

    elif pilihan == "2":
        stack.pop()

    elif pilihan == "3":
        stack.size()

    elif pilihan == "4":
        stack.peek()

    elif pilihan == "5":
        if stack.is_full():
            print("Stack dalam kondisi penuh.")
        else:
            print("Stack masih ada ruang.")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")