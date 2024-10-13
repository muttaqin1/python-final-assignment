
class Bank:
    balance=0
    accounts=[]
    total_loan=0
    loan_enabled=True
    admins=[]

    @staticmethod()
    def add_admin(admin):
        for v in Bank.admins:
            if v.username== admin.username:
                print('username already exists!')
                return
        Bank.admins.append(admin)


