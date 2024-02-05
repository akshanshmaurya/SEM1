mylist=[]
num_items=int(input("enter the number of items to add to the list:"))
for i in range(num_items):
    item=input(f"enter item{i+1}:")
    mylist.append(item)
print("final list:",mylist)