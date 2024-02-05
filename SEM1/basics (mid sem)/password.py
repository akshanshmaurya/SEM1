
while(True):
  text=input("Enter your Password :")
  a1=a2=a3=a4=0
  if len(text)>=12:
   for i in text:
       if i.isalpha():
          if i.isupper():
           a1+=1
          elif i.islower():
           a2+=1
       elif i.isdigit():
           a3+=1
       else:
          a4+=1
   if (a1>=1 and a2>=1 and a3>=1 and a4>=1):
       print("You entered a valid password")
       break
   else:
       print("Your password is incorect")
       continue
    





