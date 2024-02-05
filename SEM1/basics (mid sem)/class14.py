"""
start=10
end=51
prime_numbers=[]
for num in range(start,end+1):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if(num%i)==0:
                break
        else:
            prime_numbers.append(num)

print(f"prime numbers between {start} and {end} :",prime_numbers)

"""


start =int(input("Enter a start value :"))
end =int(input("Enter an end value :"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
                print(num,end=",")
