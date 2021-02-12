st=input("Enter a word:")
c=0
for i in st:
    if i==" ":
        continue
    else:
        c+=1
print(c," Characters in "+st)