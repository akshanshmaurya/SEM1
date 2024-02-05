a=input("Enter you are Veg. or NonVeg :").lower()
b=float(input("Enter Your budget in dollars :"))
c=int(input("Enter your Time Constraint in min. :"))
if a =="veg" and b<= 5 and c<=10:
    print("There we can serve you some delicious Veg Sandwich and Veg burger.")
elif a =="nonveg" and b<= 5 and c<=10:
    print("There we can serve you chicken burger. ;chicken wrap and chicken bucket.(small)")
elif a =="veg" and b<= 10 and c<=15:
    print("there we can serve you delicios veg noodles.")



