class SeatUnavailableError(Exception):
    def __init__(self, message='Kursi tidak tersedia'):
        self.message = message
        super().__init__(self.message)

class InvalidBookingError(Exception):
    def __init__(self, message='Pememsanan tidak valid'):
        self.message = message
        super().__init__(self.message)

class PaymentFailedError(Exception):
    def __init__(self, message='Pembayaran Gagal'):
        self.message = message
        super().__init__(self.message)
