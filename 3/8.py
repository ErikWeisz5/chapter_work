att = int(input("People attending: "))
hdpp = int(input("Hot dogs per-person: "))
t = att * hdpp

rp = t // 10
l = t % 10
p = t // 8
b = t % 8

print ("Required Hotdogs packs:", rp)
print("Bun Packets required", p)
print ("Hot dogs left over", l)
print ("Buns leftover", b)