n=[]
s=int(input("Enter a limit"))
print(f"Enter {s} values")
for i in range(0,s):
    n.append(int(input()))
for i in range(0,len(n)):
    if n[i]>=100:
        print("over")
    else:
        print(n[i])