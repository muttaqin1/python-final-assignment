from Bank import Bank
from Transaction import Transaction

class Bank_account:

    def __init__(self,acc_type,name,email,address) -> None:
        self.__acc_no=email.split('.')[0]
        self.__acc_type=acc_type
        self.__acc_balance=0
        self.__transactions=[]
        self.__loan_count=0
        self.name=name
        self.email=email
        self.address=address
        self.__bank=Bank()
        self.__bank.add_account(self)
    


    def __validate_amount(self,amount):
        if amount <= 0 :
            print('Please enter a valid amount!')
            return False
        if self.__acc_balance < amount:
            print('Withdrawal amount exceeded!')
            return False
        if self.__bank.get_balance < amount:
            print('Bank is bankrupt.')
            return False
        return True
    
    @property
    def get_acc_balance(self):
        return self.__acc_balance
    
    def add_acc_balance(self,amount):
        self.__acc_balance+=amount

    @property
    def get_acc_no(self):
        return self.__acc_no

    def deposit(self, amount):
        if amount <= 0 :
            print('Please enter a valid amount!')
            return
        self.__acc_balance+=amount
        self.__bank.add_money(amount)
        self.__transactions.append(Transaction().deposit(amount))
        print(f'Amount: {amount} added.')
        self.check_balance()
    
    def withdraw(self, amount):
        if not self.__validate_amount(amount): return
        self.__acc_balance-=amount
        self.__bank.remove_money(amount)
        self.__transactions.append(Transaction().withdraw(amount))
        print(f'Withdraw {amount} successful!')
        self.check_balance()

    def check_balance(self):
        print(f'Account current balance: {self.__acc_balance}')
    
    def transfer(self, reciever_ac_no, amount):
        if reciever_ac_no==self.__acc_no:
            print('Invalid action!')
            return
        if not self.__validate_amount(amount): return
        if not self.__bank.update_account_money(reciever_ac_no,amount):return
        self.__acc_balance-=amount
        self.__transactions.append(Transaction().transfer(self.__acc_no,reciever_ac_no,amount))
        print(f'{amount} transfer successful to account :{reciever_ac_no}')
        self.check_balance()

    
    def get_transaction_history(self):
        if len(self.__transactions)==0:
            print("Transaction list is empty!")
            return
        for v in self.__transactions:
            print(v)
            print()

    def take_loan(self, amount):
        if amount <=0 :
            print("Invalid amount!")
            return
        if self.__loan_count > 1:
            print('Loan limit exceeded!')
            return
        if not self.__bank.loan_enabled:
            print('Bank has disabled loans!')
            return
        if self.__bank.get_balance < amount:
            print('Bank is bankrupt.')
            return
        self.__loan_count+=1
        self.__acc_balance+=amount
        self.__bank.add_loan(amount)
        self.__transactions.append(Transaction().loan(amount))
        print(f'You have got loan amount: {amount}.\nCurrent balance: {self.__acc_balance}')

    



        