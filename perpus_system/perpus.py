from .buku import book
from .exception import BookNotFoundError, BukuSudahDipinjam
import json
import os

class library:
    def __init__(self):
        self.books = []
        self.books_file = os.path.join(os.path.dirname(__file__), 'books.json')
    
    def load_books(self):
        self.books.clear()
        if os.path.exists(self.books_file):
            try:
                with open(self.books_file, 'r') as file:
                    books_data = json.load(file)
                    for buku_data in books_data:
                        buku = book(
                            judul=buku_data['judul'],
                            penulis=buku_data['penulis'],
                            tahun=buku_data['tahun'],
                            status=buku_data['status']
                        )
                        self.books.append(buku)
            except json.JSONDecodeError:
                print("Error: Gagal memuat data buku. Format JSON tidak valid.")
        else:
            print("File books.json tidak ditemukan. Data buku kosong.")

    
    def save_books(self):
        with open(self.books_file, 'w') as file:
            json.dump([vars(buku) for buku in self.books], file)

    def tambah_buku(self, judul, penulis, tahun, status):
        buku_baru = book(judul, penulis, tahun, status)
        self.books.append(buku_baru)
        self.save_books()
        print(f"Buku '{judul}' berhasil ditambahkan.")
        
    
    def cari_buku(self, judul):
        for buku in self.books:
            if buku.judul == judul:
                return buku
        return None
    
    def pinjam_buku(self, judul):
        buku = self.cari_buku(judul)
        if buku is None:
            raise BookNotFoundError("Buku tidak ditemukan")
        if buku.status != "tersedia":
            raise BukuSudahDipinjam("Buku sudah dipinjam")
        buku.status = "dipinjam"
        self.save_books()
        return True
    
    def kembalikan_buku(self, judul):
        buku = self.cari_buku(judul)
        if buku is None:
            raise BookNotFoundError("Buku tidak ditemukan")
        if buku.status != "dipinjam":
            raise BookNotFoundError("Buku sedang tidak dipinjam")
        buku.status = "tersedia"
        self.save_books()
        return True
    
    def menu(self):
        while True:
                    print("=== Menu Perpustakaan ===")
                    print("1. Tambah Buku")
                    print("2. Cari Buku")
                    print("3. Pinjam Buku")
                    print("4. Kembalikan Buku")
                    
                    user = input('Pilih Menu(q to quit): ')
                    
                    if user == '1':
                        judul = input('Masukkan Judul Buku: ').capitalize()
                        penulis = input('Masukkan Nama Penulis: ').capitalize()
                        tahun = input('Masukkan Tahun Terbit: ')
                        status = "tersedia"
                        self.tambah_buku(judul, penulis, tahun, status)
                    
                    elif user == '2':
                        judul = input('Masukkan Judul Buku: ').capitalize()
                        buku = self.cari_buku(judul)
                        if buku is not None:
                            print(f"Judul: {buku.judul}")
                            print(f"Penulis: {buku.penulis}")
                            print(f"Tahun Terbit: {buku.tahun}")
                            print(f"Status: {buku.status}")
                        else:
                            print("Buku tidak ditemukan.")
                        
                    elif user == '3':
                        judul = input('Masukkan Judul Buku: ').capitalize()
                        try:
                            if self.pinjam_buku(judul):
                                print(f"Buku '{judul}' berhasil dipinjam.")
                        except (BookNotFoundError, BukuSudahDipinjam) as e:
                            print(f"[ERROR]: {e}")
                    
                    elif user == '4':
                        judul = input('Masukkan Judul Buku: ').capitalize()
                        try:
                            if self.kembalikan_buku(judul):
                                print(f"Buku '{judul}' berhasil dikembalikan.")
                        except BookNotFoundError as e:
                            print(f"[ERROR]: {e}")
                    
                    elif user == 'q' or user == 'Q':
                        print("Terima kasih telah menggunakan sistem perpustakaan.")
                        break
                    
                    else:
                        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    perpustakaan = library()
    perpustakaan.load_books()
    perpustakaan.menu()
    
