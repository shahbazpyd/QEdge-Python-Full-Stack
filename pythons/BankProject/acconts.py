class Account:
    def __init__(self,balance=0.0):
        self.balance=balance
        if self.balance<0:
            self.balance=0.0
            print("initial_balance is invalid")
        
    
           
    def credit(self,amount):
        self.balance+=amount
        # return self.balance
        # print("credit amount is ",amount)
        # print("initial balance is ",self.balance)
        
    def debit(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            # return self.balance
            # print("debit amount is ",amount)
            # print("initial balance is ",self.balance)
        else:
            print("Debit amount exceeded account balance.")
            
    def get_balance(self):
        return self.balance
           

         
      
        
class Sevingsaccount(Account):
    
    def __init__(self,interest_rate=0.0,balance=0.0):
        self.interest_rate=interest_rate
        super().__init__(balance)
      
        
    def calculate_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned 
        # print("initial balance after interest: ",self.balance)
        return self.balance 
        
    
    def credit(self,amount):
        self.balance+=amount
        # print("initial balance after credit: ",self.balance)
        
        
    def debit(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            # print("initial balance after debit: ",self.balance)
           
        else:
            print("Debit amount exceeded account balance.")
            
    def get_balance(self):
        return self.balance

    
    
    
class Checkingaccount(Account):
    def __init__(self,fee_charges=0.0,balance=0.0):
        self.fee_charge=fee_charges
        super().__init__(balance)
        
    def credit(self,amount):
        self.balance+=amount
        self.balance-=self.fee_charge
        # print("initial balance after credit and fee charge : ",self.balance)
        
        
    def debit(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.balance-=self.fee_charge
            # print("initial balance after debit and fee charge: ",self.balance)
           
        else:
            print("Debit amount exceeded account balance.")
            
    def get_balance(self):
        return self.balance
    
    
    
    
    
    
class Currentaccount(Account):
    def __init__(self,overdraft_limit=0.0,balance=0.0):
        self.overdraft_limit=overdraft_limit
        super().__init__(balance)
        
        
    def credit(self,amount):
        self.balance+=amount
        # print("initial balance after credit : ",self.balance)
    
        
    def debit(self,amount):
        if self.balance>= amount:
            self.balance-=amount
            # print("initial balance (greater than amount) after debit : ",self.balance)
        elif self.balance< amount and self.balance>0:
            if (amount-self.balance) <= self.overdraft_limit:
                self.balance -= amount
                # print("initial balance (lesser than amount) after debit : ",self.balance)
            else:
                print("Debit amount exceeded to Overdraft limit.")
        elif self.balance<=0:
            if amount< self.overdraft_limit:
                self.balance-=amount
                # print("initial balance (lesser than 0) after debit : ",self.balance)   
            else:
                print("Debit amount exceeded to Overdraft limit.")

            
    def get_balance(self):
        return self.balance

