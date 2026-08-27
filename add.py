import sys


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    # Check if the user provided both numbers
    if len(sys.argv) < 3:
        print("Error: Please provide two numbers.")
        print("Usage: python add.py <number1> <number2>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    result = add_numbers(num1, num2)

    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum          : {result}")
