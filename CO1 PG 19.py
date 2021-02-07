a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
i = 1
while i<=a and i<=b:
  if a%i==0 and b%i==0:
    gcd = i
  i = i + 1
print("GCD is", gcd)