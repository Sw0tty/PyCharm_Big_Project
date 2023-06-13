class RetailItem:

    def __init__(self, name, value, price):
        self.name = name
        self.value = value
        self.price = price


class CashRegister:

    retail_items = []

    def warehouse_status(self):
        if not self.retail_items:
            return "Товар не выбран"
        return False

    @staticmethod
    def purchase_item():
        while True:
            while True:
                name = input("Наименование товара: ")
                if name.isspace() or not name:
                    pass
                elif name.isalpha():
                    break
                elif ' ' in name and name.replace(' ', '').isalpha():
                    break
                print("Принимаются только строки!")
            while True:
                value = input("Количество товара: ")
                if not value.isdigit() or value == '0':
                    print("Принимаются только целые числа!")
                    continue
                value = int(value)
                break
            while True:
                try:
                    price = float(input("Цена товара: "))
                    if price <= 0:
                        raise ValueError
                except ValueError:
                    print("Принимаются только числа, которые больше нуля!")
                else:
                    price = float(price)
                    break
            item = RetailItem(name, value, price)
            purchase.retail_items.append(item)
            print("Товар успешно добавлен к покупке")
            if input("Добавить еще товар к покупке? (yes - да)") != 'yes':
                break
            else:
                continue

    def get_total(self):
        if not self.warehouse_status():
            total_price = 0
            for i in self.retail_items:
                total_price += i.price*i.value
            return f"Общая стоимоть всех товаров составляет: ${total_price}"
        return self.warehouse_status()

    def show_items(self):
        if not self.warehouse_status():
            for i in self.retail_items:
                print(f"--К покупке следующие товары--\nНаименование: {i.name}\n"
                      f"Количество на складе: {i.value}\nЦена за штуку: ${round(i.price, 2)}\n")
        else:
            print(self.warehouse_status())

    def clear(self):
        self.retail_items.clear()


if __name__ == '__main__':
    purchase = CashRegister()
    print(purchase.show_items())
    purchase.purchase_item()
    purchase.show_items()
    print(purchase.get_total())
