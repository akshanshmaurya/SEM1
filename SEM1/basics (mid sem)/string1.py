text=" Python Programming "
text1="My university name is :- GLA University"
#Remove starting and ending whitespaces
trimmed_text=text.strip()
print(trimmed_text)
#convert to lowercase and uppercase
lower_case=text.lower()
upper_case=text.upper()
print("Lowercase",lower_case)
print("Uppercase",upper_case)
#replace
replaced_text=text.replace('Programming',"Coding")
print(replaced_text)
#find substring
index=text1.find("GLA")
print("Index of 'GLA':",index)
#alphabet or not
text3="abc"
print(text3.isalpha())
#check
text2="abc123"
print(text2.isalpha())
number="123"
print(number.isdigit())
text4="abc123"
print(text.isdigit())

text5="  hello world  "
stripped_text=text5.strip()
print(stripped_text)

text6="hello,world"
print(text6.split('o'))

words = ["hello","world"]
print(','.join(words))



