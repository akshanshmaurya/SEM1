gpa =  float(input("Enter your GPA :"))
ques = input("have you ever participated in any extracuricular activities (yes/no) :").lower()
if gpa >= 3.5 and ques == "yes":
    print("You are eligible for scholarship ")
else:
    print("You are not eligible for scholarship") 