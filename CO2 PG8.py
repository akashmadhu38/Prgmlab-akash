n=int(input("Enter a limit:"))
l=[]
h=[]
for i in range(0,n):
    l.append(input())
for i in range(0,n):
    h.append(len(l[i]))
    h.sort()
print(h[-1:])

