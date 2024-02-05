numbers= [int(x) for x in input("Enter a list of integers seperated by spaces:").split()]
result=[x**2 for x in numbers if (x**2)% 2 ==0]
print(" ".join([str(x) for x in result]))