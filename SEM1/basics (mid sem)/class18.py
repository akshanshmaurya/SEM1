# my_univ=input("My university name is :- ")
# print(my_univ[0:5])
# print(my_univ[5:])
# print(my_univ[:10])
# print(my_univ[-1])


text=" Python Programming "
text1="My university name is :- GLA University"

#remove leading and trailing whitespace
trimmed_text=text.strip()
print(trimmed_text)

#convert to lower case and uppercase 
lower_case= text.lower()
upper_case= text.upper()
print("Lowercase",lower_case)
print("Uppercase",upper_case)
# replace 
replaced_text=text.replace("Programming" , "Coding")
print(replaced_text)
#Find Substring
index = text1.find("GLA")
print("Index of 'GLA' : ", index)
