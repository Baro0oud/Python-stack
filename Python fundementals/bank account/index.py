class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into the account.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from the account.")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            print(f"Interest of ${interest} added to the account.")

# Example usage:
account1 = BankAccount(0.05, 1000)
account1.display_account_info()  # Balance: $1000

account1.deposit(500)  # Deposited $500 into the account.
account1.display_account_info()  # Balance: $1500

account1.withdraw(200)  # Withdrew $200 from the account.
account1.display_account_info()  # Balance: $1300

account1.yield_interest()  # Interest of $65.0 added to the account.
account1.display_account_info()  # Balance: $1365.0
