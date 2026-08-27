import random

# Mock Data Generation - Creating 100 random integers between 0 and 1000
print("Generating mock data...")
data_list = [random.randint(0, 1000) for _ in range(100)]
print(f"Generated {len(data_list)} random numbers")

# Sorting the list from minimum to maximum
data_list.sort()
print("Data sorted successfully")

# Basic Metrics - Finding minimum and maximum values
min_value = min(data_list)
max_value = max(data_list)

# Separating even and odd numbers for aggregation
even_numbers = [num for num in data_list if num % 2 == 0]
odd_numbers = [num for num in data_list if num % 2 != 0]

# Calculating averages for even and odd numbers
if even_numbers:
    avg_even = sum(even_numbers) / len(even_numbers)
else:
    avg_even = 0

if odd_numbers:
    avg_odd = sum(odd_numbers) / len(odd_numbers)
else:
    avg_odd = 0

# Console Output - Data Quality Report
print("\n--- Data Profiling Report ---")
print(f"Total records: {len(data_list)}")
print(f"Min value: {min_value}")
print(f"Max value: {max_value}")
print(f"Average of EVEN numbers: {avg_even:.1f}")
print(f"Average of ODD numbers: {avg_odd:.1f}")
print("-----------------------------")