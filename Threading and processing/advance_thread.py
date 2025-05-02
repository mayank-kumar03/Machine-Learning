from concurrent.futures import ThreadPoolExecutor
import time

def print_number(num):
    time.sleep(1)
    return f"Number: {num}"

numbers = [1, 23, 4, 5, 6]

# Corrected 'max_workers' parameter
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result
