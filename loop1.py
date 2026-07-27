p=[]
for s in range(1,11):

 l=int(input("Enter 10 numbers:"))
 p.append(l)
for i in p:
    for j in range (1,11):
        print(i,"*",j,"=",i*j)