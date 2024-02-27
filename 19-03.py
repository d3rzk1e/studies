# Создайте класс Car, который будет содержать информацию об
# автомобиле. С помощью механизма наследования, реализуйте класс
# ElectricCar (содержит информацию об электроавтомобиле). Каждый из
# классов должен содержать необходимые для работы методы.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Автомобиль запущен.")

    def stop(self):
        print("Автомобиль остановлен.")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print("Аккумулятор заряжается.")

    def start(self):
        print("Электромобиль запущен.")

    def stop(self):
        print("Электромобиль остановлен.")


car1 = Car("BMW", "X5", 2022)
car1.start()  # Вывод: Автомобиль запущен.

car2 = ElectricCar("Tesla", "Model S", 2023, 100)
car2.start()  # Вывод: Электромобиль запущен.
car2.charge()  # Вывод: Аккумулятор заряжается.

# Создайте класс Device, который будет содержать информацию об
# электронном устройстве. С помощью механизма наследования, реализуйте
# класс MobilePhone (содержит информацию об мобильном телефоне). Каждый
# из классов должен содержать необходимые для работы методы.


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print("Устройство включено.")

    def turn_off(self):
        print("Устройство выключено.")


class MobilePhone(Device):
    def __init__(self, brand, model, operating_system):
        super().__init__(brand, model)
        self.operating_system = operating_system

    def make_call(self, number):
        print("Вызов на номер", number)

    def send_message(self, number, message):
        print("Отправка сообщения на номер", number, "с текстом:", message)


device1 = Device("Samsung", "Galaxy Tab")
device1.turn_on()  # Вывод: Устройство включено.

phone1 = MobilePhone("Apple", "iPhone 12", "iOS")
phone1.turn_on()  # Вывод: Устройство включено.
phone1.make_call("123456789")  # Вывод: Вызов на номер 123456789
# Вывод: Отправка сообщения на номер 987654321 с текстом: Привет!
phone1.send_message("987654321", "Привет!")
