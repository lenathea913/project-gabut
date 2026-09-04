from exception import ProductNotAvailableError

class Product:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Inventory:
    def __init__(self):
        self.products = []
    
    def tambah_produk(self, nama, harga, stok):
        produk_baru = Product(nama, harga, stok)
        self.products.append(produk_baru)
        print(f'Produk {nama} berhasil ditambahkan ke inventaris.')
    
    def kurangi_stok(self, nama, jumlah):
        for produk in self.products:
            if produk.nama == nama:
                if produk.stok >= jumlah:
                    produk.stok -= jumlah
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

if __name__ == "__main__":
    print()
    print('==================================')
    print("=== Program Sistem Inventaris ===")
    print('==================================')
    
    print()
    print()
    
    inventaris = Inventory()
    inventaris.tambah_produk("Laptop", 15000000, 10)
    inventaris.tambah_produk("Mouse", 150000, 50)
    
    try:
        inventaris.kurangi_stok("Laptop", 5)
        inventaris.kurangi_stok("Mouse", 60)  # Akan memicu ProductNotAvailableError
    except ProductNotAvailableError as e:
        print(f"[ERROR]: {e}")