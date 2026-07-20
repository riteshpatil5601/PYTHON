b=set()
c=set()
for i in range (8):
    a=int(input("Enter the number:"))
    if a in b:
        c.add(a)
    else:
        b.add(a)
print("without duplicates:",b)
print("The duplicate numbers are:",c)