a=input("Enter a msg:")
if " " in a:
    print("Space is present in the string at index:",a.index(" "),"and the total number of spaces present in the string is:",a.count(" "))
else:
    print("Space is not present in the string")