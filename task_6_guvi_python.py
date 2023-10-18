
# 1) You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351]
# your task is to create two List one which have all the Even Numbers and another List which will have all the ODD numbers in it? 


# You can create two separate lists, one for even numbers and one for odd numbers, 
# by iterating through the given list and checking whether each number is even or odd. 

# Here's how you can do it in Python:

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = []
odd_numbers = []

for num in original_list:``
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# This code will result in two lists: even_numbers containing all the even numbers from the original list, and odd_numbers containing all the odd numbers.

print('****'*20)

# 2) Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] 
# your task is to Count all the Prime Numbers and create a new Python List which will contain all the Prime Numbers in it?


# You can count the prime numbers and create a new list containing only 
# the prime numbers from the given list using the following Python code:

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []
count = 0

for num in original_list:
    if is_prime(num):
        prime_numbers.append(num)
        count += 1

print("Prime Numbers:", prime_numbers)
print("Count of Prime Numbers:", count)
# This code will create a new list prime_numbers containing all 
# the prime numbers from the original list and also count the prime numbers in the list.

print('****'*20)

# 3) Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] 
# Find out how many numbers are there in the given Python List which are Happy Numbers?


# A happy number is a number which, when repeatedly replaced by the sum of the squares of its digits,
#  eventually reaches the number 1. If a number is not a happy number, the process will repeat in a cycle that does not include 1.
#  You can check if a number is a happy number using a function like this:

def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in original_list if is_happy_number(num)]
count = len(happy_numbers)

print("Happy Numbers:", happy_numbers)
print("Count of Happy Numbers:", count)
# This code will find and count the happy numbers in the given list and create a new list happy_numbers 
# containing those happy numbers.

print('****'*20)


# 4) Write a python program to find the sum of the first and last digit of an integer?


# You can find the sum of the first and last digits of an integer in Python using the following program:

# Function to find the sum of the first and last digit of an integer
def sum_of_first_and_last_digit(number):
    # Convert the integer to a string to easily access its digits
    number_str = str(number)

    # Check if the input is a single-digit number
    if len(number_str) == 1:
        return 2 * number  # The sum of the first and last digit is 2 times the number itself

    # Calculate the sum of the first and last digits
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    return first_digit + last_digit

