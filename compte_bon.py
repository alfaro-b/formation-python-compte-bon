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
    plates = []
    for _ in range(6):
        plates.append(random.choice(plates_stock))
    return plates




initial_plates_stock = create_plates_stock()
target_number = choose_target_number()
plates_game = choose_six_plates(initial_plates_stock)

print(initial_plates_stock)
print(target_number)
print(plates_game)
