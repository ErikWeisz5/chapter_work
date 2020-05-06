number = int(input("Enter your number to be analysed..."))
if number > 0:
    print("Positive")
if number < 0:
    print("Negative")
if number == 0:
    print("even")
num = (number % 2)
if num == 1:
    print ("Odd")
if num == 0:
    print ("Even")