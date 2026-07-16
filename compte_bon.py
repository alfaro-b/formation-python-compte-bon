def create_plates_stock():
    plates_stock = []
    for i in range(1, 11):
        plates_stock.append(i)
        plates_stock.append(i)
    for i in (25, 50, 75, 100):
        plates_stock.append(i)
    return plates_stock


initial_plates_stock = create_plates_stock()

print(initial_plates_stock)
