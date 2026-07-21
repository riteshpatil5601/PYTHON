a=int(input("Enter marks 1:"))
b= int(input("Enter marks 2:"))
c=int (input("Enter marks 3:"))
d=(a+b+c)*40/100
e=(a+b+c)*100//300
if d>=40:
    if a>=33 and b>=33 and c>=33:
        print(e,"%:pass")
    else:
        print("fail")
else:
    print("fail")
