import threading
import functools


class BankAccount:
    def check_open(err_msg):
        def decorator_is_open(func):
            @functools.wraps(func)
            def wrapper_is_open(self, *args, **kwargs):
                if self.is_open:
                    value = func(self, *args, **kwargs)
                else:
                    raise ValueError(err_msg)
                return value
            return wrapper_is_open
        return decorator_is_open

    def decorator_lock(func):
        @functools.wraps(func)
        def wrapper_lock(self, *args, **kwargs):
            with self.lock:
                value = func(self, *args, **kwargs)
            return value
        return wrapper_lock

    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0
        self.is_open = False

    @check_open(err_msg='Account is not Open')
    def get_balance(self):
        return self.balance

    @check_open(err_msg='Account is not Open')
    @decorator_lock
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('can not deposit negative value')
        self.balance += amount

    @check_open(err_msg='Account is not Open')
    @decorator_lock
    def withdraw(self, amount):
        if amount > self.balance or amount < 0:
            raise ValueError('can not withdraw more than balance')
        self.balance -= amount

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False
