# Function to check if a number is odd
def is_odd(num):
    return num % 2 != 0

# Function to print all odd numbers in a range
def print_odd_numbers(start, end):
    print(f"Odd numbers between {start} and {end}:")
    for i in range(start, end + 1):
        if is_odd(i):
            print(i, end=" ")
    print()  # new line

# --- Main Program ---
print("1. Check if a number is odd")
print("2. Print all odd numbers in a range")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    num = int(input("Enter a number: "))
    if is_odd(num):
        print(num, "is an odd number")
    else:
        print(num, "is not an odd number")

elif choice == 2:
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print_odd_numbers(start, end)

else:
    print("Invalid choice!")
