from collections import OrderedDict
d={}
di={}
a=int(input("Enter a limit:"))
for i in range(0,a):
    k=int(input("Enter key:"))
    v=int(input("Enter value:"))
    d.update({k:v})
b=int(input("\nEnter a limit:"))
for i in range(0,b):
    ke=int(input("Enter key:"))
    vv=int(input("Enter value:"))
    di.update({ke:vv})
print("Before merging:",d,di,end=" ")
s={}
s.update(d)
s.update(di)
print("\nAfter merging:",s)
