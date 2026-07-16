import random


def create_plates_stock():
    plates_stock = []
    for i in range(1, 11):
        plates_stock.append(i)
        plates_stock.append(i)
    for i in (25, 50, 75, 100):
        plates_stock.append(i)
    return plates_stock


def choose_target_number():
    number = random.randint(101, 999)
    return number


def choose_six_plates(plates_stock):
    plates = random.sample(plates_stock, 6)
    return plates


def calculate(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2
    return None


def ask_operation():
    choice = input("Choisissez un operation: (+, -, * ou /)")
    while choice not in ("+", "-", "*", "/"):
        print("Choisissez une des opérations proposées")
        choice = input("Choisissez un operation: (+, -, * ou /)")
    return choice


def choose_play_numbers(plates_list):

    number1 = int(input(f"Choisissez un nombre parmi les nombres disponibles : {plates_list}"))
    while number1 not in plates_list:
        print("Le nombre choisi ne fait pas parti de la liste.")
        number1 = int(input(f"Choisissez un nombre parmi les nombres disponibles : {plates_list}"))
    plates_list.remove(number1)

    number2 = int(input(f"Choisissez un deuxième nombre parmi les nombres disponibles : {plates_list}"))
    while number2 not in plates_list:
        print("Le nombre choisi ne fait pas parti de la liste.")
        number2 = int(input(f"Choisissez un nombre parmi les nombres disponibles : {plates_list}"))
    plates_list.remove(number2)
    return number1, number2


initial_plates_stock = create_plates_stock()
target_number = choose_target_number()
plates_game = choose_six_plates(initial_plates_stock)
print(initial_plates_stock)
print(target_number)
print(plates_game)

choice_operation = ask_operation()
print(choice_operation)
choice_numbers = choose_play_numbers(plates_game)
print(choice_numbers)
