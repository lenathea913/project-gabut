import sys

from models.bank_account import BankAccount
from models.inventory import Inventory
from models.payment import CreditCard, BankTransfer, EWallet
from exceptions import (
    DanaTidakCukup,
    InvalidAmountError,
    AccountLockedError,
    ProductNotAvailableError,
    PembayaranGagalError,
    DataTidakValidError,
)


def menu_akun_bank(accounts):
    while True:
        print("\n╔══════════════════════════════════╗")
        print("║     KELOLA AKUN BANK             ║")
        print("╠══════════════════════════════════╣")
        print("║  1. Buat Akun Baru               ║")
        print("║  2. Pilih Akun Aktif             ║")
        print("║  3. Cek Saldo                    ║")
        print("║  4. Setor Dana                   ║")
        print("║  5. Tarik Dana                   ║")
        print("║  6. Transfer Dana                ║")
        print("║  7. Lihat Riwayat Transaksi      ║")
        print("║  8. Kunci / Buka Akun            ║")
        print("║  0. Kembali ke Menu Utama        ║")
        print("╚══════════════════════════════════╝")
        choice = input("Pilih menu: ")

        if choice == '0':
            break
        elif choice == '1':
            nama = input("Masukkan nama pemilik akun: ").strip()
            if not nama:
                print("Nama tidak boleh kosong.")
                continue
            if nama in accounts:
                print("Akun dengan nama tersebut sudah ada.")
                continue
            try:
                saldo = float(input("Masukkan saldo awal: Rp."))
                akun = BankAccount(nama, saldo)
                akun.save_account_data()
                accounts[nama] = akun
                print(f"Akun bank untuk '{nama}' berhasil dibuat.")
            except ValueError:
                print("Saldo awal harus berupa angka yang valid.")
        elif choice == '2':
            if not accounts:
                print("Belum ada akun. Silakan buat akun terlebih dahulu.")
                continue
            print("Akun tersedia:", ', '.join(accounts.keys()))
            nama = input("Masukkan nama pemilik akun: ").strip()
            if nama in accounts:
                print(f"Akun aktif: {nama} (Saldo: Rp.{accounts[nama].get_balance():,.0f})")
            else:
                print("Akun tidak ditemukan.")
        elif choice == '3':
            akun = _pilih_akun_aktif(accounts)
            if akun:
                try:
                    print(f"Saldo saat ini: Rp.{akun.get_balance():,.0f}")
                except AccountLockedError as e:
                    print(f"Error: {e}")
        elif choice == '4':
            akun = _pilih_akun_aktif(accounts)
            if akun:
                try:
                    amount = float(input("Masukkan jumlah setoran: Rp."))
                    akun.deposit(amount)
                    print(f"Setor berhasil! Saldo saat ini: Rp.{akun.get_balance():,.0f}")
                except ValueError:
                    print("Jumlah setoran harus berupa angka.")
                except (AccountLockedError, InvalidAmountError) as e:
                    print(f"Error: {e}")
        elif choice == '5':
            akun = _pilih_akun_aktif(accounts)
            if akun:
                try:
                    amount = float(input("Masukkan jumlah penarikan: Rp."))
                    akun.withdraw(amount)
                    print(f"Penarikan berhasil! Saldo saat ini: Rp.{akun.get_balance():,.0f}")
                except ValueError:
                    print("Jumlah penarikan harus berupa angka.")
                except (AccountLockedError, InvalidAmountError, DanaTidakCukup) as e:
                    print(f"Error: {e}")
        elif choice == '6':
            akun = _pilih_akun_aktif(accounts)
            if akun:
                try:
                    amount = float(input("Masukkan jumlah transfer: Rp."))
                    target_name = input("Masukkan nama pemilik akun tujuan: ").strip()
                    target = accounts.get(target_name)
                    if target is None:
                        print("Akun tujuan tidak ditemukan.")
                        continue
                    akun.transfer(amount, target)
                    print(f"Transfer Rp.{amount:,.0f} ke '{target_name}' berhasil!")
                except ValueError:
                    print("Jumlah transfer harus berupa angka.")
                except (AccountLockedError, InvalidAmountError, DanaTidakCukup) as e:
                    print(f"Error: {e}")
        elif choice == '7':
            akun = _pilih_akun_aktif(accounts)
            if akun:
                try:
                    akun.print_transaction_history()
                except AccountLockedError as e:
                    print(f"Error: {e}")
        elif choice == '8':
            akun = _pilih_akun_aktif(accounts)
            if akun:
                print("1. Kunci Akun  2. Buka Akun")
                sub = input("Pilih: ")
                if sub == '1':
                    try:
                        akun.lock_account()
                        print("Akun telah dikunci.")
                    except AccountLockedError as e:
                        print(f"Error: {e}")
                elif sub == '2':
                    akun.unlock_account()
                    print("Akun telah dibuka.")
                else:
                    print("Pilihan tidak valid.")
        else:
            print("Pilihan tidak valid.")


