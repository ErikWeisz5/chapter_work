length = int(input("rectangle length: "))
width = int(input("rectangle width:"))
length2 = int(input("rectangle 2 length: "))
width2 = int(input("rectangle 2 width: "))
r1 = (length*width)
r2 = (length2 * width2)
if r1 > r2:
    print("The first rectangle was a bigger rectangle :(")
if r1 == r2:
    print("Both rectangles are the same ")
else:
    print("The second rectangle was a bigger rectangle :)")