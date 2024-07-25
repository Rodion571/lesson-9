# Task 1
import string
def calculate_tax(income, tax_rate):
    tax = income * (tax_rate / 100)
    return tax
income = 50000
tax_rate = 20
tax = calculate_tax(income, tax_rate)
print(f"Amount of tax to be paid: {tax}")
# Task 2
import string
import random
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
print(generate_password())
# Task 3
import math
def is_palindrome(number):
    return str(number) == str(number)[::-1]
def largest_palindrome_product():
    largest_palindrome = 0
    factors = (0, 0)
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                factors = (i, j)
    return largest_palindrome, factors
palindrome, (factor1, factor2) = largest_palindrome_product()
print(f"The largest palindrome is {palindrome}, which is the product of {factor1} and {factor2}.")
# Task 4
# Task 5