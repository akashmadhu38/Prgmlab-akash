n=int(input("Enter a limit:"))
a=0
b=1
s=0
for i in range(0,n):
    s=a+b
    a=b
    b=s
    print(s)
