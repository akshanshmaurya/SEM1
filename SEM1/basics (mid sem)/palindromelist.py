list=eval(input("Enter a list :"))
newlist=list[::-1]
if list==newlist:
    print("The given list is a pallindrome .")
else:
    print("The given list is not pallindrome .")