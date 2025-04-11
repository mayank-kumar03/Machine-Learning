import math

# Take input from the user as a list of numbers
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

# Perform operations
maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)
total_sum = sum(numbers)
squared_roots = [math.sqrt(num) for num in numbers]
rounded_numbers = [round(num) for num in numbers]

# Display results
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Average: {average}")
print(f"Sum: {total_sum}")
print("Square Roots:", squared_roots)
print("Rounded Numbers:", rounded_numbers)
