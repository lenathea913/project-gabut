from exception import ProductNotAvailableError
import json
import os
class Product:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Inventory:
    def __init__(self):
        self.products = []
        self.gudang = os.path.join(os.path.dirname(__file__), 'gudang.json')
        self.load_products()
    
    def load_products(self):
        self.products.clear()
        if os.path.exists(self.gudang):
            try:
                with open(self.gudang, 'r') as file:
                    produk_data = json.load(file)
                    for data in produk_data:
                        produk = Product(
                            nama=data['nama'],
                            harga=data['harga'],
                            stok=data['stok']
                        )
                        self.products.append(produk)
            except json.JSONDecodeError:
                print("Error: Gagal memuat data produk. Format JSON tidak valid.")
        else:
            print('File gudang.json tidak ditemukan.')
    
    def save_data(self):
        with open(self.gudang, 'w') as file:
            json.dump([vars(produk) for produk in self.products], file)
    
    def tambah_produk(self, nama, harga, stok):
        produk_baru = Product(nama, harga, stok)
        self.products.append(produk_baru)
        self.save_data()
        print(f'Produk {nama} berhasil ditambahkan ke inventaris.')
    
    def kurangi_stok(self, nama, jumlah):
        for produk in self.products:
            if produk.nama == nama:
                if produk.stok >= jumlah:
                    produk.stok -= jumlah
                    self.save_data()
                    print(f'Stok produk {nama} berhasil dikurangi sebanyak {jumlah}.')
                else:
                    raise ProductNotAvailableError(f'Stok produk {nama} tidak mencukupi.')
            else:
                raise ProductNotAvailableError(f'Produk {nama} tidak ditemukan dalam inventaris.')
    
    def cari_produk(self, nama):
        for produk in self.products:
            if produk.nama == nama:
                return produk
        raise ProductNotAvailableError(f'Produk {nama} tidak ditemukan dalam inventaris.')
    
    def lihat_gudang(self):
        if not self.products:
            print('Gudang Kosong.')
        else:
            print('Daftar produk dalam gudang.')
            for produk in self.products:
                print(f'Nama: {produk.nama:10} | Harga: {produk.harga:10,.0f} | Stok: {produk.stok:10,.0f}')
        

if __name__ == "__main__":
    while True:
        print()
        print('==================================')
        print("=== Program Sistem Inventaris ===")
        print('==================================')
        print('1. Tambah Produk')
        print('2. Kurangi Stok')
        print('3. Cari Produk')
        print('4. Lihat Gudang')
        print('5. Keluar')
        
        user = input('Masukkan pilihan (1-5): ')
        
        if user == '1':
            nama = input('Masukkan nama produk: ')
            harga = float(input('Masukkan harga produk: '))
            stok = int(input('Masukkan stok produk: '))
            inventory = Inventory()
            inventory.tambah_produk(nama, harga, stok)
            
        elif user == '2':
            nama = input('Masukkan Nama produk: ').lower()
            jumlah = int(input('Masukkan jumlah: '))
            inventory = Inventory()
            try:
                inventory.kurangi_stok(nama, jumlah)
            except ProductNotAvailableError as e:
                print(e)
            
        elif user == '3':
            nama = input('Masukkan nama produk: ').lower()
            inventory = Inventory()
            try:
                produk = inventory.cari_produk(nama)
                print(f'Produk ditemukan: {produk.nama}, Harga: {produk.harga}, Stok: {produk.stok}')
            except ProductNotAvailableError as e:   
                print(e)
            
        elif user == '4':
            inventory = Inventory()
            inventory.lihat_gudang()
        
        elif user == '5':
            print('Terima kasih telah menggunakan program ini.')
            break
            
        else:
            print('Pilihan tidak valid. Silakan pilih antara 1-4.')
    