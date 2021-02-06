n=int(input("Enter a limit:"))
print(f"Enter {n} words")
w=[]
l=[]
s=[]
for i in range(0,n):
    w.append(input())
    l.append(w[i].split())
l=sum(l,[])
for i in range(0,n+1):
    if i%2==0:
        s.append(l[i])
str1=""
for i in s:
    str1+=i
print("Number of a in ",s," is:")
c=0
for i in range(0,len(str1)):
    if str1[i]=="a":
        c+=1
print(c)
