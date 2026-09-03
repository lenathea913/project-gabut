from rekening import rekeningBank
from exception import JumlahTidakValidError, SaldoTidakCukupError

def main():
    rek = rekeningBank("123-456", "Budi", saldo_awal=1000000)
    
    try:
        rek.deposit(100000)
        print(f"Saldo saat ini: Rp.{rek._saldo:,.2f}")
        
        rek.withdraw("seratus ribu")
    except SaldoTidakCukupError as e:
        print(f"[ERROR]: {e}")
    except JumlahTidakValidError as e:
        print(f"[ERROR]: {e}")
        
if __name__ == "__main__":
    main()