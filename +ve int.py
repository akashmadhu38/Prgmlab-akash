c=int(input("Enter the limit"))
print("Enter some integers:")
lst=[]
for i in range(0,c):
    lst.append(int(input()))
for i in lst:
    if i<0:
        continue;
    else:
        print(i)

