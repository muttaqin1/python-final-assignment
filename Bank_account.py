from abc import ABC

class Bank_account_interface(ABC):
    
    def __init__(self,acc_type,acc_balance,user) -> None:
        self.acc_no=f'{user.name}:{user.email}'
        self.acc_type=acc_type
        self.acc_balance=acc_balance
        self.user=user
        self.transactions=[]
        self.loan_count=0

    def deposit(self,amount):
        raise NotImplementedError()
    
    def withdraw(self,amount):
        raise NotImplementedError()
    
    def check_balance(self):
        raise NotImplementedError()
    
    def transfer(self,reciever_ac_no,amount):
        raise NotImplementedError()
    
    def get_transaction_history(self):
        raise NotImplementedError()
    
    def take_loan(self,amount):
        raise NotImplementedError()

   




        