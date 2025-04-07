print("You are to enter 2 numbers which will be divided")
print("Enter \"q\" to quit")

while True:
    first_number = input("Enter first number: ")
    if first_number == "q":
        break
    second_number = input("Enter second number: ")
    if second_number == "q":
        break
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    except ValueError:
        print("Please enter valid numbers")
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")