class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(
            f"\n{amount} has been added to {self.name}'s account\nNow actual balance is {self.balance}"
        )

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(
                f"{amount} has been withdrawn from {self.name}'s account\nNow actual balance is {self.balance}"
            )

    def display_balance(self):
        print(f"\nName: {self.name}")
        print(f"Balance: {self.balance}")


a1 = BankAccount("Ram")
a1.deposit(1000)
a1.withdraw(1100)
a1.display_balance()

a2 = BankAccount("Hari", 5000)
a2.deposit(1000)
a2.withdraw(5000)
a2.display_balance()
