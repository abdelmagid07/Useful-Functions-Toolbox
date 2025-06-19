from datetime import datetime

# Converts standard metric values to American units
def American_unit_converter(conversion, value):
    '''
    Converts from metric to American units.
    - 1: Celsius to Fahrenheit
    - 2: Kilometers to Miles
    - 3: Kilograms to Pounds
    '''
    print("American Unit Converter")

    if int(conversion) == 1:
        return ((value * 9 / 5) + 32)
    elif int(conversion) == 2:
        return (value / 1.6)
    elif int(conversion) == 3:
        return (value * 2.2)
    else:
        print("Invalid conversion code")

# Counts the number of words in user input
def Word_counter():
    print("Word Counter")
    text = input('Enter the text you want analyzed: ')
    words = text.split()
    word_count = len(words)
    print('Word Count:', word_count)

# Calculates the mean (average) of a list of numbers entered by the user
def mean():
    print("Mean Calculator")
    numbers = input("Enter numbers separated by spaces: ")
    split_numbers = numbers.split()
    nums = [float(i) for i in split_numbers]
    result = sum(nums) / len(nums)
    print('Mean:', result)

# Checks if a password meets basic security standards
def validate_password(password):
    '''
    Checks if a password:
    - Is at least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one special character
    '''
    has_upper = False
    has_special = False
    special = "!@#$%^&*_-"

    for char in password:
        if char.isupper():
            has_upper = True
        if char in special:
            has_special = True

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    elif not has_upper:
        print("Password must contain at least one uppercase letter.")
        return False
    elif not has_special:
        print("Password must contain at least one special character.")
        return False
    else:
        print("Password is valid.")
        return True

# Calculates factorial of a user-entered integer
def factorial():
    n = int(input('Enter an integer: '))
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(n, "Factorial is:", result)

# Calculates current age based on user-entered birth date
def calculate_age():
    current = datetime.now()
    current_year = current.year
    current_month = current.month
    current_day = current.day

    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    age = current_year - birth_year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1

    print("You are", age, "years old.")
    return age
