from booking import Booking
from exception import SeatUnavailableError, InvalidBookingError, PaymentFailedError

def main():
    while True:
        print()
        print('==================================')
        print("=== Program Pemesanan Tiket ===")
        print('==================================')
        print('1. Buat Pemesanan')
        print('2. Proses Pembayaran')
        print('3. Konfirmasi Pembayaran')
        print('4. Tampilkan Informasi Booking')
        
        user = input('Masukkan pilihan (q to quit): ').lower()
        
        if user == '1':
            try:
                nama = input('Masukkan nama pemesan: ').lower()
                nomor_kursi = int(input('masukkan nomor kursi (1-10): '))
                harga = float(input('Masukkan harga tiket: '))
                booking = Booking(nama, nomor_kursi, harga)
                print('Pemesanan berhasil dibuat.')
            except (SeatUnavailableError, InvalidBookingError, ValueError) as e:
                print(e)
        
        elif user == '2':
            if 'booking' not in locals():
                print()
                print('Belum ada pemesanan yang dibuat.')
                continue
            try:
                jumlah_bayar = float(input('Masukkan jumlah pembayaran: '))
                booking.proses_pembayaran(jumlah_bayar)
            except PaymentFailedError as e:
                print(e)
            except ValueError as e:
                print(f'Jumlah pembayaran tidak valid: {e}')
        
        elif user == '3':
            if 'booking' not in locals():
                print()
                print('Belum ada pemesanan yang dibuat.')
                continue
            try:
                booking.konfirmasi_pembayaran()
                print()
                print('Pembayaran berhasil dikonfirmasi.')
            except PaymentFailedError as e:
                print(e)
        
        elif user == '4':
            if 'booking' not in locals():
                print()
                print('Belum ada pemesanan yang dibuat.')
                continue
            booking.tampilkan_info()
        
        elif user == 'q':
            print()
            print('Terima kasih telah menggunakan program ini.')
            print('==================================')
            break
        
        else:
            print('Pilihan tidak valid. Silakan coba lagi.')

if __name__ == '__main__':
    main()