n=int(input("Enter a limit:"))
lst=[]
print(f"Enter {n} numbers")
for i in range(1,n+1):
    a=int(input())
    lst.append(a)
for i in range(0,n):
     print(lst[i]*lst[i])




