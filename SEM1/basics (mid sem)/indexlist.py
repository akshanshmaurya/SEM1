numbers=[1,3,5,7,9,11,13,15]
print(f"element at index 3:{numbers[3]}")
print(f"last element:{numbers[-1]}")

sublist=numbers[1:5]
print(f"sublist from index 1 to 4:{sublist}")

numbers[2]=10
print(f"modified list after changing element at index 2:{numbers}")

numbers.append(20)
print(f"list after appending 20:{numbers}")

del numbers[0]
print(f"list after removing element at index 0:{numbers}")

numbers.insert(1,5)
print(f"list after inserting 5 at index 1:{numbers} ")

print(f"final list:{numbers}")