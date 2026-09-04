class ProductNotAvailableError(Exception):
    def __init__(self, message='Stok produk habis'):
        self.message = message
        super().__init__(self.message)
    