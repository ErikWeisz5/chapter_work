l = int(input("number of laps: "))
r = set()
a = 0
b = 0

while a < l:
    seconds = int(input("Lap time: "))
    r.add(seconds)
    a += 1

r = list(r)
r.sort()

while  b < l:
    b += r[b]
average = b/l

print("fastest lap : ", r[0])
print("Slowest Lap : ", r[a-1])
print("average lap : ", average)