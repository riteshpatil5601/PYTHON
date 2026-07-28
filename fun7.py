def s(l,n):
    result=[]
    for i in l:
        if i.strip()!=n:
            result.append(i)
    return (result)
        

list=["Abhi","Rahul","Ritesh","Sahil"]
k="Ritesh"
print("List after removing",k,"is",s(list,k))