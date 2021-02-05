lst=[1,2,3,4,5,6,7]
lst1=[2,1,3,5,7,10,6]
s=int(0)
c=int(0)
for i in lst and lst1:
    if len(lst)==len(lst1):
        print("Lists are samae length")
        break
    else:
        print("Lists have different length")
        break
for i in range(0,len(lst) and len(lst1)):
    s=s+lst[i]
    c=c+lst1[i]
for i in range(0, len(lst) and len(lst1)):
    if s==c:
        print("Sum of values are same")
        break
    else:
        print("Sum of values are different")
        break
print("Elements that matched are:")
l=[]
for i in range(0,len(lst)):
    for j in range(0,len(lst1)):
        if lst[i]==lst1[j]:
            l.append(lst[i] and lst1[j])
        else:
            p=i
            continue
print(l)
