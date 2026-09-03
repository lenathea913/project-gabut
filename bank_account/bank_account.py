import json
import os
class DanaTidakCukup(Exception):
    def __init__(self, message="Saldo Anda tidak cukup"):
        super().__init__(message)

class InvalidAmountError(Exception):
    def __init__(self, message='Jumlah yang dimasukkan tidak valid.'):
        super().__init__(message)

class AccountLockedError(Exception):
    def __init__(self, message='Akun anda terkunci.'):
        super().__init__(message)

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        if initial_balance < 0:
            raise InvalidAmountError('Saldo awal tidak boleh negatif.')
        self.account_holder = account_holder
        self._balance = initial_balance
        self._is_locked = False
        self._account_history = []
        self.bank_file = os.path.join(os.path.dirname(__file__), 'bank_accounts.json')
        
    def to_dict(self):
        return {
            'account_holder': self.account_holder,
            'balance': self._balance,
            'is_locked': self._is_locked,
            'account_history': self._account_history
        }

    @classmethod
    def load_account_data(cls, bank_file=None):
        if bank_file is None:
            bank_file = os.path.join(os.path.dirname(__file__), 'bank_accounts.json')
        if not os.path.exists(bank_file):
            return []

        try:
            with open(bank_file, 'r') as file:
                accounts_data = json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError('Format file bank_accounts.json tidak valid.') from error

        accounts = []
        for account_data in accounts_data:
            account = cls(
                account_holder=account_data['account_holder'],
                initial_balance=account_data.get('balance', 0)
            )
            account._is_locked = account_data.get('is_locked', False)
            account._account_history = account_data.get('account_history', [])
            accounts.append(account)
        return accounts
    
    def save_account_data(self):
        accounts_data = []
        if os.path.exists(self.bank_file):
            try:
                with open(self.bank_file, 'r') as file:
                    accounts_data = json.load(file)
            except json.JSONDecodeError as error:
                raise ValueError('Format file bank_accounts.json tidak valid.') from error

        account_data = self.to_dict()
        for index, saved_account in enumerate(accounts_data):
            if saved_account.get('account_holder') == self.account_holder:
                accounts_data[index] = account_data
                break
        else:
            accounts_data.append(account_data)

        with open(self.bank_file, 'w') as file:
            json.dump(accounts_data, file, indent=2)
    
    def get_balance(self):
        if self._is_locked:
            raise AccountLockedError()
        return self._balance
    
    def get_account_holder(self):
        return self.account_holder
    
    def get_account_info(self):
        if self._is_locked:
            raise AccountLockedError()
        return{
            'account_holder': self.account_holder,
            'balance': self._balance,
            'is_locked': self._is_locked,
            'transaksi': self._account_history
        }
    
    def deposit(self, amount):
        if self._is_locked:
            raise AccountLockedError()
        if amount <= 0:
            raise InvalidAmountError()
        self._balance += amount
        self._account_history.append(f'Deposit: Rp.{amount}')
        self.save_account_data()
    
    def withdraw(self, amount):
        if self._is_locked:
            raise AccountLockedError()
        if amount <= 0:
            raise InvalidAmountError()
        if amount > self._balance:
            raise DanaTidakCukup()
        self._balance -= amount
        self._account_history.append(f'Penarikan: Rp.{amount}')
        self.save_account_data()

    def transfer(self, amount, target_account):
        if self._is_locked:
            raise AccountLockedError()
        if amount <= 0:
            raise InvalidAmountError()
        if amount > self._balance:
            raise DanaTidakCukup()
        if not isinstance(target_account, BankAccount):
            raise TypeError('Akun tujuan harus berupa object BankAccount.')
        if target_account._is_locked:
            raise AccountLockedError('Akun tujuan terkunci.')
        self._balance -= amount
        target_account.deposit(amount)
        self._account_history.append(f'Transfer: Rp.{amount} ke {target_account.get_account_holder()}')
        self.save_account_data()

    def lock_account(self):
        self._is_locked = True
        self._account_history.append('Akun terkunci.')
        self.save_account_data()

    def unlock_account(self):
        self._is_locked = False
        self._account_history.append('Akun dibuka.')
        self.save_account_data()

    def get_transaction_history(self):
        if self._is_locked:
            raise AccountLockedError()
        return self._account_history
    
    def print_transaction_history(self):
        if self._is_locked:
            raise AccountLockedError()
        print(f'Riwayat Transaksi {self.account_holder}:')
        print('-------------------------')
        if not self._account_history:
            print('Tidak ada riwayat Transaksi.')
        else:
            for i, transaksi in enumerate(self._account_history, start=1):
                print(f'{i}. {transaksi}')
        print('-------------------------')
    

            