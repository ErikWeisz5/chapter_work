import time


s = int(input("Speed your going"))
h = int(input("Time travelled in hours"))
t = 0

while t < h:
    t = t + 1
    d = s * t
    time.sleep(2)
    print("After", t, "your going to travel", d, "Km's")