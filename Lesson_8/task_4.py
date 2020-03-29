# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

import json


class Storage:
    def __init__(self, item: object, row=0, shelf=0, cell=0):
        # self.storage = storage
        # self.name = item.name
        # self.row = row
        self.item_dict = item.__dict__
        # self. shelf = shelf
        # self.cell = cell

    # Метод получения данных с файла/базы
    def get_storage_cell(self, file_name: str):
        with open(file_name) as read_f:
            data = json.load(read_f)
        return data

    # Метод записи в файл/базу
    def put_storage_info(self, data: dict, file_name: str):
        with open(file_name, "w") as write_f:
            json.dump(data, write_f)

    # Метод сдачи товара на склад
    def input_item(self, data: dict, item_dict: dict, items_dict: dict):
        address = None
        if self.check_val(item_dict):
            for key, item in data.items():
                if item == False:
                    address = key
                    data[key] = item_dict
                    items_dict = self.count_item(items_dict, item_dict, input_item=True, output_item=False)
                    self.put_storage_info(data, "warehouse.json")
                    self.put_storage_info(items_dict, "items_dict.json")
                    break
            return address if address != None else "Все ячейки складов заняты!"
        else:
            return False

    # Метод выдачи товара со склада либо по адресу ячейки где он находится, либо по имени объекта (имя уникально)
    def output_item(self, data: dict, items_dict: dict, **kwargs):
        try:
            kwargs["address"]
        except KeyError:
            kwargs["address"] = None
        if kwargs["address"] != None:
            if data[kwargs["address"]] != False:
                items_dict = self.count_item(items_dict, data[kwargs["address"]], input_item=False, output_item=True)
                data[kwargs["address"]] = False
            else:
                print("Товара в данной ячейке нет")
            self.put_storage_info(data, "warehouse.json")
            self.put_storage_info(items_dict, "items_dict.json")

        elif kwargs["object_dict"]:
            for key, item in data.items():

                if item != False and item["name"] == kwargs["object_dict"]["name"]:
                    items_dict = self.count_item(items_dict, data[key], input_item=False,
                                                 output_item=True)
                    data[key] = False

                    self.put_storage_info(data, "warehouse.json")
                    self.put_storage_info(items_dict, "items_dict.json")
                    break
            else:
                print(f"Товар {kwargs['object_dict']['name']} не найден")
        else:
            print("Не достаточно данных для поиска товара!")

    # Подсчет количества объектов в базе (считается, что имя объекта уникально!)
    def count_item(self, items_dict: dict, object_dict: dict, input_item=False, output_item=False):
        if input_item == True:
            if items_dict.get(object_dict["name"]) == None:
                items_dict[object_dict["name"]] = 1
            else:
                items_dict[object_dict["name"]] += 1
        elif output_item == True:
            if items_dict[object_dict["name"]] == 1:
                val_item = items_dict.pop(object_dict["name"])
            elif items_dict[object_dict["name"]] > 1:
                items_dict[object_dict["name"]] -= 1
            else:
                print("Такого наименования товара нет!")
        return items_dict

    # Поиск адресов ячеек по параметрам объекта
    def find_obj_by_atr(self, data: dict, **kwargs):
        adr_list = []
        for item_key, item in data.items():
            result = False
            for key, val in kwargs.items():
                if item != False and kwargs[key] == item[key]:
                    result = True
                else:
                    result = False
                    break
            if result == True:
                adr_list.append(item_key)
        return adr_list

    # Проверка типа вводимых данных
    def check_val(self, object_dict: dict):
        result = False
        type_of_val ={
            "length": int,
            "width": int,
            "height": int,
            "weight": int,
            "name": str,
            "print_tech": str,
            "color": bool,
            "max_form": str,
            "permission": int,
            "scan_form": str,
            "speed_scan": int,
            "max_permission": int,
            "quantity": int
        }
        for key, val in object_dict.items():
            if type(object_dict[key]) != type_of_val[key]:
                print(f"Не совпадает тип данных {key}")
                break
        else:
            result = True
        return result




class Office_eq:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight


class Printers(Office_eq):
    def __init__(self, length, width, height, weight, name, print_tech, color, max_form):
        super().__init__(length, width, height, weight)
        self.name = name
        self.print_tech = print_tech
        self.color = color
        self.max_form = max_form


class Scaners(Office_eq):
    def __init__(self, length, width, height, weight, name, permission, scan_form):
        super().__init__(length, width, height, weight)
        self.name = name
        self.permission = permission
        self.scan_form = scan_form


class Xeroxes(Office_eq):
    def __init__(self, length, width, height, weight, name, speed_scan, max_permission):
        super().__init__(length, width, height, weight)
        self.name = name
        self.speed_scan = speed_scan
        self.max_permission = max_permission


# допустим имеется два склада, по 3 ряда, в каждом ряду по 3 полки, на каждой полке по 2 ячейки
# то есть место техники имеет 4 разряда


# Сделано одно допущение, имя техники уникально для каждого вида устройства
# office_eq_1 = Printers(100, 60, 20, 2, "printer 1", "laser", True, "A4")
# office_eq_1 = Printers(100, 50, 20, 2, "printer 2", "laser", True, "A4")
office_eq_1 = Printers(100, 40, 20, 2, "printer 3", "laser", True, "A4")

storage_1 = Storage(office_eq_1)
# print(storage_1.item.name)

# Добавление объекта на склад
address = storage_1.input_item(storage_1.get_storage_cell("warehouse.json"), storage_1.item_dict, storage_1.get_storage_cell("items_dict.json"))
print(address)

# Забрать объект со склада по параметру как объект (полное описание)
address = "1111"
# storage_1.output_item(storage_1.get_storage_cell("warehouse.json"), storage_1.get_storage_cell("items_dict.json"),
#                       object_dict=storage_1.item_dict)

# забрать объект со склада по значению ячейки в которой он находится
# storage_1.output_item(storage_1.get_storage_cell("warehouse.json"), storage_1.get_storage_cell("items_dict.json"),
#                       address=address)

# Поиск ячеек в которых находятся объекты удовлетворяющим перечисленным параметрам
# print(storage_1.find_obj_by_atr(storage_1.get_storage_cell("warehouse.json"), length=100))
# print(storage_1.find_obj_by_atr(storage_1.get_storage_cell("warehouse.json"), length=100), width=40)
# print(storage_1.find_obj_by_atr(storage_1.get_storage_cell("warehouse.json"), length=100), width=40, height= 20)

# Проверка типа вводимых данных объекта. Используется перед записью данных объекта в базу.
# Считается, что в базе все записи сделаны уже в правильном типе данных
# print(storage_1.check_val(office_eq_1.__dict__))