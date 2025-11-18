numbers = []
while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer or 'done'.")

total_sum = sum(numbers)
print(f"The sum of the integers is: {total_sum}")