from datetime import datetime


class Transaction:

    def __init__(self) -> None:
        self.type=None

    def deposit(self, amount):
       self.date=datetime.now() 
       self.amount=amount
       self.type='deposit'
       return self

    def withdraw(self, amount):     
        self.date=datetime.now() 
        self.amount=amount
        self.type='Withdraw'
        return self
    
    def transfer(self,sender_acc_no, reciever_ac_no, amount):
        self.date=datetime.now() 
        self.amount=amount
        self.type='Transfer'
        self.sender_acc_no=sender_acc_no
        self.reciever_acc_no=reciever_ac_no
        return self   
    
    def loan(self, amount):
        self.date=datetime.now() 
        self.amount=amount
        self.type='Loan'
        return self
    
    def __repr__(self) -> str:
        if self.type == 'Loan':
            return f'TYPE: {self.type.upper()}\nAMOUNT: {self.amount}\nDATE: {self.date}\n'
        elif self.type == 'Transfer':
            return f'TYPE: {self.type.upper()}\nAMOUNT: {self.amount}\nDATE: {self.date}\nSENDER: {self.sender_acc_no}\nRECIEVER: {self.reciever_acc_no}'
        elif self.type == 'Withdraw':
            return f'TYPE: {self.type.upper()}\nAMOUNT: {self.amount}\nDATE: {self.date}\n'
        else :
            return f'TYPE: {self.type.upper()}\nAMOUNT: {self.amount}\nDATE: {self.date}\n'


