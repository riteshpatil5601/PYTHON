l=int(input("Enter a number:"))

for i in range(2,l):
    if l%i==0:
        print(l,"is not a prime number")
        break
else:
    print(l,"is a prime number")