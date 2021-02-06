w=input("Enter a word")
v=["a","e","i","o","u"];
for i in range(1,len(w)):
    if w[i]=="a" or w[i]=="e" or w[i]=="i" or w[i]=="o" or w[i]=="u" or w[i]=="A" or w[i]=="E" or w[i]=="I" or w[i]=="O" or w[i]=="U":
        print(i,w[i] )