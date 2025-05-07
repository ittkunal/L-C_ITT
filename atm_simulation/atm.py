from exceptions import InsufficientATMCashException, ServerConnectionException
from utils import is_server_connected

class ATM:
    def __init__(self, cash_reserve):
        self.cash_reserve = cash_reserve

    def withdraw_cash(self, account, amount):
        if not is_server_connected():
            raise ServerConnectionException("Unable to connect with server.")
        if amount > self.cash_reserve:
            raise InsufficientATMCashException("Insufficient cash in ATM.")
        account.withdraw(amount)
        self.cash_reserve -= amount
        print(f"Withdrawal successful. Please collect your cash: ₹{amount}")
