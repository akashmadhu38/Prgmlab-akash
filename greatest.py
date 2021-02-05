a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a>b:
    if a>c:
        print(a ," a is greater")
    else:
        print(c ," c is greater")
elif b>a:
    if b>c:
        print(b ," b Is greater")
    else:
        print(c ," c is greater")
else:
    print(c ," c is greater")