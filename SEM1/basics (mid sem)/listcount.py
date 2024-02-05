list=eval(input("Enter a list :"))
num=int(input("Enter the element "))
c=0
for x in list:
    if x==num:
        c+=1
print("the number of times it occur is ",c)