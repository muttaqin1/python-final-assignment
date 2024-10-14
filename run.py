from Bank import Bank
from Bank_account import Bank_account
from Admin import Admin

main_menu="""
    1. User
    2. Admin
    3. Exit
please enter any key: """

admin=Admin('admin','123')
bank_acc=None

sample_acc_1=Bank_account('current','rakib khan','rakib@gmail.com','dhaka')
sample_acc_2=Bank_account('savings','md rohim','rohim@gmail.com','khulna')
sample_acc_3=Bank_account('savings','sayem khan','sayem@gmail.com','sylhet')

def verify_account_creation(acc):
    if acc==None:
        print('Please create an account!')
        return False
    return True

def getName(acc):
    if acc==None:
        return ''
    else:
        return f'Welcome {acc.name},\n' 
    
    
user_op="""
        1. Create account.
        2. Deposit.
        3. Withdraw.
        4. Transfer.
        5. Check balance.
        6. Transaction history.
        7. Take loan.
        8. Exit
Please enter any key: """
def user_operations():
    global bank_acc
    while True:
        op=int(input(f'\n\t\t\t{getName(bank_acc)}'+user_op))
        if op == 1:
            acc_type=input('Please enter the account type [savings/current]:')
            name=input('Please enter your name: ')
            email=input('Please enter your email: ')
            address=input('Please enter your address: ')
            if acc_type not in ['savings','current']:
                print("Please enter a valid account type.")
                continue
            if len(name) ==0:
                print("Please enter a valid name")
                continue
            if len(email)==0:
                print("Please enter a valid email")
                continue
            if len(address)==0:
                print("Please enter a valid address")
                continue
            bank_acc=Bank_account(acc_type,name,email,address)
            print('---Account creation successful.')
        elif op==2:
            if not verify_account_creation(bank_acc):continue
            amount=int(input('Please enter any amount: '))
            bank_acc.deposit(amount)
        elif op==3:
            if not verify_account_creation(bank_acc):continue
            amount=int(input('Please enter any amount: '))
            bank_acc.withdraw(amount)
        elif op==4:
            if not verify_account_creation(bank_acc):continue
            reciever_acc=input('Please enter reciever account no: ')
            amount= int(input('Please enter any amount: '))
            if len(reciever_acc)==0:
                print('Please enter a valid reciever account!')
                continue
            bank_acc.transfer(reciever_acc,amount)
        elif op==5:
            if not verify_account_creation(bank_acc):continue
            bank_acc.check_balance()
        elif op==6:
            if not verify_account_creation(bank_acc):continue
            bank_acc.get_transaction_history()
        elif op==7:
            if not verify_account_creation(bank_acc):continue
            amount= int(input('Please enter any amount: '))
            bank_acc.take_loan(amount)
        elif op==8:
            break
        else:
            print("Please enter a valid key!")


admin_op="""
1. Delete user.
2. Accounts.
3. Bank balance.
4. Loan amount.
5. Disable loan.
6. Exit.
Please enter any key: """


def admin_operations():
    while True:
        op=int(input(admin_op))
        if op==1:
            acc = input('Please enter a bank account no: ')
            admin.delete_user(acc)
        elif op==2:
            admin.get_all_accounts()
        elif op==3:
            admin.get_total_bank_balance()
        elif op==4:
            admin.get_total_loan_amount()
        elif op==5:
            admin.disable_loan()
        elif op==6:
            break
        else:
            print('Please enter a valid key!')

def run():
    while True:
        op=int(input(main_menu))
        if op == 1:
            user_operations()
        elif op==2:
            username=input('Please enter your username: ')
            password=input('Please enter your passowrd: ')
            if username==admin.username and password==admin.password:
                admin_operations()
            else:
                print('Invalid credentials.')
        elif op==3:
            break
        else:
            print('Please enter a valid key!')


run()