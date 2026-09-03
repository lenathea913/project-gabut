class saldoTidakCukupError(Exception):
    pass

class JumlahTidakValidError(Exception):
    pass

class RekeningBank:
    
    def __init__(self, nomor_rekening: str, nama_pemilik: str, saldo_awal: float = 0.0, saldo_minimal:float = 50000.0):
        if not isinstance(nomor_rekening, str) or not nomor_rekening.strip():
            raise ValueError("Nomor rekening harus berupa string dan tidak boleh kosong")
        
        if not isinstance(nama_pemilik, str) or not nama_pemilik.strip():
            raise ValueError("Nama Pemilik Harus berupa string dan tidak boleh kosong")
        
        if not isinstance(saldo_awal, (int, float)) or saldo_awal < 0:
            raise ValueError("Saldo awal harus berupa angka dan non negatif")
        
        if not isinstance(saldo_minimal, (int,float)) or saldo_minimal < 0:
            raise ValueError("Saldo minimal tidak boleh kosong dan non negatif")
        
        self.nomor_rekening = nomor_rekening.strip()
        self.nama_pemilik = nama_pemilik.strip()
        self._saldo = float(saldo_awal)
        self.saldo_minimal = float(saldo_minimal)
        
    @property
    def saldo(self) -> float:
        return self._saldo
    
    def _validasi_jumlah(self, jumlah: float, jenis_transaksi:str):
        if not isinstance(jumlah, (int, float)) or isinstance(jumlah, bool):
            raise JumlahTidakValidError(f"Jumlah {jenis_transaksi} harus berupa angka")
        if jumlah <= 0:
            raise JumlahTidakValidError(f"Jumlah {jenis_transaksi} harus lebih besar dari 0")
    
    def deposit(self, jumlah:float) -> float:
        self._validasi_jumlah(jumlah, "deposit")
        self._saldo += float(jumlah)
        print(f"[SUKSES] Deposit: Rp.{jumlah:.2f} berhasil. Saldo saat ini: Rp.{self._saldo:.2f}")
        return self._saldo
    
    def withdraw(self, jumlah:float) -> float:
        self._validasi_jumlah(jumlah, "penarikan")
        
        sisa_saldo = self._saldo - jumlah
        if sisa_saldo < self.saldo_minimal:
            raise saldoTidakCukupError(
                f"Penarikan Saldo: Rp.{jumlah:,.2f} gagal "
                f"Saldo saat ini Rp.{self._saldo:,.2f} tidak menyukupi untuk menyisakan saldo minimal: Rp.{self.saldo_minimal:,.2f}"
            )
        self._saldo -= float(jumlah)
        print(f"[SUKSES] Penarikan Saldo: {jumlah:,.2f} berhasil. Sisa saldo: Rp.{self._saldo:,.2f}")
        return self._saldo
    
    def info_rekening(self) -> str:
        return (
            f"\n=== INFORMASI REKENING ===\n"
            f"Nomor Rekening = {self.nomor_rekening}\n"
            f"Nama Pemilik = {self.nama_pemilik}\n"
            f"Saldo = {self._saldo:,.2f}\n"
            f"Saldo Minimal = {self.saldo_minimal:,.2f}\n"
            f"==========================="
        )
    
    def __str__(self) -> str:
        return f"RekeningBank({self.nomor_rekening} - {self.nama_pemilik} : Rp.{self._saldo:,.2f})"
    
if __name__ == "__main__":
    print("--- 1. Inisiasi Rekening ---")
    rek = RekeningBank(nomor_rekening="123-456-789", nama_pemilik="Ainul Yakhin", saldo_awal=500000, saldo_minimal=50000)
    print(rek.info_rekening())
    
    print("\n--- 2. Transaksi Normal(Deposit & Withdraw) ---")
    try:
        rek.deposit(200000)
        rek.withdraw(150000)
    except Exception as e:
        print(f"[ERROR]: {e}")
    
    print("\n--- 3. Error Handling: Depost jumlah negatif ---")
    try:
        rek.deposit(-50000)
    except JumlahTidakValidError as e:
        print(f"[ERROR] : {e}")
    
    print("\n--- 4. Error Handling: Penarikan Melebihi saldo minimal ---")
    try:
        rek.withdraw(520000)
    except saldoTidakCukupError as e:
        print(f"[ERROR]: {e}")
    
    print("\n--- 5. Error Handling: Tipe data tidak aktif ---")
    try:
        rek.deposit("seratus ribu")
    except JumlahTidakValidError as e:
        print(f"[ERROR]: {e}")
    
    print("\n--- 6. Status Akhir ---")
    print(rek.info_rekening())