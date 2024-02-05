text = input("Enter a text :")
a=b=0
for i in text:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        b+=1
    else:
        continue
print(f"Number of Alphabets are : {a}")
print(f"number of Digits are : {b}")        
                                                                                                            