# my_list=eval(input("Enter a list :"))
# max_element=my_list[0]
# min_element=my_list[1]
# if min_element>max_element:
#         max_element,min_element=min_element,max_element
# for num in my_list[2::]:
#     if num>max_element:
#         min_element=max_element
#         max_element=num
#     elif max_element>num>min_element:
#         min_element=num
# print(f"the second largest number in the list is:{min_element}")



a=[2,4,3,5,6,4,7,8,]
a.sort()
print(a[-2])
