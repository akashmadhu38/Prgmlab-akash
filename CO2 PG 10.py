n=int(input("Enter a number:"))
print(f"factor of {n} are:")
for i in range(0,n):
    for j in range(0,n):
        if i*j==n:
            print(i,j)
