class PembayaranGagalError(Exception):
    def __init__(self, message='Pembayaran gagal. Silahkan coba lagi.'):
        self.message = message
        super().__init__(self.message)

class DataTidakValidError(Exception):
    def __init__(self, message='Data Tidak Valid. Silahkan Periksa kembali data yang dimasukkan.'):
        self.message = message
        super().__init__(self.message)