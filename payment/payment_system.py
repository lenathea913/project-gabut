from abc import ABC, abstractmethod
from .exception import PembayaranGagalError, DataTidakValidError

class Payment(ABC):
    @abstractmethod
    def proses_pembayaran(self, jumlah):
        pass

class CreditCard(Payment):
    def __init__(self, nomor_kartu, nama_pemilik):
        self.nomor_kartu = nomor_kartu
        self.nama_pemilik = nama_pemilik
    
    def proses_pembayaran(self, jumlah):
        if not self.nomor_kartu or not self.nama_pemilik:
            raise DataTidakValidError("Data kartu kredit tidak valid")
        return print(f'Pembayaran sebesar {jumlah:,.0f} berhasil!.')

class BankTransfer(Payment):
    def __init__(self, nomor_rekening, nama_bank):
        self.nomor_rekening = nomor_rekening
        self.nama_bank = nama_bank
    
    def proses_pembayaran(self, jumlah):
        if not self.nomor_rekening or not self.nama_bank:
            raise DataTidakValidError("Data transfer bank tidak valid")
        return print(f'Pembayaran sebesar Rp.{jumlah:,.0f} Berhasil!.')

class EWallet(Payment):
    def __init__(self, nomor_akun, nama_akun):
        self.nomor_akun = nomor_akun
        self.nama_akun = nama_akun
    
    def proses_pembayaran(self, jumlah):
        if not self.nomor_akun or not self.nama_akun:
            raise DataTidakValidError("Data e-wallet tidak valid")
        return print(f'Pembayaran sebesar Rp.{jumlah:,.0f} Berhasil!.')
    

if __name__ == "__main__":
    print()
    print('==================================')
    print("=== Program Sistem Pembayaran ===")
    print('==================================')
    
    print()
    print()
    
    print('1. Credit Card')
    print('----------------------------------')
    kredit = CreditCard("1234-5678-9012-3456", "John Doe")
    try:
        kredit.proses_pembayaran(100000)
    except DataTidakValidError as e:
        print(f"[ERROR]: {e}")
    
    print()
    print()
    
    print('2. Bank Transfer')
    print('----------------------------------')
    transfer = BankTransfer("9876543210", "Bank ABC")
    try:
        transfer.proses_pembayaran(200000)
    except DataTidakValidError as e:
        print(f"[ERROR]: {e}")
    
    print()
    print()
    
    print('3. E-Wallet')
    print('----------------------------------')
    ewallet = EWallet("ewallet123", "Jane Doe")
    try:
        ewallet.proses_pembayaran(150000)
    except DataTidakValidError as e:
        print(f"[ERROR]: {e}")
    
    print('Error Handling Demonstration')
    print('----------------------------------')
    # Mencoba proses pembayaran dengan data yang tidak valid
    kredit_invalid = CreditCard("", "John Doe")
    try:
        kredit_invalid.proses_pembayaran(100000)
    except DataTidakValidError as e:
        print(f"[ERROR]: {e}")
    
    
