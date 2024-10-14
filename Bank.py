
class Bank:
    __balance=10000
    __accounts=[]
    __total_loan=0
    __loan_enabled=True
    __admins=[]


    
    def accounts(self):
        return Bank.__accounts
    
    def add_account(self,acc):
        Bank.__accounts.append(acc)

    @property
    def get_balance(self):
        return Bank.__balance
    

    @property
    def get_total_loan(self):
        return Bank.__total_loan

    @property
    def add_loan(self,amount):
        Bank.__total_loan+=amount

    def add_money(self,amount):
        Bank.__balance+=amount
    
    
    
    def remove_money(self,amount):
        Bank.__balance-=amount
    
    @property
    def total_loan(self):
        return Bank.__total_loan
    
    def add_loan(self,amount):
        Bank.__total_loan+=amount
    
    
    @property
    def loan_enabled(self):
        return Bank.__loan_enabled
    
    
    
    def set_loan_status(self,status):
         Bank.__loan_enabled=status


    

    
    def add_admin(self,admin):
        for v in Bank.admins:
            if v.username== admin.username:
                print('username already exists!')
                return
        Bank.admins.append(admin)

    
    def verify_admin(self,username,password):
        for admin in Bank.admins:
            if admin.username==username:
                if admin.password ==password:
                    return True
        
        return False

    
    def exists_account(self,acc_no):
        for index,account in enumerate(Bank.__accounts):
            if account.get_acc_no == acc_no:
                return index
        return None
    
    def update_account_money(self,acc_no,amount):
        temp=self.exists_account(acc_no)
        if temp==None:
            print("Invalid reciver account no.")
            return False
        Bank.__accounts[temp].add_acc_balance(amount)
        return True
    
    def delete_account(self,acc_no):
        if self.exists_account(acc_no)==None:
            print("User doesnt exists!")
            return
        for account in Bank.__accounts:
            if account.get_acc_no == acc_no:
                Bank.__accounts.remove(account)
        print(f'{acc_no} deleted!')
        

        
