import random
Num = random.randint(0,36)
n = (Num % 2)


if Num == 0:
    print("green", Num)

elif Num <= 10:

    if n == 1:
        print("red", Num)

    if n == 0:
        print("black", Num)

elif Num <= 18:

    if n == 1:
        print("black", Num)

    if n == 0:
        print("red", Num)

elif Num <= 28:

    if n == 1:
        print("red", Num)

    if n == 0:
        print("black", Num)

elif Num <= 36:

    if n == 1:
        print("black", Num)

    if n == 0:
        print("red", Num)