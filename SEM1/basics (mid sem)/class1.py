amount = float(input("Enter your amount :"))
member = input("Are you a member? (yes/no) :").lower()
if amount >= 100 and member == "yes":
    discount = amount - amount/10
    print("Discounted Amount is :" , discount)
else:
    print("Your final Amount is :" , amount)
