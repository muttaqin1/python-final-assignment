class User:
    def __init__(self,name,email,address) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.bank_accounts={'savings':[],'current':[]}

