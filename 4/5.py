
y = int(input("years?"))
a = 0
b = 0
r = set()
while a < y:
    while b < 12:
        s = int(input("rainfall monthly): "))
        b = b + 1
        r.add(s)
    a = a + 1
print ("including", 12 * y, "months")
r = list(r)
i = 0
c = 0
while i < y * 12:
    c = r[i] + c
    i = i + 1
print ("Average rain per month: ", c/(y * 12))
print ("Total rainfall ", c)