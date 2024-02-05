# Consider the string 
st1='hello welcome to gla university'
print("string:",st1)

#Slice First 10 characters
print(st1[slice(10)])

#slice form last 4 th psotion to the 10 th postion
print(st1[slice(-10,-3)])

#slice from first character to 5 th character 
print(st1[slice(0,5)])

#slice from 2nd character to 10th character by skipping 3 characters
print(st1[slice(0,5,3)])

#return the entire string using array slicing
print(st1[:])

#slice from 7 th character to 20 th charcter
print(st1[6:20])

