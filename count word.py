w=input("Enter a sentence:")
c = dict()
s = w.split()
for s in s:
    if s in c:
        c[s] += 1
    else:
        c[s] = 1
print(c)

