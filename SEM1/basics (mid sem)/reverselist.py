# list=eval(input("Enter a list :"))
# newlist=list[::-1]
# newlist=list[::-1]
# print(newlist)


# List=eval(input("Enter a list :"))
# newlist=[]
# for a in List:
#     newlist=[a]+newlist
# print(newlist)

list=eval(input("Enter a list :"))
reversed_list=[]
for i in range(len(list)-1,-1,-1):
    reversed_list.append(list[i])
print(f"The reversed list is :{reversed_list}")    