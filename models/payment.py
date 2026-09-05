from abc import ABC, abstractmethod
from exceptions import (
    PembayaranGagalError,
    DataTidakValidError,
    InvalidAmountError,
)


class Payment(ABC):
    @abstractmethod
    def proses_pembayaran(self, jumlah, bank_account=None):
        pass

    @abstractmethod
    def get_info(self):
        pass


class CreditCard(Payment):
    def __init__(self, nomor_kartu, nama_pemilik):
        self.nomor_kartu = nomor_kartu
        self.nama_pemilik = nama_pemilik

    def proses_pembayaran(self, jumlah, bank_account=None):
        if jumlah <= 0:
            raise InvalidAmountError("Jumlah pembayaran harus lebih dari 0.")
        if not self.nomor_kartu or not self.nama_pemilik:
            raise DataTidakValidError("Data kartu kredit tidak valid.")
        if bank_account is not None:
            bank_account.withdraw(jumlah)
        print(f"Pembayaran via Kartu Kredit sebesar Rp.{jumlah:,.0f} berhasil!")

    def get_info(self):
        masked = self.nomor_kartu[-4:] if self.nomor_kartu else "****"
        return f"Kartu Kredit (****{masked}) - {self.nama_pemilik}"


class BankTransfer(Payment):
    def __init__(self, nomor_rekening, nama_bank):
        self.nomor_rekening = nomor_rekening
        self.nama_bank = nama_bank

    def proses_pembayaran(self, jumlah, bank_account=None):
        if jumlah <= 0:
            raise InvalidAmountError("Jumlah pembayaran harus lebih dari 0.")
        if not self.nomor_rekening or not self.nama_bank:
            raise DataTidakValidError("Data transfer bank tidak valid.")
        if bank_account is not None:
            bank_account.withdraw(jumlah)
        print(f"Pembayaran via Transfer Bank ({self.nama_bank}) sebesar Rp.{jumlah:,.0f} berhasil!")

    def get_info(self):
        return f"Transfer Bank - {self.nama_bank} (Rek: {self.nomor_rekening})"


class EWallet(Payment):
    def __init__(self, nomor_akun, nama_akun):
        self.nomor_akun = nomor_akun
        self.nama_akun = nama_akun

    def proses_pembayaran(self, jumlah, bank_account=None):
        if jumlah <= 0:
            raise InvalidAmountError("Jumlah pembayaran harus lebih dari 0.")
        if not self.nomor_akun or not self.nama_akun:
            raise DataTidakValidError("Data e-wallet tidak valid.")
        if bank_account is not None:
            bank_account.withdraw(jumlah)
        print(f"Pembayaran via E-Wallet ({self.nama_akun}) sebesar Rp.{jumlah:,.0f} berhasil!")

    def get_info(self):
        return f"E-Wallet - {self.nama_akun} (ID: {self.nomor_akun})"
