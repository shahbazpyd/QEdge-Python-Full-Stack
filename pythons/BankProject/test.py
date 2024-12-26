from acconts import *

# test

sac = Sevingsaccount(0.08,1000)
sac.calculate_interest()
sac.credit(100)
sac.debit(50)
current_balance = sac.get_balance()
print(current_balance)


# chacc= Checkingaccount(5.0,1000)
# chacc.credit(100)
# chacc.debit(50)
# current_balance = chacc.get_balance()
# print(current_balance)


# cacc=Currentaccount(500,1000)
# cacc.credit(100)
# cacc.debit(2000)
# current_balance = cacc.get_balance()
# print(current_balance)
