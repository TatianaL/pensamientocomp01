def fibonacci(n):
    # Initialize the first two numbers of the sequence
    fib_sequence = [0, 1]
    
    # Generate the sequence up to n numbers
    while len(fib_sequence) < n:
        # Next number is sum of the last two numbers
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Get input from user
n = int(input("Ingrese cuántos números de la serie de Fibonacci desea ver: "))

# Validate input
if n <= 0:
    print("Por favor ingrese un número mayor que 0")
else:
    # Get and print the sequence
    resultado = fibonacci(n)
    print(f"\nLos primeros {n} números de la serie de Fibonacci son:")
    print(resultado)