def menu_inventaris(inventory):
    while True:
        print("\n╔══════════════════════════════════╗")
        print("║     KELOLA INVENTARIS            ║")
        print("╠══════════════════════════════════╣")
        print("║  1. Tambah Produk                ║")
        print("║  2. Kurangi Stok                 ║")
        print("║  3. Cari Produk                  ║")
        print("║  4. Lihat Gudang                 ║")
        print("║  5. Update Harga Produk          ║")
        print("║  6. Update Stok Produk           ║")
        print("║  0. Kembali ke Menu Utama        ║")
        print("╚══════════════════════════════════╝")
        choice = input("Pilih menu: ")

        if choice == '0':
            break
        elif choice == '1':
            nama = input("Masukkan nama produk: ").strip()
            try:
                harga = float(input("Masukkan harga produk: Rp."))
                stok = int(input("Masukkan stok produk: "))
                inventory.tambah_produk(nama, harga, stok)
            except ValueError:
                print("Harga dan stok harus berupa angka.")
        elif choice == '2':
            nama = input("Masukkan nama produk: ").strip()
            try:
                jumlah = int(input("Masukkan jumlah yang ingin dikurangi: "))
                inventory.kurangi_stok(nama, jumlah)
            except ValueError as e:
                print(f"Error: {e}")
            except ProductNotAvailableError as e:
                print(f"Error: {e}")
        elif choice == '3':
            nama = input("Masukkan nama produk: ").strip()
            try:
                produk = inventory.cari_produk(nama)
                print(f"Produk ditemukan: {produk.nama} | Harga: Rp.{produk.harga:,.0f} | Stok: {produk.stok}")
            except ProductNotAvailableError as e:
                print(f"Error: {e}")
        elif choice == '4':
            inventory.lihat_gudang()
        elif choice == '5':
            nama = input("Masukkan nama produk: ").strip()
            try:
                harga_baru = float(input("Masukkan harga baru: Rp."))
                inventory.update_harga(nama, harga_baru)
            except ValueError:
                print("Harga harus berupa angka.")
            except ProductNotAvailableError as e:
                print(f"Error: {e}")
        elif choice == '6':
            nama = input("Masukkan nama produk: ").strip()
            try:
                stok_baru = int(input("Masukkan jumlah stok yang ditambahkan: "))
                inventory.update_stok(nama, stok_baru)
            except ValueError:
                print("Stok harus berupa angka bulat.")
            except ProductNotAvailableError as e:
                print(f"Error: {e}")
        else:
            print("Pilihan tidak valid.")


def menu_belanja(accounts, inventory):
    while True:
        print("\n╔══════════════════════════════════╗")
        print("║        SISTEM BELANJA            ║")
        print("╠══════════════════════════════════╣")
        print("║  1. Beli Produk                  ║")
        print("║  0. Kembali ke Menu Utama        ║")
        print("╚══════════════════════════════════╝")
        choice = input("Pilih menu: ")

        if choice == '0':
            break
        elif choice == '1':
            _proses_belanja(accounts, inventory)
        else:
            print("Pilihan tidak valid.")


