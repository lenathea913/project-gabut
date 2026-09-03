class BookNotFoundError(Exception):
    def __init__(self, message="Buku tidak ditemukan."):
        super().__init__(message)


class BukuSudahDipinjam(Exception):
    def __init__(self, message="Buku sudah dipinjam."):
        super().__init__(message)