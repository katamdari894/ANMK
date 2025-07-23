import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    """
    if num < 0:
        return False
    
    original_num = num
    sum_of_factorials = 0
    
    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
        
    return sum_of_factorials == original_num

def print_strong_numbers_in_range(start, end):
    """
    Prints all strong numbers within a specified range.
    """
    print(f"Strong numbers from {start} to {end}:")
    found_strong_numbers = False
    for i in range(start, end + 1):
        if is_strong_number(i):
            print(i)
            found_strong_numbers = True
            
    if not found_strong_numbers:
        print("No strong numbers found in this range.")

# Call the function to print strong numbers from 1 to 5000
print_strong_numbers_in_range(1, 5000)