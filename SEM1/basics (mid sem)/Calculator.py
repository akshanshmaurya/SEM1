list=[]
n=0
operation=list
while(True):
     print("1. Addition ")
     print("2. Subtraction")
     print("3. Multiplication")
     print("4. Division")
     print("5. Display Operations")
     print("6. Quit")
     ch =float(input("Enter your Choice(1/2/3/4/5/6) :"))
     print()
     if ch==1:
          a=float(input("Enter your First Number :"))
          b=float(input("Enter your Second Number :"))
          result=a+b
          print(a,"+",b,"=", result)
          print()
          n+=1
          list.append(f"{n}. {a} + {b} = {result}")
     elif ch==2:
          a=float(input("Enter your First Number :"))
          b=float(input("Enter your Second Number :"))
          result=a-b
          print(a,"-",b,"=",result)
          print()
          n+=1
          list.append(f"{n}. {a} - {b} = {result}")
     elif ch==3:
          a=float(input("Enter your First Number :"))
          b=float(input("Enter your Second Number :"))
          result=a*b
          print(a,"*",b,"=",result)
          print()
          n+=1
          list.append(f"{n}. {a} * {b} = {result}")
     elif ch==4:
          a=float(input("Enter your First Number :"))
          b=float(input("Enter your Second Number :"))
          if b==0:
               print(b, " can not be used for the division. ")
               continue   
          result=a//b
          print(a,"//",b,"=",result)
          print()
          n+=1
          list.append(f"{n}. {a} // {b} = {result}")   
     elif ch==5:
          if not operation:
               print("No opertions performed yet.")
          else:
               for i in list:
                print(i)
          print()   
     elif ch==6:
          break
     else:
          print("Wrong Choice")
                              
              