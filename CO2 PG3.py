n=int(input("Enter a limit:"))
print(f"Enter {n} values:")
s=0
lst=[]
for i in range(0,n):
    lst.append(int(input()))
    s=s+lst[i]
print(s)
