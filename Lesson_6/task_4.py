# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        print(f"Машина повернула {direction}!")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        self.max_speed = 60
        if self.speed > self.max_speed:
            print(f"Скороть выше {self.max_speed} км/ч! Сбавьте скорость на {self.speed - self.max_speed} км/ч!!!")
        else:
            print(f"Скорость автомобиля типа TownCar {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        self.max_speed = 40
        if self.speed > 40:
            print(f"Скороть выше {self.max_speed} км/ч! Сбавьте скорость на {self.speed - self.max_speed} км/ч!!!")
        else:
            print(f"Скорость автомобиля типа WorkCar {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

#Экземпляр класса Car
print("Класс Car")
car_1 = Car(100, "red", "mazda")
car_1.go()
print(f"Автомобиль {car_1.name} цветом {car_1.color} едет со скоростью {car_1.speed} км/ч. "
      f"{'Не является машиной полиции!' if car_1.is_police == False else 'Является машиной полиции!'}")
car_1.show_speed()
car_1.turn("налево")
car_1.stop()
print()

# Экземпляр класса TownCar
print("Класс TownCar")
car_2 = TownCar(70, "white", "toyota")
car_2.go()
print(f"Автомобиль {car_2.name} цветом {car_2.color} едет со скоростью {car_2.speed} км/ч. "
      f"{'Не является машиной полиции!' if car_2.is_police == False else 'Является машиной полиции!'}")
car_2.show_speed()
car_2.turn("налево")
car_2.stop()
print()

# Экземпляр класса SportCar
print("Класс SportCar")
car_3 = SportCar(170, "white", "toyota")
car_3.go()
print(f"Автомобиль {car_3.name} цветом {car_3.color} едет со скоростью {car_3.speed} км/ч. "
      f"{'Не является машиной полиции!' if car_3.is_police == False else 'Является машиной полиции!'}")
car_3.show_speed()
car_3.turn("направо")
car_3.stop()
print()


# Экземпляр класса WorkCar
print("Класс WorkCar")
car_4 = WorkCar(50, "white", "toyota")
car_4.go()
print(f"Автомобиль {car_4.name} цветом {car_4.color} едет со скоростью {car_4.speed} км/ч. "
      f"{'Не является машиной полиции!' if car_4.is_police == False else 'Является машиной полиции!'}")
car_4.show_speed()
car_4.turn("направо")
car_4.stop()
print()


# Экземпляр класса PoliceCar
print("Класс PoliceCar")
car_5 = PoliceCar(210, "white", "toyota")
car_5.go()
print(f"Автомобиль {car_5.name} цветом {car_5.color} едет со скоростью {car_5.speed} км/ч. "
      f"{'Не является машиной полиции!' if car_5.is_police == False else 'Является машиной полиции!'}")
car_5.show_speed()
car_5.turn("направо")
car_5.stop()
print()