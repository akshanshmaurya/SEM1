a=int(input("Enter a starting value :"))
b=int(input("Enter a ending value :"))
for i in range (a , b+1):
    if  i%5==0:
        print(i , "-" , i+2)