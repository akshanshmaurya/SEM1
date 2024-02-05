mylist=[]
num_items=int(input("Enter the number of items to add to the list :"))
for i in range(num_items):
    item=input(f"enter items {i+1}:")
    mylist.append(item)
print("Final list :",mylist)    