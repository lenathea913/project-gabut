class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
    
    def hitung_gaji(self):
        return self.gaji_pokok
    
    def info(self):
        print(f"{self.nama} mendapatkan gaji {self.hitung_gaji()}")

class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan
    
    def hitung_gaji(self):
        total = self.gaji_pokok + self.tunjangan_jabatan
        return total
    
class SalesPerson(Karyawan):
    def __init__(self, nama, gaji_pokok, komisi_penjualan):
        super().__init__(nama, gaji_pokok)
        self.komisi_penjualan = komisi_penjualan
    
    def hitung_gaji(self):
        gaji = self.gaji_pokok + self.komisi_penjualan
        return gaji
    
ainul = Karyawan("Ainul", 3000000)
ryan = Manager("Ryan", 10000000, 2000000)
rachel = Manager("Rachel", 10000000, 1500000)
hafis = SalesPerson("Hafis", 2500000, 500000)

ainul.info()
ryan.info()
rachel.info()
hafis.info()