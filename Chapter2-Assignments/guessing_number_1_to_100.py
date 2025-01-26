import random

def get_user_input(request):
    return input(request)

def is_valid_input_number(user_input):
    return user_input.isdigit() and 1 <= int(user_input) <= 100

def display_invalid_input_message():
    print("The input provided is invalid. Please enter a number between 1 and 100: ")

def convert_input_to_int(user_input):
    return int(user_input)

def compare_user_input(user_input, expected_number):
    if user_input < expected_number:
        print("Too low. Guess again.")
    elif user_input > expected_number:
        print("Too high. Guess again.")
    else:
        print(f"You guessed it! The number was {expected_number}.")

def generate_random_number():
    return random.randint(1, 100)


def main():
    expected_number = generate_random_number()
    user_input_count = 0
    guessed_correct = False

    while not guessed_correct:
        user_input = get_user_input("Guess a number between 1 and 100: ")

        if not is_valid_input_number(user_input):
            display_invalid_input_message()
            continue

        user_guess = convert_input_to_int(user_input)
        user_input_count += 1

        if user_guess == expected_number:
            print(f"You guessed it in {user_input_count} guesses!")
            guessed_correct = True
        else:
            compare_user_input(user_guess, expected_number)

if __name__ == "__main__":
    main()