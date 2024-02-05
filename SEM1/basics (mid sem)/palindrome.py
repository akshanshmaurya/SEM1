

# word = input("Enter the word you want to check whether it is a palindrome or not. :")
# if word==word[::-1]:
#     print(word , "is a palinndrome. ")
# else:
#     print(word , "is not a palindrome")


num=int(input("Enter a number :"))
a=num
rev=0
while num>0:
    dig=num%10
    rev=(rev*10)+dig
    num=num//10 
if a==rev:
     print(a , "  is palindrome .")
else:
     print(a , "  is not a palindrome .")



 
 