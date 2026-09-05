class SensorError(Exception):
    def __init__(self, message='Sensor error.'):
        self.message = message
        super().__init__(self.message)

class SensorReadError(SensorError):
    '''Raised ketika terjadi kesalahan saat membaca data dari sensor.'''
    def __init__(self, message='Gagal membaca data dari sensor.'):
        self.message = message
        super().__init__(self.message)

class SensorOutOfRangeError(SensorError):
    '''Raised ketika suhu sensor berada di luar batas yang ditentukan.'''
    def __init__(self, message='Sensor out of range.'):
        self.message = message
        super().__init__(self.message)