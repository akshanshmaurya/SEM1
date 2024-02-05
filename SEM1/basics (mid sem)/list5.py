# num=int(input("Enter the number :"))
# sum=0
# while num!=0:
#     r=num%10
#     sum=sum+r
#     num=num//10
# print(sum)    




num=int(input("Enter a number (except one-digit) :"))
digits=[int(digit) for digit in str(num)]
sum_of_digits=0
for digit in digits:
    sum_of_digits+=digit
print(f"The sum of digits in {num} is {sum_of_digits}")    