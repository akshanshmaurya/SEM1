num = int(input("Enter a no. : "))
sum = 0
for i in range(1,num+1):
    if i%5 ==0:
        sum=sum+(i-1)+(i-2)
print(sum)        
