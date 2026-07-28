def sum(n):
    if n==0:
        return (0)
    else:
        return (n+sum(n-1))
r=int(input("Enter a number:"))
print("Sum of numbers from 1 to", r, "is", sum(r))