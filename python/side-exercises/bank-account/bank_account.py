import threading


class BankAccount(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        if self.is_open:
            with self.lock:
                return self.balance
        else:
            raise ValueError('account is not open')

    def open(self):
        if not self.is_open:
            with self.lock:
                self.is_open = True

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('can not deposit negative value')
        if self.is_open:
            with self.lock:
                self.balance += amount
        else:
            raise ValueError('can not deposit to closed account')

    def withdraw(self, amount):
        if amount > self.balance or amount < 0:
            raise ValueError('can not withdraw more than balance')

        if self.is_open:
            with self.lock:
                self.balance -= amount

    def close(self):
        if self.is_open:
            with self.lock:
                self.is_open = False
