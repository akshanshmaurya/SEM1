num= int(input("Enter a number :"))
num_digits=len(str(num))
sum=0
while num>0:
    dig=num%10
    sum+=dig**num_digits
    sum= sum//10
if sum==num:
    print(num , " is a armstrong .")  
else:
    print(num , " is not a armstrong .")  
