from exception import JumlahTidakValidError, SaldoTidakCukupError

class rekeningBank:
    def __init__(self, nomor_rekening:str, nama_pemilik:str, saldo_awal:float = 0.0, saldo_minimal:float = 500000.0):
        self.nomor_rekening = nomor_rekening.strip()
        self.nama_pemikin = nama_pemilik.strip()
        self._saldo = float(saldo_awal)
        self.saldo_minimal = float(saldo_minimal)
        
    @property
    def saldo(self) -> float:
        return self._saldo
    
    def _validasi_jumlah(self, jumlah:float, jenis_transaksi:str):
        if not isinstance(jumlah, (int, float)) or isinstance(jumlah, bool):
            raise JumlahTidakValidError(f"Jumlah {jenis_transaksi} harus berupa angka")
        if jumlah <= 0:
            raise JumlahTidakValidError(f"Jumlah {jenis_transaksi} harus lebih besar dari nol")
        
    def deposit(self, jumlah:float) -> float:
        self._validasi_jumlah(jumlah, "deposit")
        self._saldo += float(jumlah)
        print(f"[SUKSES] Deposit Rp.{jumlah}")
        return self._saldo
    
    def withdraw(self, jumlah:float) ->float:
        self._validasi_jumlah(jumlah, "penarikan")
        sisa_saldo = self._saldo - jumlah
        if sisa_saldo < self.saldo_minimal:
            raise SaldoTidakCukupError("Saldo tidak menyukupi untuk saldo minimum")
        self._saldo -= float(jumlah)
        return self._saldo