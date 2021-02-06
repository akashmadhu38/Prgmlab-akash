from collections import OrderedDict
d={}
a=int(input("Enter a limit:"))
for i in range(0,a):
    k=int(input("Enter key:"))
    v=int(input("Enter value:"))
    d.update({k:v})
for i in sorted(d):
    print(i,d[i],end=",")