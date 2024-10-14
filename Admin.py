from Bank import Bank

class Admin:
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password
        self.bank=Bank()

    def delete_user(self,bank_account_no):
        self.bank.delete_account(bank_account_no)


    def get_all_accounts(self):
        for account in self.bank.accounts():
            print(f'Name: {account.name} \tAccount no: {account.get_acc_no}\tBalance: {account.get_acc_balance}\n')
    
    def get_total_bank_balance(self):
        print(f'Total bank balance: {self.bank.get_balance}')

    def get_total_loan_amount(self):
        print(f'Total loan amount: {self.bank.get_total_loan}')
    
    def disable_loan(self):
        self.bank.set_loan_status(False)
        print('Loan disabled!')