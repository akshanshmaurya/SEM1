num=int(input("Enter a no."))
rev=0
while num>0:
    dig=num%10
    rev=(rev*10)+dig
    num=num//10
print(rev)