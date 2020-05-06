A = float(input("How big is the area you want to paint (feet): "))
P = float(input("How much is it for a gallon of paint ($): "))

AP = A / 112
H = AP / 12
Cost = P * AP
L = H * 35
Total = Cost + L

print("You need", AP, "gallons of paint and", H, "worth of tradie hours")
print(" labour costing", L, "and total paint price", Cost, ", The total comes to", Total)