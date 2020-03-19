# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat(self):
        sum_cloth = self.v / 6.5 + 0.5
        return sum_cloth

    def suit(self):
        sum_cloth = self.h * 2 + 0.3
        return sum_cloth


class Clothes_2(ABC):
    def __init__(self, param_1):
        self.param_1 = param_1

    @abstractmethod
    def sum_cloth(self):
        pass


class Coat(Clothes_2):
    @property
    def sum_cloth(self):
        return (self.param_1 / 6.5 + 0.5)


class Suit(Clothes_2):
    def sum_cloth(self):
        return (self.param_1 * 2 + 0.3)


cl = Clothes(42, 180)
sum_cloth = cl.coat() + cl.suit()
print(sum_cloth)

v_coat = Coat(42)
v_suit = Suit(180)
print(v_coat.sum_cloth + v_suit.sum_cloth())
