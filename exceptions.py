class DanaTidakCukup(Exception):
    def __init__(self, message="Saldo Anda tidak cukup"):
        super().__init__(message)


class InvalidAmountError(Exception):
    def __init__(self, message="Jumlah yang dimasukkan tidak valid."):
        super().__init__(message)


class AccountLockedError(Exception):
    def __init__(self, message="Akun Anda terkunci."):
        super().__init__(message)


class ProductNotAvailableError(Exception):
    def __init__(self, message="Stok produk habis"):
        self.message = message
        super().__init__(self.message)


class PembayaranGagalError(Exception):
    def __init__(self, message="Pembayaran gagal. Silahkan coba lagi."):
        self.message = message
        super().__init__(self.message)


class DataTidakValidError(Exception):
    def __init__(self, message="Data Tidak Valid. Silahkan periksa kembali data yang dimasukkan."):
        self.message = message
        super().__init__(self.message)
