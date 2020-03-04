#2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


user_data = {"имя": "", "фамилия": "", "год рождения": "", "город проживания": "", "email": "", "телефон":""}

def inp_user_data(user_data):
    for key in user_data.keys():
        var = input(f"Введите {key}: ")
        user_data[key] = var
    return user_data

def user_data_to_str(user_data):
    str = ""
    for key in user_data.keys():
        str = (str + ", ") if (key != "имя") else str
        str = str + key + " - " + user_data[key]
    return str

def inp_user_data_par(name, f_name, b_year, sity, email, f_number):
    str = f"имя - {name}, фамилия - {f_name}, год рождения - {b_year}, город проживания - {sity}, email - {email}, телефон - {f_number}."
    return str

# Вариант 1.  Не совсем соответствует условиям задачи, но для закрепления материала с прошлой ДР
print(user_data_to_str(inp_user_data(user_data)))

#Вариант 2. Как в задании
print(inp_user_data_par(name = user_data["имя"], f_name = user_data["фамилия"], b_year = user_data["год рождения"],
                        sity = user_data["город проживания"], email = user_data["email"], f_number = user_data["телефон"]))

#print(inp_user_data(user_data))
#print(user_data_to_str(user_data))
