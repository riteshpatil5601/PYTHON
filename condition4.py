a=input("Enter a username:")
if len(a)<10:
    print("Username contains less than 10 characters")
elif len(a)==10:
    print("Username contains 10 characters")
else:
    print("Username contains more than 10 characters")