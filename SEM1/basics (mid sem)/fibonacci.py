limit= 1000
fibonacci_sequence = [0,1]

while True:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    if next_number > limit:
        break
    fibonacci_sequence += [next_number]

print("Fibonacci Sequence :")
print(fibonacci_sequence)