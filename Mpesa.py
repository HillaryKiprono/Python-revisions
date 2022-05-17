class Mpesa:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def check_balance(self):
        return self.balance

    def deposit_money(self, amount):
        self.balance = self.balance + amount

    '''
    Transaction fee is 10/=
    '''

    def withdraw_money(self, amount):
        if 60 <= self.balance <= amount:
            self.balance = self.balance - amount - 10
            print(f'You have withdrawn KSH. {amount}, your balance is KSH. {self.balance}')
        else:
            print(f'You have insufficient fund, your balance is KSH. {self.balance}')


mpesa = Mpesa(1000, "0706003891")

mpesa.deposit_money(500)
print(mpesa.check_balance())
mpesa.withdraw_money(1600)
