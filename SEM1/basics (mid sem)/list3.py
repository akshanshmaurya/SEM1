L=eval(input("enter the list:"))
sum_even=0
sum_odd=0
for i in range(len(L)):
    if L[i]%2==0:
        sum_even=sum_even+L[i]**2
    else:
        sum_odd=sum_odd+L[i]**3
print(sum_even)
print(sum_odd)