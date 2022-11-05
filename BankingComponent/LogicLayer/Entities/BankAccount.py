
class BankAccount():
    
    def __init__(self, email, account_number, CVV, pin_code, balance):
        self.email = email
        self.account_number = account_number
        self.CVV = CVV
        self.pin_code = pin_code
        self.balance = balance


    
    def return_account(self):
        return self.email, self.account_number, self.CVV, self.pin_code, self.balance