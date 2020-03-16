# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, lenght, width, weight=25, height=5):
        self._lenght = lenght
        self._width = width
        self._weight = weight
        self._height = height

    def quantity(self):
        asphalt_weight = self._lenght * self._width * self._weight * self._height / 1000
        return asphalt_weight

road_need = Road(5000, 20)
print(road_need.quantity())