# Input from the user
try:
    number = int(input("Enter an integer: "))
    result = sum_of_first_and_last_digit(number)
    print("Sum of the first and last digit:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# This program defines a function sum_of_first_and_last_digit 
# that takes an integer as input, converts it to a string to access its digits,
# and then calculates the sum of the first and last digits. 
# It also handles single-digit numbers by doubling 
# the number itself, as both the first and last digits are the same in this case.

print('****'*20)

# 5) You have been given a list of N integers which represents the number of Mangoes in a bag. Each bag has a variable number of Mangoes. 
# There are M students in a Guvi class, your task is to distribute the Mangoes in such a way that each student gets one Bag.
# The difference between the number of Mangoes in a bag with maximum Mangoes and Bag with minimum Mangoes given to the student is minimum ?

# To distribute the mangoes in a way that minimizes the difference b/w 
# the bag with the maximum number of mangoes and the bag with the minimum number of mangoes given to the students, you can follow these steps in Python:

# Sort the list of mangoes in ascending order.
# Calculate the minimum difference by subtracting the number of mangoes in the bag with the lowest count from the bag with the highest count.
# Create a sublist of bags with the minimum number of mangoes by taking the first M bags from the sorted list.

def distribute_mangoes(mangoes, students):
    if len(mangoes) < students:
        return "Not enough bags for all students"
    
    mangoes.sort()  # Sort the list of mangoes in ascending order
    min_diff = float('inf')  # Initialize the minimum difference to positive infinity

    for i in range(len(mangoes) - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        if diff < min_diff:
            min_diff = diff
            result = mangoes[i:i + students]

    return result, min_diff

# Example usage:
bag_of_mangoes = [10, 7, 15, 9, 12, 3, 5]
students = 3
distribution, min_difference = distribute_mangoes(bag_of_mangoes, students)

if isinstance(distribution, str):
    print(distribution)
else:
    print("Distribution of bags:", distribution)
    print("Minimum difference:", min_difference)
    
# This program sorts the list of mangoes, then iterates through it to find the subsequence of bags
# that results in the minimum difference and assigns those bags to students.

print('****'*20)

# 6) You have been given three lists. Your task is to find the duplicates in the three lists. 
# Write a python program for the same. You can use your own python lists?

# You can find the duplicates in three lists by first converting each list to a set and then finding t
# he intersection of the sets, which will contain the common elements (duplicates). 


# Here's a Python program

# Sample lists (you can use your own lists)
list1 = [1, 2, 3, 4, 5, 2, 7]
list2 = [4, 5, 6, 7, 8, 2]
list3 = [7, 8, 9, 10, 2, 5]

# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find the duplicates by taking the intersection of the sets
duplicates = set1.intersection(set2, set3)

# Convert the result back to a list (if needed)
duplicate_list = list(duplicates)

# Print the duplicates
if len(duplicates) > 0:
    print("Duplicate elements:", duplicate_list)
else:
    print("No duplicates found.")
# In this program, we convert each list to a set (to remove duplicates within each list),
# and then we find the intersection of the three sets, which will give you the common elements (duplicates) among the three lists.

print('****'*20)


# 7) Write a python program to find the first non - repeating elements in a given list of integers?

# You can find the first non-repeating element in a list of integers using a Python program by iterating through 
# the list and keeping track of the frequency of each element. 

# Here's a program

def find_first_non_repeating_element(numbers):
    element_count = {}

    # Count the frequency of each element
    for num in numbers:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Find the first non-repeating element
    for num in numbers:
        if element_count[num] == 1:
            return num

    # If there are no non-repeating elements, return None
    return None

# Example usage:
numbers = [4, 5, 6, 4, 7, 5, 8]
result = find_first_non_repeating_element(numbers)

if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found in the list.")
# In this program, we use a dictionary (element_count) to count the frequency of each element in the list. Then,
# we iterate through the list again and find the first element with a count of 1, which indicates that it is a non-repeating element.

print('****'*20)

# 8) Write a python program to find the minimum element in a rated and sorted list?


# To find the minimum element in a sorted list, you can simply access the first element of the list, 
# as the minimum element will always be the first element in a sorted list. 

# Here's a Python program

def find_minimum_element(sorted_list):
    if len(sorted_list) > 0:
        return sorted_list[0]
    else:
        return None

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7]

minimum_element = find_minimum_element(sorted_list)

if minimum_element is not None:
    print("The minimum element is:", minimum_element)
else:
    print("The list is empty.")
# In this program, we check if the list is not empty and then access the first element using sorted_list[0] 
# to find the minimum element in the sorted list.

print('****'*20)

# 9) You have been given a Python list [10,20,30,9] and a value of 59. 
# Write a python program to find the triplet in the list whose sum is equal to the given value?

# You can find the triplet in a list whose sum is equal to the given value by using a nested loop to iterate through 
# all possible combinations of triplets and checking if the sum of each triplet matches the given value.

# Here's a Python program

def find_triplet_with_sum(arr, target_sum):
    n = len(arr)
    if n < 3:
        return None

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    return [arr[i], arr[j], arr[k]]

    return None

# Example usage:
input_list = [10, 20, 30, 9]
target_sum = 59

result = find_triplet_with_sum(input_list, target_sum)

if result is not None:
    print("Triplet with sum", target_sum, "is:", result)
else:
    print("No such triplet found.")
# This program checks all combinations of triplets by using three nested loops and returns 
# the first triplet that has a sum equal to the given value.

print('****'*20)


# 10) Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with sum equal to Zero?


# You can use a Python program to find if there is a sub-list with a sum equal to zero by iterating through 
# the list and keeping track of the running sum. If at any point the running sum repeats, it means there's a sub-list with a sum of zero.


#  Here's a sample program

def has_sublist_with_zero_sum(lst):
    sum_set = set()
    current_sum = 0

    for num in lst:
        current_sum += num

        if current_sum == 0 or current_sum in sum_set:
            return True
        sum_set.add(current_sum)

    return False

# Example list
my_list = [4, 2, -3, 1, 6]

if has_sublist_with_zero_sum(my_list):
    print("There is a sub-list with a sum equal to zero.")
else:
    print("There is no sub-list with a sum equal to zero.")
# This program defines a function has_sublist_with_zero_sum that iterates through t
# he input list and uses a set to keep track of the running sum. If it encounters a sum of zero or a sum that has 
# already been seen (indicating the presence of a sub-list with a zero sum), it returns True. Otherwise, 
# it returns False.