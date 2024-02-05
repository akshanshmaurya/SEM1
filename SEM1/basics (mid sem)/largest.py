num1= float(input("Enter first no. :"))
num2= float(input("Enter second no. :"))
if num1< 1 or num2<1:
    print("No.s are invalid please enter a valid value")
elif num1 > num2:
    print(num1 ," is greater than ", num2)
elif num1 < num2:
    print(num2 ,"is greater than ", num1)
elif num1==num2:
    print("Both no. are same.")