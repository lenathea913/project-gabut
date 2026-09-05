import json
import os
from exceptions import ProductNotAvailableError

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
GUDANG_FILE = os.path.join(DATA_DIR, 'gudang.json')


class Product:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok


class Inventory:
    def __init__(self):
        self.products = []
        self.gudang = GUDANG_FILE
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
                            stok=data['stok'],
                        )
                        self.products.append(produk)
            except json.JSONDecodeError:
                print("Error: Gagal memuat data produk. Format JSON tidak valid.")

    def save_data(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(self.gudang, 'w') as file:
            json.dump([vars(produk) for produk in self.products], file, indent=2)

    def tambah_produk(self, nama, harga, stok):
        if not nama or len(nama.strip()) == 0:
            print("Nama tidak boleh kosong.")
            return
        if harga <= 0:
            print("Harga tidak boleh negatif atau nol.")
            return
        if stok <= 0:
            print("Stok tidak boleh negatif atau nol.")
            return
        produk_baru = Product(nama, harga, stok)
        self.products.append(produk_baru)
        self.save_data()
        print(f"Produk {nama} berhasil ditambahkan ke inventaris.")

    def kurangi_stok(self, nama, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari 0.")
        for produk in self.products:
            if produk.nama.lower() == nama.lower():
                if produk.stok >= jumlah:
                    produk.stok -= jumlah
                    self.save_data()
                    print(f"Stok produk {nama} berhasil dikurangi sebanyak {jumlah}.")
                    return
                else:
                    raise ProductNotAvailableError(
                        f"Stok produk {nama} tidak mencukupi (sisa: {produk.stok})."
                    )
        raise ProductNotAvailableError(f"Produk {nama} tidak ditemukan dalam inventaris.")

    def cari_produk(self, nama):
        for produk in self.products:
            if produk.nama.lower() == nama.lower():
                return produk
        raise ProductNotAvailableError(f"Produk {nama} tidak ditemukan dalam inventaris.")

    def lihat_gudang(self):
        if not self.products:
            print("Gudang Kosong.")
        else:
            print("Daftar produk dalam gudang:")
            print("-" * 60)
            print(f"{'No':<4} {'Nama':<20} {'Harga':>15} {'Stok':>10}")
            print("-" * 60)
            for i, produk in enumerate(self.products, 1):
                print(
                    f"{i:<4} {produk.nama:<20} Rp.{produk.harga:>12,.0f} {produk.stok:>10}"
                )
            print("-" * 60)

    def list_produk_untuk_belanja(self):
        """Menampilkan produk yang tersedia (stok > 0) untuk menu belanja."""
        tersedia = [p for p in self.products if p.stok > 0]
        if not tersedia:
            print("Tidak ada produk yang tersedia.")
            return []
        print("Produk yang tersedia:")
        print("-" * 60)
        print(f"{'No':<4} {'Nama':<20} {'Harga':>15} {'Stok':>10}")
        print("-" * 60)
        for i, produk in enumerate(tersedia, 1):
            print(
                f"{i:<4} {produk.nama:<20} Rp.{produk.harga:>12,.0f} {produk.stok:>10}"
            )
        print("-" * 60)
        return tersedia

    def update_harga(self, nama, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga tidak boleh negatif atau nol.")
        produk = self.cari_produk(nama)
        produk.harga = harga_baru
        self.save_data()
        print(f"Harga produk {nama} berhasil diupdate.")

    def update_stok(self, nama, stok_baru):
        if stok_baru <= 0:
            raise ValueError("Stok tidak boleh negatif atau nol.")
        produk = self.cari_produk(nama)
        produk.stok += stok_baru
        self.save_data()
        print(f"Stok produk {nama} berhasil ditambahkan. Stok sekarang: {produk.stok}.")
