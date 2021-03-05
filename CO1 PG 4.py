w=input("Enter a sentence:")
c = dict()
s = w.split()
for i in s:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print(c)

