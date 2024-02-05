n= int(input("Enter a positive integer (N) :"))
sum_of_numbers1 = 0
sum_of_numbers2 = 0
for i in range (1,n+1):
    if i%2==0:
        sum_of_numbers1+=i
    elif i%2 !=0:
        sum_of_numbers2+=i
print(f"The sum of even numbers is :{sum_of_numbers1}")
print(f"The sum of odd numbers is :{sum_of_numbers2}")    

