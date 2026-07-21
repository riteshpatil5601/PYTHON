a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
d=int(input("Enter a number:"))

if a>b and a>c and a>d:
    print(a," :is the greatest number")
elif b>a and b>c and b>d:
    print(b," :is the greatest number")
elif c>a and c>b and c>d:
    print(c," :is the greatest number")
else:
    print(d," :is the greatest number")