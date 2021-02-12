l=int(input("Enter length of the rectangle:"))
b=int(input("Enter breath of the rectangle:"))
h=int(input("Enter height of triangle:"))
ar=lambda x,y: x*y
asq=lambda x: x*x
at=lambda x,y:0.5*b*h
print("Area of rectangle:",ar(l,b))
print("Area of square:",asq(l))
print("Area of triangle:",at(b,h))