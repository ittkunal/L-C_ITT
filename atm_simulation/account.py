from exceptions import InsufficientFundsException, InvalidPINException, DailyLimitExceededException

class Account:
    def __init__(self, balance, daily_limit, pin):
        self.balance = balance
        self.daily_limit = daily_limit
        self.pin = pin
        self.invalid_pin_attempts = 0
        self.daily_withdrawn = 0
        self.is_blocked = False

    def validate_pin(self, entered_pin):
        if self.is_blocked:
            raise InvalidPINException("Card is blocked due to multiple invalid PIN attempts.")
        if entered_pin != self.pin:
            self._handle_invalid_pin()
        else:
            self.invalid_pin_attempts = 0

    def withdraw(self, amount):
        self._check_balance(amount)
        self._check_daily_limit(amount)
        self.balance -= amount
        self.daily_withdrawn += amount

    def _handle_invalid_pin(self):
        self.invalid_pin_attempts += 1
        if self.invalid_pin_attempts >= 3:
            self.is_blocked = True
            raise InvalidPINException("Card is now blocked after 3 invalid PIN attempts.")
        raise InvalidPINException("Invalid PIN. Please try again.")

    def _check_balance(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds in account.")

    def _check_daily_limit(self, amount):
        if self.daily_withdrawn + amount > self.daily_limit:
            raise DailyLimitExceededException("Daily withdrawal limit exceeded.")
