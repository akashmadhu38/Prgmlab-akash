n=int(input("Enter a limit:"))
lst=[]
print(f"Enter {n} numbers")
for i in range(2,n+2):
    lst.append(int(input()))
lst=[i*i for i in lst]
print(lst)




