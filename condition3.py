a="Make a lot of money"
b="Buy now"
c="subscribe this"
d="Click this"
e=input("Enter a message:")
if e==a or e==b or e==c or e==d:
    print(e,": is a spam message")
else:
    print(e,": is not a spam message")