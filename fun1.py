def big (a,b,c):
    if a>b and a>c:
        print(a,"is the biggest number")
    elif b>a and b>c:
        print(b,"is the biggest number")
    else:
        print(c,"is the biggest number")
        
p=int(input("Enter first number:"))
q=int(input("Enter second number:"))
r=int(input("Enter third number:"))
big(p,q,r)
    