# 3. Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        # self._income = {"wage": wage, "bonus": bonus}
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return (f"Имя сотрудника - {self.name}, \n"
                f"Фамилия сотрудника - {self.surname}")

    def get_total_income(self):
        # return(self._income["wage"] + self._income["bonus"])
        return (f'Доход сотруждника {self._Worker__income["wage"] + self._Worker__income["bonus"]} зайчиков')


a = Position("Петр", "Иванов", "инженер", 300, 100)

print(f"Атрибут name - {a.name}")
print(f"Атрибут surname - {a.surname}")
print(f"Атрибут position - {a.position}")
print(f"Атрибут income: wage - {a._Worker__income['wage']}")
print(f"Атрибут income: bonus - {a._Worker__income['bonus']}")

print(a.get_full_name())
print(a.get_total_income())
