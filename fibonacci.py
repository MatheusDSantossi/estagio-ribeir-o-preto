def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
        
    return fib_sequence

def is_in_fibonnaci(n):
    fib_sequence = fibonacci(n)
    if n in fib_sequence: 
        return f"The number {n} belongs to the fibonacci sequence"
    
    return f"The number {n} does not belong to the fibonacci sequence"

number = int(input("Type the number: "))

print(is_in_fibonnaci(number))
