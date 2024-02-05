height= float(input("Enter your height in m :"))
weight=float(input("Enter your Weight in kg :"))
bmi= weight/(height**2)
if bmi <= 18.5:
    print("Underweight")
elif bmi <= 25:
    print("Normal")
elif bmi<=38:
    print("Overweight")
else:
    print("obese")