def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")
#Added this section to showcase improved error handling
my_string_list = [1,2,'a',4]
try:
    average_string = calculate_average(my_string_list)
    print(f"The average is: {average_string}")
except TypeError as e:
    print(f"Error: {e}") 