class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    # @balance.setter
    def deposit(self, amount):
        self.__balance += amount

    # @balance.setter
    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            return self.__balance

    def check_balance(self):
        return self.__balance


b1 = BankAccount()
b1.deposit(1000)
print(b1.check_balance())
b1.withdraw(500)
print(b1.check_balance())
