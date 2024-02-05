#coincise way to create lists
squares=[x**2 for x in range(5)]
print(squares)


even_numbers=[x for x in range(10) if x%2==0]
print(even_numbers)
   

results=["Pass" if score>=60 else"Fail" for score in[75,30,85.50]]
print(results)


names=['john','jane','jim']
name_lengths=[len(name) for name in names]
print(name_lengths)