import random


def create_plates_stock():
    """
    Constitue le stock initial des 24 plaques de nombre.
    :return: Liste des 24 plaques de nombre.
    """
    plates_stock = []
    for i in range(1, 11):
        plates_stock.append(i)
        plates_stock.append(i)
    for i in (25, 50, 75, 100):
        plates_stock.append(i)
    return plates_stock


def choose_target_number():
    """
    Tire au sort un nombre à obtenir.
    :return: Un nombre entier entre 101 et 999.
    """
    number = random.randint(101, 999)
    return number


def choose_six_plates(plates_stock):
    """
    Tire au sort 6 plaques de nombre parmi les 24 plaques disponibles.
    :param plates_stock: Liste des 24 plaques initiales.
    :return: Liste de six plaques disponibles pour jouer.
    """
    plates = random.sample(plates_stock, 6)
    return plates


def calculate(number1, number2, operation):
    """
    Calcule le résultat d'une opération.
    :param number1: Un nombre entier
    :param number2: Un nombre entier
    :param operation: Une opération (+, -, * ou /)
    :return: Retourne le résultat de l'opération.
    """
    # Addition
    if operation == "+":
        return number1 + number2
    # Soustraction
    elif operation == "-":
        if number1 > number2:
            return number1 - number2
    # Multiplication
    elif operation == "*":
        return number1 * number2
    # Division
    elif operation == "/" and number2 != 0 and number1 % number2 == 0:
        return number1 // number2
    return None


def ask_operation():
    """
    Demande à l'utilisateur de choisir une opération (+, -, * ou /).
    :return: Retourne l'opération choisie
    """
    choice = input("Choisissez un operation: (+, -, * ou /) : ")
    while choice not in ("+", "-", "*", "/"):
        print("Choisissez une des opérations proposées! ")
        choice = input("Choisissez un operation: (+, -, * ou /) : ")
    return choice


def choose_play_numbers(plates_list):
    """
    Demande à l'utilisateur de choisir deux nombres parmi ceux disponibles.
    :param plates_list: Liste des nombres disponibles.
    :return: Les deux nombres choisis.
    """

    number1 = int(input(f"Choisissez un nombre parmi les nombres disponibles {format_numbers(plates_list)} : "))
    while number1 not in plates_list:
        print("Le nombre choisi ne fait pas parti de la liste.")
        number1 = int(input(f"Choisissez un nombre parmi les nombres disponibles {format_numbers(plates_list)} : "))

    number2 = int(input(f"Choisissez un 2ème nombre parmi les nombres disponibles {format_numbers(plates_list)} : "))
    while (
        number2 not in plates_list
        or (number1 == number2 and plates_list.count(number1) < 2)
        # évite que l'utilisateur choisi deux fois le même nombre s'il n'était présent qu'une fois
    ):
        if number2 not in plates_list:
            print("Le nombre choisi ne fait pas parti de la liste.")
        else:
            print(
                f"Il n'y qu'un seul exemplaire du nombre {number1}. "
                "Choisissez un autre nombre. "
            )
        number2 = int(input(f"Choisissez un 2ème nombre parmi les nombres disponibles {format_numbers(plates_list)} : "))
    return number1, number2


def do_operation(number1, number2, operation, numbers_list):
    """
    Fait le calcule entre les deux nombres choisis et l'opération choisie.
    :param number1: Premier nombre entier choisi
    :param number2: Deuxième nombre entier choisi
    :param operation: Opération choisie
    :param numbers_list: Liste de nombres
    :return: Le nouveau nombre qui est le résultat de l'opération.
    """
    result_number = calculate(number1, number2, operation)
    if result_number is None:
        return None
    numbers_list.remove(number1)
    numbers_list.remove(number2)
    numbers_list.append(result_number)
    return result_number


def user_stop():
    """
    Demande à l'utilisateur s'il souhaite arrêter le jeu.
    :return: Retourne True s'il veut arrêter.
    """
    choice_stop = input("Voulez-vous arrêter? o/n : ").lower()
    while choice_stop not in ("o", "n"):
        choice_stop = input("Voulez-vous arrêter? o/n : ").lower()
    if choice_stop == "o":
        return True
    else:
        return False


def format_numbers(numbers_list):
    """
    Permet de formater une liste de nombre pour avoir un affichage des nombres séparés par un tiret.
    :param numbers_list: Liste de nombres
    :return: Affichage des nombres séparés par un tiret.
    """
    return " - ".join(map(str, numbers_list))


def display_result(numbers_list, desired_number):
    """
    Affiche le résultat final quand le jeu s'arrête.
    :param numbers_list: Liste de nombres
    :param desired_number: Nombre cible
    :return: None
    """
    nearest_number = numbers_list[0]
    smallest_difference = abs(desired_number - nearest_number)  # abs permet d'avoir valeur absolue
    for number in numbers_list:
        difference = abs(desired_number - number)
        if difference < smallest_difference:
            nearest_number = number
            smallest_difference = difference

    if smallest_difference == 0:
        print(f"Le compte est bon. Vous avez trouvé le nombre exact {desired_number}. ")
    else:
        print(f"Le nombre le plus proche obtenu est {nearest_number}. ")
        print(f"Il est à {smallest_difference} du nombre cible {desired_number}. ")


if __name__ == "__main__":

    initial_plates_stock = create_plates_stock()
    target_number = choose_target_number()
    available_numbers = choose_six_plates(initial_plates_stock)
    print(f"Plaques disponibles en début de jeu : {format_numbers(available_numbers)}")
    print(f"Nombre visé : {target_number}")
    print(f"Nombres disponibles : {format_numbers(available_numbers)}")

    while len(available_numbers) > 1 and not user_stop():

        choice_operation = ask_operation()
        print(f"opération choisie : {choice_operation}")

        choice_numbers = choose_play_numbers(available_numbers)
        print(f"Nombres choisis pour l'opération : {format_numbers(choice_numbers)}")

        new_number = do_operation(choice_numbers[0], choice_numbers[1], choice_operation, available_numbers)
        if new_number is None:
            print("C'est opération n'est pas possible")
        else:
            print(f"Nombre obtenu : {new_number}")
        print(f"Nombres disponibles : {format_numbers(available_numbers)}")
        print(f"Nombre à obtenir : {target_number}")

    display_result(available_numbers, target_number)
