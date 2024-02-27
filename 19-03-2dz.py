# Создайте класс Human, который будет содержать информацию о
# человеке. С помощью механизма наследования, реализуйте класс Builder
# (содержит информацию о строителе), класс Sailor (содержит информацию о
# моряке), класс Pilot (содержит информацию о летчике). Каждый из классов
# должен содержать необходимые для работы методы.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Привет, меня зовут", self.name, "и мне", self.age, "лет.")


class Builder(Human):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def build(self):
        print("Я строитель", self.name,
              "и я специализируюсь на", self.specialization)


class Sailor(Human):
    def __init__(self, name, age, ship):
        super().__init__(name, age)
        self.ship = ship

    def sail(self):
        print("Я моряк", self.name, "и я работаю на корабле", self.ship)


class Pilot(Human):
    def __init__(self, name, age, aircraft):
        super().__init__(name, age)
        self.aircraft = aircraft

    def fly(self):
        print("Я летчик", self.name, "и я управляю самолетом", self.aircraft)


human1 = Human("Иван", 30)
human1.speak()  # Вывод: Привет, меня зовут Иван и мне 30 лет.

builder1 = Builder("Петр", 35, "строительные конструкции")
builder1.speak()  # Вывод: Привет, меня зовут Петр и мне 35 лет.
# Вывод: Я строитель Петр и я специализируюсь на строительные конструкции.
builder1.build()

sailor1 = Sailor("Алексей", 25, "Titanic")
sailor1.speak()  # Вывод: Привет, меня зовут Алексей и мне 25 лет.
sailor1.sail()  # Вывод: Я моряк Алексей и я работаю на корабле Titanic.

pilot1 = Pilot("Михаил", 40, "Boeing 747")
pilot1.speak()  # Вывод: Привет, меня зовут Михаил и мне 40 лет.
pilot1.fly()  # Вывод: Я летчик Михаил и я управляю самолетом Boeing 747.

# Создайте класс Passport (паспорт), который будет содержать
# паспортную информацию о гражданине заданной страны. С помощью
# механизма наследования, реализуйте класс ForeignPassport (загран.паспорт)
# производный от Passport. Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер заграничного
# паспорта


class Passport:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number


class ForeignPassport(Passport):
    def __init__(self, name, passport_number, visa_data, foreign_passport_number):
        super().__init__(name, passport_number)
        self.visa_data = visa_data
        self.foreign_passport_number = foreign_passport_number


passport1 = Passport("Иванов Иван", "123456789")
print(passport1.name)  # Вывод: Иванов Иван
print(passport1.passport_number)  # Вывод: 123456789

foreign_passport1 = ForeignPassport(
    "Петров Петр", "987654321", "Виза в США", "ABC123")
print(foreign_passport1.name)  # Вывод: Петров Петр
print(foreign_passport1.passport_number)  # Вывод: 987654321
print(foreign_passport1.visa_data)  # Вывод: Виза в США
print(foreign_passport1.foreign_passport_number)  # Вывод: ABC123
