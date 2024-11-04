class BankAccount:
    def __init__(self):
        self.owner = input("사용자 : ")
        self.balance = int(input("잔액 : "))

    def deposit(self):
        self.amount = int(input("입금 금액 : "))
        self.balance += self.amount

    def withdraw(self):
        self.amount = int(input("출금 금액 : "))
        self.balance -= self.amount

    def display_balance(self):
        print("통장 잔액 : ", self.balance)

information = BankAccount()
information.deposit()
information.withdraw()
information.display_balance()





