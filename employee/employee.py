class Employee:
    def __init__(self, nama, id, gaji):
        self.nama = nama
        self.id = id
        self.gaji = gaji
    
    def get_gaji(self):
        return self.gaji
    
    def get_info(self):
        print(f'Nama: {self.nama}')
        print(f'ID: {self.id}')
        print(f'Gaji: {self.gaji:,.0f}')
    
    def hitung_bonus(self):
        return self.gaji * 0.10
    
    def tampilkan_bonus(self):
        bonus = self.hitung_bonus()
        print(f'Bonus: {bonus:,.2f}')

class Manager(Employee):
    def __init__(self, nama, id, gaji, departemen, tim_size):
        super().__init__(nama, id, gaji)
        self.departemen = departemen
        self.tim_size = tim_size
    
    def get_info(self):
        super().get_info()
        print(f'Departemen: {self.departemen}')
        print(f'Jumlah anggota tim: {self.tim_size} orang')
    
    def hitung_bonus(self):
        return self.gaji * 0.20

class Developer(Employee):
    def __init__(self, nama, id, gaji, bahasa_prog, framework):
        super().__init__(nama, id, gaji)
        self.bahasa_prog = bahasa_prog
        self.framework = framework
    
    def get_info(self):
        super().get_info()
        print(f'Bahasa Pemrograman: {self.bahasa_prog}')
        print(f'Framework: {self.framework}')
    
    def hitung_bonus(self):
        return self.gaji * 0.15

if __name__ == "__main__":
    print()
    print('==================================')
    print("=== Program Manajemen Karyawan ===")
    print('==================================')
    
    print()
    print()
    
    print('1. Manager')
    print('----------------------------------')
    mgr = Manager('Ryan', 'MGR007', 15000000, 'IT', 5)
    mgr.get_info()
    print('----------------------------------')
    
    print()
    
    print('2. Developer 1')
    print('----------------------------------')
    dev = Developer('Ainul', 'DEV001', 5000000, 'Python', 'Django')
    dev.get_info()
    print('----------------------------------')
    
    print()
    
    print('3. Developer 2')
    print('----------------------------------')
    dev2 = Developer('Rizky', 'DEV002', 6000000, 'JavaScript', 'React')
    dev2.get_info()
    print('----------------------------------')
    
    print()
    
    employees = [mgr, dev, dev2]
    
    print('================================== ')
    print('= Perhitungan Bonus Tiap Karyawan =')
    print('================================== ')
    
    for emp in employees:
        bonus  = emp.hitung_bonus()
        print(f'{emp.nama:15} {emp.id:10}: {bonus:,.2f}')
    
    print('================================== ')
    print('Statistik')
    total_bonus = sum(emp.hitung_bonus() for emp in employees)
    print(f'Total Bonus: {total_bonus:,.2f}')
    max_bonus = max(emp.hitung_bonus() for emp in employees)
    print(f'Bonus Terbesar: {max_bonus:,.2f}')

