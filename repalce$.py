w=str(input("Enter data:"))
for i in range(0,len(w)):
    if i==0:
        print(w[i])
    else:
        if w[i] == w[0]:
            print("$")
        else:
            print(w[i])

