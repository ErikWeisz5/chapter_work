print("number of coins needed for one dollar")
p = int(input("enter amount of pennies"))
n = int(input("enter amount of nickels"))
d = int(input("enter amount of  dimes"))
q = int(input("enter amount of quarters"))

pennies = 0.01
nickels = 0.05
dimes = 0.1
quarters = 0.25

TotalP = p*pennies
TotalN = n*nickels
TotalD = d*dimes
TotalQ = q*quarters

T = TotalP+TotalN+TotalD+TotalQ

if T == 1:
    print("total of your dollar")

else:
    print("your wrong ", T - 1)