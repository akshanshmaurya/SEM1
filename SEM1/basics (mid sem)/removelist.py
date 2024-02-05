list=eval(input("Enter The list :"))
unique_list=[]
for x in list:
    if x not in unique_list:
        unique_list.append(x)
print(f"The list after removing duplicates is :{unique_list}")        