def fibonacci_series():
    # Initialize the first two numbers of the series
    fibonacci_numbers = [0, 1]
    # Loop to generate Fibonacci numbers until reaching 100
    while True:
        # Calculate the next Fibonacci number
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        # Break the loop if the next number exceeds or equals 100
        if next_number >= 100:
            break
        # Add the next number to the series
        fibonacci_numbers.append(next_number)
    # Return the generated Fibonacci series
    return fibonacci_numbers
