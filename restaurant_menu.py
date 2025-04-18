class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_info(self):
        return f"{self.name} - {self.description} - {self.price} so'm"


class Starter(Dish):
    def __init__(self, name, description, price):
        super().__init__(name, description, price)


class MainCourse(Dish):
    def __init__(self, name, description, price, vegetarian=False, gluten_free=False):
        super().__init__(name, description, price)
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free

    def get_info(self):
        info = super().get_info()
        if self.vegetarian:
            info += " (Vegetarian)"
        if self.gluten_free:
            info += " (Gluten-Free)"
        return info


class Dessert(Dish):
    def __init__(self, name, description, price, vegetarian=False, gluten_free=False):
        super().__init__(name, description, price)
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free

    def get_info(self):
        info = super().get_info()
        if self.vegetarian:
            info += " (Vegetarian)"
        if self.gluten_free:
            info += " (Gluten-Free)"
        return info


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"{dish.name} menyuga qo‘shildi.")

    def remove_dish(self, name):
        for dish in self.dishes:
            if dish.name.lower() == name.lower():
                self.dishes.remove(dish)
                print(f"{name} menyudan o‘chirildi.")
                return
        print(f"{name} menyuda topilmadi.")

    def show_menu(self):
        if not self.dishes:
            print("Menyuda hozircha taomlar yo‘q.")
        else:
            for dish in self.dishes:
                print(dish.get_info())

    def find_dish(self, name):
        for dish in self.dishes:
            if dish.name.lower() == name.lower():
                return dish
        return None


class Order:
    def __init__(self):
        self.ordered_dishes = []

    def add_to_order(self, dish):
        self.ordered_dishes.append(dish)

    def calculate_total(self):
        total = sum(dish.price for dish in self.ordered_dishes)
        if total > 100000:
            total *= 0.9
        return total


menu = Menu()
order = Order()

while True:
    print("\n1. Yangi taom qo‘shish")
    print("2. Taomni o‘chirish")
    print("3. Menyuni ko‘rish")
    print("4. Buyurtma qilish")
    print("5. Chiqish")

    choice = input("Tanlovni kiriting (1-5): ")

    if choice == "1":
        name = input("Taom nomi: ")
        description = input("Tavsifi: ")
        try:
            price = float(input("Narxi: "))
        except ValueError:
            print("Narx noto‘g‘ri formatda.")
            continue

        dish_type = input("Turi (starter, asosiy, desert): ").lower()

        if dish_type == "starter":
            dish = Starter(name, description, price)
        elif dish_type == "asosiy":
            veg = input("Vegetarian? (ha/yo‘q): ").lower() == "ha"
            gluten = input("Gluten-free? (ha/yo‘q): ").lower() == "ha"
            dish = MainCourse(name, description, price, veg, gluten)
        elif dish_type == "desert":
            veg = input("Vegetarian? (ha/yo‘q): ").lower() == "ha"
            gluten = input("Gluten-free? (ha/yo‘q): ").lower() == "ha"
            dish = Dessert(name, description, price, veg, gluten)
        else:
            print("Noto‘g‘ri tur.")
            continue

        menu.add_dish(dish)

    elif choice == "2":
        name = input("O‘chirmoqchi bo‘lgan taom nomi: ")
        menu.remove_dish(name)

    elif choice == "3":
        menu.show_menu()

    elif choice == "4":
        while True:
            menu.show_menu()
            name = input("Buyurtma qilmoqchi bo‘lgan taom nomi (yoki 'stop'): ")
            if name.lower() == "stop":
                break
            dish = menu.find_dish(name)
            if dish:
                order.add_to_order(dish)
                print(f"{dish.name} buyurtmaga qo‘shildi.")
            else:
                print("Taom topilmadi.")

        total = order.calculate_total()
        print(f"Buyurtma yakuni: {total} so‘m")

    elif choice == "5":
        print("Dastur tugatildi.")
        break

    else:
        print("Noto‘g‘ri tanlov.")
