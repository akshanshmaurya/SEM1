#sets are used to store multiple items in a single variable
#A set is a collection which is unordered ,unchangeable and unindexed
#set items are unchangeable,but you can remove items and add new items 
thisset={"apple","banana","cherry"}
print(thisset)


thisset1={"apple","banana","cherry","apple"}
print(thisset1)

Myset={"apple","banana","cherry"}
for x in Myset:
    print(x)

thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)


thisset={"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)


thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x)
print(thisset)


thisset={"apple","banana","cherry"}
thisset.clear()
print(thisset)