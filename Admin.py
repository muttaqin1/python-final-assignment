from abc import ABC

class Admin_interface(ABC):

    def __init__(self,name,username,password) -> None:
        self.name=name
        self.username=username
        self.password=password
    
    def delete_user(self):
        raise NotImplementedError()
    
    def get_all_accounts(self):
        raise NotImplementedError()
    
    def get_total_bank_balance(self):
        raise NotImplementedError()
    
    def get_total_loan_amount(self):
        raise NotImplementedError()
    
    def disable_loan(self):
        raise NotImplementedError()