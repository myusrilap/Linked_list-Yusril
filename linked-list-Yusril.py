class LinkedList:
    def __init__(self):
        self.head = None
        self.history = []

    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self.history.append(("add", item))

    def remove(self, index):
        try:
            if not self.head:
                raise Exception("Daftar belanjaan kosong.")
            if not isinstance(index, int):
                raise Exception("Nomor index harus berupa angka.")
            if index == 0:
                removed_item = self.head.item
                self.head = self.head.next_node
                self.history.append(("remove", removed_item))
                return
            current = self.head
            prev = None
            i = 0
            while current:
                if i == index:
                    removed_item = current.item
                    prev.next_node = current.next_node
                    self.history.append(("remove", removed_item))
                    return
                prev = current
                current = current.next_node
                i += 1
            raise Exception("Nomor index tidak valid.")
        except Exception as e:
            print(f"Gagal menghapus belanjaan: {e}")

    def display(self):
        if not self.head:
            print("Daftar belanjaan kosong.")
        else:
            current = self.head
            i = 1
            while current:
                print(f"{i}. {current.item}")
                current = current.next_node
                i += 1

    def display_history(self):
        if not self.history:
            print("Belum ada operasi yang dilakukan.")
        else:
            print("History:")
            for operation in self.history:
                if operation[0] == "add":
                    print(f"Tambah belanjaan: {operation[1]}")
                elif operation[0] == "remove":
                    print(f"Hapus belanjaan: {operation[1]}")

class Node():
    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node


def main():
    shopping_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Tambah belanjaan")
        print("2. Hapus belanjaan")
        print("3. Tampilkan daftar belanjaan")
        print("4. Tampilkan history")
        print("5. Keluar")
        choice = input("Pilih menu (1/2/3/4/5): ")
        if choice == "1":
            item = input("Masukkan nama belanjaan: ")
            shopping_list.add(item)
            print(f"{item} telah ditambahkan ke daftar belanjaan.")
        elif choice == "2":
            print("Daftar belanjaan:")
            shopping_list.display()
            try:
                index = int(input("Masukkan nomor index belanjaan yang ingin dihapus: ")) - 1
                shopping_list.remove(index)
            except ValueError:
                print("Nomor index harus berupa angka.")
        elif choice == "3":
            print("Daftar belanjaan:")
            shopping_list.display()
        elif choice == "4":
            shopping_list.display_history()
        elif choice == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
