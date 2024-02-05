a = int(input("Enter the fibonacci series limit : "))
b = 0
c = 1
d = 0
for i in range(1,a+1):
    b=c
    c=d
    d=b+c
    print(d,end=",")