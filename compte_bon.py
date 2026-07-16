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
    number = random.randint(101, 1000)
    return number


initial_plates_stock = create_plates_stock()
target_number = choose_target_number()

print(initial_plates_stock)
print(target_number)
