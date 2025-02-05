from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class BankAccount(Bank):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance} 💰")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance} 💸")

class SavingsAccount(BankAccount):
    def __init__(self, balance,min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
        print(f"New Savings Account created with balance {self.balance} 💰")
        print(f"Minimum balance limit is {self.min_balance} 💸")

    def withdraw(self, amount):
        if self.check_balance():
            super().withdraw(amount)

    def check_balance(self):
        if self.balance < self.min_balance:
            print("Balance is below minimum balance limit! 💸")
            return False
        return True

account1 = BankAccount(1000)
account1.deposit(500)
account1.withdraw(200)

savingAccount1 = SavingsAccount(1000, 500)
savingAccount1.withdraw(500)
savingAccount1.withdraw(200)
savingAccount1.withdraw(1500)
