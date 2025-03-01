class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        return f"Store: {self.name}, Address: {self.address}, Items: {self.items}"

# Создание магазинов
store1 = Store("Fresh Market", "123 Main St")
store2 = Store("Organic Foods", "456 Green Ave")
store3 = Store("Budget Mart", "789 Economy Rd")

# Добавление товаров
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("milk", 1.2)
store2.add_item("bread", 1.5)
store3.add_item("eggs", 2.0)
store3.add_item("cheese", 3.5)

# Обновление и удаление товаров
store1.update_price("apples", 0.6)
store2.remove_item("bread")

# Вывод информации о магазинах
print("\nStores Information:")
print(store1)
print(store2)
print(store3)

