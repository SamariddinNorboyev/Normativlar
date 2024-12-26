from abc import ABC, abstractmethod

class Computer(ABC):
    total_computers = 0
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
        Computer.total_computers += 1

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def get_total_computer(cls):
        return Computer.total_computers

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
            return True
        if value < 0 or value == 0:
            print("Xato qiymat kiritildi!")
            return False

    def __gt__(self, other):
        if isinstance(other, Computer):
            return self.__price > other.__price
        else:
            print("Xato qiymat kiritildi!")
            return False


class Monoblock(Computer):
    def __init__(self, brand, model, year, price, screen_size):
        super().__init__(brand, model, year, price)
        self.screen_size = screen_size

    def display_info(self):
        return f"Brand - {self.brand}, Model - {self.model}, Year - {self.year}, Price - {self.price}, ScreenSize - {self.screen_size}"

    def __repr__(self):
        return self.display_info()

class Notebook(Computer):
    def __init__(self, brand, model, year, price, battery_life):
        super().__init__(brand, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        return f"Brand - {self.brand}, Model - {self.model}, Year - {self.year}, Price - {self.price}, BatteryLife - {self.battery_life}"

    def __repr__(self):
        return self.display_info()

class Factory:
    factories_number = 0
    def __init__(self, name):
        self.name = name
        self.list_products = []
        Factory.factories_number += 1


    def add_product(self, a):
        if isinstance(a, Computer):
            self.list_products.append(a)
            return True
        else:
            print(f"{a} Computer emas!")
            return False





    def show_products(self):
        for i in self.list_products:
            print(i.display_info())

    @classmethod
    def get_factories(cls):
        return Factory.factories_number

monoblock1 = Monoblock("HP", "Thunder", "2022", 1299, 27)
monoblock2 = Monoblock("LENOVO", "Blunder", "2020", 1199, 26)
monoblock3 = Monoblock("ASUS", "G16", "2019", 1099, 25)
monoblock4 = Monoblock("AURUS", "T45", "2018", 999, 22)
notebook1 = Notebook("Mackbook", "Air", "2023", 1550, 14)
notebook2 = Notebook("Lenovo", "IdeaPad3", "2022", 1340, 15)
notebook3 = Notebook("HP", "Pavilion", "2021", 1670, 16)
notebook4 = Notebook("ASUS", "ROG", "2020", 1220, 17)
notebook5 = Notebook("Acer", "Predator", "2019", 1110, 18)

zavod1 = Factory("Samarqand")
zavod1.add_product(monoblock1)
zavod1.add_product(notebook1)
zavod2 = Factory("Toshkent")
zavod2.add_product(monoblock2)
zavod2.add_product(monoblock3)
zavod2.add_product(monoblock4)
zavod2.add_product(notebook2)
zavod2.add_product(notebook3)
zavod2.add_product(notebook4)
zavod2.add_product(notebook5)

zavod1.show_products()
print(Computer.get_total_computer())