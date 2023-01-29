import random


def get_number():
    """
    User give the number from 1 to 49
    :return: int
    """
    while True:
        try:
            user_choice = int(input("Give the number from 1 to 49: "))
            break
        except ValueError:
            print("It's not a number")
    return user_choice


def get_numbers():
    """
    Check that the user choose 6 numbers and validation of the number
    :return: list
    """
    numbers = []
    while len(numbers) < 6:
        number = get_number()
        if number not in numbers and 0 < number <= 49:
            numbers.append(number)
    return sorted(numbers)


def random_numbers():
    """
    randomize the list with the numbers and slice the six of them
    :return: list
    """
    computer_numbers = list(range(1, 49))
    random.shuffle(computer_numbers)
    return computer_numbers[:6]


def lotto():
    """
    Main code of the program
    """
    user_numbers = get_numbers()
    print(f"Your numbers: {user_numbers}")

    computer_numbers = random_numbers()
    print(f"Winning numbers: {computer_numbers}")

    hits = 0
    for number in user_numbers:
        if number in random_numbers():
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 or hits == 0 else 'numbers'}!")


if __name__ == '__main__':
    lotto()