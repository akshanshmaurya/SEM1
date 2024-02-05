l= eval(input("Enter a list :"))
a=b=0
for i in l:
    if i%2==0:
        a+=i
    else:
        b+=i
print(a)
print(b)        