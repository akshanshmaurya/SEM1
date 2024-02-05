a=float(input("Enter side 1 of a Triangle."))
b=float(input("Enter side 2 of a Triangle."))
c=float(input("Enter side 3 of a Triangle."))
if a==b and b==c:
    print("The Triangle is an Equilateral Triangle. ")
elif a==b or b==c or c==a:
    print("The Triangle is an Isoceles Triangle. ")
else:
    print("The Tiangle is a Scalene Triangle. ")
