# EvenOddChecker.py

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def single_number_check():
    try:
        num = int(input("Enter a number to check if it is even or odd: "))
        result = check_even_odd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def list_number_check():
    try:
        nums_input = input("Enter a list of numbers separated by spaces: ")
        nums = [int(n) for n in nums_input.split()]
        
        for n in nums:
            result = check_even_odd(n)
            print(f"The number {n} is {result}.")
    except ValueError:
        print("Invalid input. Please enter only integers.")

if __name__ == "__main__":
    single_number_check()
    print("\nNow let's check a list of numbers.")
    list_number_check()