def _proses_belanja(accounts, inventory):
    # 1. Pilih produk
    print("\n--- Langkah 1: Pilih Produk ---")
    produk_list = inventory.list_produk_untuk_belanja()
    if not produk_list:
        print("Tidak ada produk yang bisa dibeli.")
        return

    try:
        idx = int(input("Masukkan nomor produk: ")) - 1
        if idx < 0 or idx >= len(produk_list):
            print("Nomor produk tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    produk = produk_list[idx]
    print(f"Produk dipilih: {produk.nama} (Rp.{produk.harga:,.0f})")

    # 2. Pilih akun bank
    print("\n--- Langkah 2: Pilih Akun Bank ---")
    akun = _pilih_akun_aktif(accounts)
    if akun is None:
        return

    # 3. Pilih jumlah
    print("\n--- Langkah 3: Jumlah Pembelian ---")
    try:
        jumlah = int(input(f"Masukkan jumlah (maks stok: {produk.stok}): "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            return
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    total = jumlah * produk.harga

    # 4. Cek saldo cukup
    try:
        saldo = akun.get_balance()
    except AccountLockedError as e:
        print(f"Error: {e}")
        return

    if saldo < total:
        print(f"Saldo tidak cukup! Dibutuhkan: Rp.{total:,.0f} | Saldo: Rp.{saldo:,.0f}")
        return

    # 5. Pilih metode pembayaran
    print("\n--- Langkah 4: Pilih Metode Pembayaran ---")
    print("1. Kartu Kredit")
    print("2. Transfer Bank")
    print("3. E-Wallet")
    metode = input("Pilih metode pembayaran: ")

    try:
        if metode == '1':
            payment = CreditCard(
                nomor_kartu=input("Masukkan nomor kartu kredit: "),
                nama_pemilik=akun.get_account_holder(),
            )
        elif metode == '2':
            payment = BankTransfer(
                nomor_rekening=input("Masukkan nomor rekening: "),
                nama_bank=input("Masukkan nama bank: "),
            )
        elif metode == '3':
            payment = EWallet(
                nomor_akun=input("Masukkan nomor akun e-wallet: "),
                nama_akun=akun.get_account_holder(),
            )
        else:
            print("Metode pembayaran tidak valid.")
            return
    except DataTidakValidError as e:
        print(f"Error: {e}")
        return

    # 6. Konfirmasi
    print(f"\n--- Konfirmasi Pembelian ---")
    print(f"Produk     : {produk.nama}")
    print(f"Jumlah     : {jumlah}")
    print(f"HargaSatuan: Rp.{produk.harga:,.0f}")
    print(f"Total      : Rp.{total:,.0f}")
    print(f"Akun       : {akun.get_account_holder()}")
    print(f"Metode     : {payment.get_info()}")
    konfirmasi = input("Lanjutkan pembayaran? (y/n): ")

    if konfirmasi.lower() != 'y':
        print("Pembelian dibatalkan.")
        return

    # 7. Proses pembayaran (dari saldo akun bank)
    try:
        payment.proses_pembayaran(total, bank_account=akun)
        inventory.kurangi_stok(produk.nama, jumlah)
        print(f"\n✓ Pembelian berhasil!")
        print(f"  Sisa saldo: Rp.{akun.get_balance():,.0f}")
    except (DanaTidakCukup, DataTidakValidError, PembayaranGagalError) as e:
        print(f"Error saat memproses pembayaran: {e}")
    except ProductNotAvailableError as e:
        print(f"Error: {e}")


def _pilih_akun_aktif(accounts):
    """Helper: meminta user memilih akun aktif."""
    if not accounts:
        print("Belum ada akun. Silakan buat akun terlebih dahulu.")
        return None
    print("Akun tersedia:", ', '.join(accounts.keys()))
    nama = input("Masukkan nama pemilik akun: ").strip()
    akun = accounts.get(nama)
    if akun is None:
        print("Akun tidak ditemukan.")
        return None
    return akun


def main():
    """Menu utama program."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    # Muat data
    accounts = {
        acc.get_account_holder(): acc
        for acc in BankAccount.load_account_data()
    }
    inventory = Inventory()

    print("\n" + "=" * 50)
    print("  SELAMAT DATANG DI SISTEM TERPADU")
    print("  Bank  |  Inventaris  |  Pembayaran")
    print("=" * 50)

    while True:
        print("\n╔══════════════════════════════════╗")
        print("║         MENU UTAMA               ║")
        print("╠══════════════════════════════════╣")
        print("║  1. Kelola Akun Bank             ║")
        print("║  2. Kelola Inventaris            ║")
        print("║  3. Belanja (Beli Produk)        ║")
        print("║  4. Lihat Semua Data             ║")
        print("║  0. Keluar                       ║")
        print("╚══════════════════════════════════╝")
        choice = input("Pilih menu: ")

        if choice == '0':
            print("Terima kasih telah menggunakan Sistem Terpadu. Sampai jumpa!")
            break
        elif choice == '1':
            menu_akun_bank(accounts)
        elif choice == '2':
            menu_inventaris(inventory)
        elif choice == '3':
            menu_belanja(accounts, inventory)
        elif choice == '4':
            _lihat_semua_data(accounts, inventory)
        else:
            print("Pilihan tidak valid. Silakan pilih antara 0-4.")


def _lihat_semua_data(accounts, inventory):
    """Menampilkan ringkasan semua data."""
    print("\n" + "=" * 50)
    print("  RINGKASAN DATA")
    print("=" * 50)

    print("\n--- Akun Bank ---")
    if accounts:
        for nama, akun in accounts.items():
            try:
                print(f"  {nama}: Rp.{akun.get_balance():,.0f}")
            except AccountLockedError:
                print(f"  {nama}: [TERKUNCI]")
    else:
        print("  Tidak ada akun.")

    print("\n--- Inventaris ---")
    if inventory.products:
        for p in inventory.products:
            print(f"  {p.nama}: Rp.{p.harga:,.0f} (stok: {p.stok})")
    else:
        print("  Gudang kosong.")
    print("=" * 50)


if __name__ == '__main__':
    main()
