class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        
    def rata_rata(self):
        total = sum(self.nilai)
        jumlah = len(self.nilai)
        return total / jumlah
    
    def status_kelulusan(self):
        if self.rata_rata() >= 60:
            return "Lulus"
        else:
            return "Tidak Lulus"
        
    def info(self):
        print(f"{self.nama} punya rata rata nilai {self.rata_rata()} dan berstatus {self.status_kelulusan()}")
    

rachel = Mahasiswa("Rachel", [80, 82, 83, 79, 78])
abigail = Mahasiswa("Abigail", [78, 89, 87, 76, 93])
intan = Mahasiswa("Intan", [76, 89, 79, 69, 67])
ainul = Mahasiswa("Ainul", [65, 54, 75, 55, 45])



rachel.info()
abigail.info()
intan.info()
ainul.info()