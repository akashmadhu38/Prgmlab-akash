c=int(input("Enter the limit"))
print(f"Enter {c} integers:")
lst=[]
for i in range(0,c):
    lst.append(int(input()))
print("+ve integers are:")
lst=[i for i in lst if i>0]
print(lst)


