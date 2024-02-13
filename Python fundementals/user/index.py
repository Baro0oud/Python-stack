class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} has withdrawn ${amount}.")
        else:
            print(f"Insufficient funds. {self.name} cannot withdraw ${amount}.")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            print(f"${amount} has been transferred from {self.name} to {other_user.name}.")
        else:
            print(f"Insufficient funds. {self.name} cannot transfer ${amount}.")

# Example usage:
user1 = User("Guido van Rossum", 1000)
user2 = User("Linus Torvalds", 500)

user1.display_user_balance()  # User: Guido van Rossum, Balance: $1000
user2.display_user_balance()  # User: Linus Torvalds, Balance: $500

user1.make_withdrawal(200)  # Guido van Rossum has withdrawn $200.
user1.display_user_balance()  # User: Guido van Rossum, Balance: $800

user1.transfer_money(user2, 300)  # $300 has been transferred from Guido van Rossum to Linus Torvalds.
user1.display_user_balance()  # User: Guido van Rossum, Balance: $500
user2.display_user_balance()  # User: Linus Torvalds, Balance: $800
