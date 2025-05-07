from account import Account
from atm import ATM
from exceptions import (
    InvalidPINException,
    InsufficientFundsException,
    InsufficientATMCashException,
    DailyLimitExceededException,
    ServerConnectionException
)

def main():
    account = Account(balance=5000, daily_limit=2000, pin="1234")
    atm = ATM(cash_reserve=10000)

    while True:
        print("\n--- ATM Machine ---")
        try:
            pin = input("Enter PIN: ")
            account.validate_pin(pin)
            amount = int(input("Enter withdrawal amount: ₹"))
            atm.withdraw_cash(account, amount)
            print(f"Remaining balance: ₹{account.balance}")
        except (InvalidPINException, InsufficientFundsException, 
                InsufficientATMCashException, DailyLimitExceededException, 
                ServerConnectionException) as exception:
            print(f"Error: {str(exception)}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        finally:
            if account.is_blocked:
                print("Your card is blocked. Exiting.")
                break
            continue_choice = input("Do you want to continue? (yes/no): ").lower()
            if continue_choice != 'yes':
                print("Thank you for using the ATM.")
                break

if __name__ == "__main__":
    main()
