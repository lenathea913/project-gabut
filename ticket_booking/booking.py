from exception import SeatUnavailableError, InvalidBookingError, PaymentFailedError

class Booking:
    kursi_tersedia = list(range(1, 11))
    
    def __init__(self, nama, nomor_kursi, harga):
        if not nama or len(nama.strip()) == 0:
            raise InvalidBookingError('Nama tidak boleh kosong.')
        if nomor_kursi not in self.kursi_tersedia:
            raise SeatUnavailableError('Kursi tidak tersedia.')
        if harga <= 0:
            raise ValueError('Harga tidak boleh negatif.')
        
        self.nama = nama
        self.nomor_kursi = nomor_kursi
        self.harga = harga
        self.status = 'Pending'
    
    def proses_pembayaran(self, jumlah_bayar):
        if jumlah_bayar < self.harga:
            raise PaymentFailedError('Jumlah pembayaran tidak mencukupi.')
        self.status = 'Lunas'
        print(f'Pembayaran berhasil. Status booking: {self.status}')
    
    def konfirmasi_pembayaran(self):
        if self.status != 'Lunas':
            raise PaymentFailedError('Pembayaran belum dilakukan.')
        self.kursi_tersedia.remove(self.nomor_kursi)
    
    def tampilkan_info(self):
        print()
        print('===================')
        print('Informasi Booking:')
        print('===================')
        print(f'Nama: {self.nama}')
        print(f'Nomor Kursi: {self.nomor_kursi}')
        print(f'Harga: {self.harga}')
        print(f'Status: {self.status}')
    
    