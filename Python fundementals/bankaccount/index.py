class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

# Create two accounts
account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.01)

# Test deposit, withdraw, display_account_info, and yield_interest methods
account1.deposit(500).deposit(100).withdraw(300).yield_interest().display_account_info()
account2.deposit(2000).withdraw(500).withdraw(1000).yield_interest().display_account_info()
