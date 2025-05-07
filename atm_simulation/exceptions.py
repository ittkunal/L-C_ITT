class InsufficientFundsException(Exception):
    pass

class InsufficientATMCashException(Exception):
    pass

class InvalidPINException(Exception):
    pass

class DailyLimitExceededException(Exception):
    pass

class ServerConnectionException(Exception):
    pass
