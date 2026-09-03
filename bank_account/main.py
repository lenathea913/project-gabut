from bank_account.bank_account import (
    AccountLockedError,
    BankAccount,
    DanaTidakCukup,
    InvalidAmountError,
)

if __name__ == '__main__':
    accounts = {
        account.get_account_holder(): account
        for account in BankAccount.load_account_data()
    }
    account = None

    while True:
        print('=== Sistem Bank ===')
        print('1. Buat Akun')
        print('2. Cek Saldo')
        print('3. Setor Dana')
        print('4. Tarik Dana')
        print('5. Transfer Dana')
        print('6. Kunci Akun')
        print('7. Buka Kunci Akun')
        print('8. Lihat Riwayat Transaksi')
        print('9. Pilih Akun Aktif')
        choice = input('Pilih menu (1-9) q to quit: ')
        
        if choice.lower() == 'q':
            print('Terima kasih telah menggunakan sistem bank.')
            break

        if choice == '1':
            account_holder = input('Masukkan nama pemilik akun: ')
            if account_holder in accounts:
                print('Akun dengan nama tersebut sudah ada.')
                continue
            try:
                initial_balance = float(input('Masukkan saldo awal: '))
                account = BankAccount(account_holder, initial_balance)
                account.save_account_data()
                accounts[account_holder] = account
                print(f'Akun bank untuk {account_holder} berhasil dibuat.')
            except ValueError:
                print('Saldo awal harus berupa angka yang valid.')
            continue

        if choice == '9':
            if not accounts:
                print('Belum ada akun yang tersedia.')
                continue
            print('Akun tersedia:', ', '.join(accounts))
            account_holder = input('Masukkan nama pemilik akun: ')
            account = accounts.get(account_holder)
            if account is None:
                print('Akun tidak ditemukan.')
            else:
                print(f'Akun aktif: {account_holder}')
            continue

        if account is None:
            print('Buat atau pilih akun terlebih dahulu melalui menu 1.')
            continue
        
        if choice == '2':
            try:
                print(f'Saldo saat ini: Rp.{account.get_balance()}')
            except AccountLockedError:
                print('Akun terkunci. Tidak dapat menampilkan saldo.')
        
        elif choice == '3':
            try:
                amount = float(input('Masukkan jumlah setoran: '))
                account.deposit(amount)
                print(f'Saldo saat ini: Rp.{account.get_balance()}')
            except ValueError:
                print('Jumlah setoran harus berupa angka yang valid.')
            except AccountLockedError:
                print('akun terkunci. Tidak dapat melakukan setoran.')
            except InvalidAmountError:
                print('Jumlah setoran tidak valid.')
            
        elif choice == '4':
            try:
                amount = float(input('Masukkan jumlah penarikan: '))
                account.withdraw(amount)
                print(f'Saldo Saat ini: Rp.{account.get_balance()}')
            except ValueError:
                print('Jumlah penarikan harus berupa angka yang valid.')
            except AccountLockedError:
                print('akun terkunci. Tidak dapat melakukan penarikan.')
            except InvalidAmountError:
                print('Jumlah penarikan tidak valid.')  
            except DanaTidakCukup:
                print('Dana tidak cukup untuk melakukan penarikan.')
            
        elif choice == '5':
            try:
                amount = float(input('Masukkan jumlah transfer: '))
                target_account_holder = input('Masukkan nama pemilik akun tujuan: ')
                target_account = accounts.get(target_account_holder)
                if target_account is None:
                    print('Akun tujuan tidak ditemukan.')
                    continue
                account.transfer(amount, target_account)
                print(f'Transfer berhasil dilakukan.')
            except ValueError:
                print('Jumlah transfer harus berupa angka yang valid.')
            except AccountLockedError:
                print('akun terkunci. Tidak dapat melakukan transfer.') 
            except InvalidAmountError:
                print('Jumlah transfer tidak valid.')
            except DanaTidakCukup:
                print('Dana tidak cukup untuk melakukan transfer.')
            
        elif choice == '6':
            try:
                account.lock_account()
                print('Akun telah dikunci.')
            except AccountLockedError:
                print('Akun sudah terkunci.')
            
        elif choice == '7':
            account.unlock_account()
            print('Akun telah dibuka.')
        elif choice == '8':
            try:
                account.print_transaction_history()
            except AccountLockedError:
                print('akun terkunci. Tidak dapat menampilkan riwayat transaksi.')

        else:
            print('Pilihan tidak valid. Silakan pilih menu yang tersedia.')