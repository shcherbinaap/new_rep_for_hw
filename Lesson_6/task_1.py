# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
from time import sleep


# Вариант 1. Параметры заданы в классе
class TrafficLight():
    def __init__(self, color=["красный", "желтый", "зеленый", "желтый"]):
        self.color = color

    # color = ["красный", "желтый", "зеленый", "желтый"]

    def running(self):
        for i in cycle(self.color):
            print(i)
            if i == "красный" or i == "зеленый":
                sleep(3)
            else:
                sleep(1)


# Вариант 2. В класс передается один цвет (начальный)
class TrafficLight:
    def __init__(self, color):
        self.color = color.lower()

    def running(self):
        while True:
            if self.color == "красный":
                print(self.color)
                self.color = "желтый"
                sleep(3)
                print(self.color)
                self.color = "зеленый"
                sleep(1)
            elif self.color == "зеленый":
                print(self.color)
                self.color = "желтый"
                sleep(3)
                print(self.color)
                self.color = "красный"
                sleep(1)
            elif self.color == "желтый":
                print(self.color)
                self.color = "зеленый"
                sleep(1)
            else:
                print("Не правильно задан цвет!")
                break


# a = TrafficLight()
# a = TrafficLight(["красный", "желтый", "зеленый", "желтый"])
# a = TrafficLight("желтый")
# a = TrafficLight("Красный")
a = TrafficLight("Зеленый")
# a = TrafficLight("голубой")
a.running()
