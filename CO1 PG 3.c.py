w=input("Enter a word")
v=["a","e","i","o","u"];
s=[i for i in w if i in v]
print("Number of vowels:",len(s))
print(s)
