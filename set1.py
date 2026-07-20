dict={
    "pani":"water",
    "aam":"mango",
    "kela":"banana",
    "seb":"apple"
}
print("DICTONARY WORDS ARE:",dict.keys())
a=input("ENTER THE WORD TO GET ITS MEANING:")
if a in dict:
    print("Meaning of",a,"is",dict[a])