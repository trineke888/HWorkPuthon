from data_create import name_data, surname_data, phone_data, address_data

file_name = "D:\Telephone\data_first_variant.csv" 
file_name = "D:\Telephone\data_second_variant.csv"

def remove_empty_lines(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        lines = file.readlines()

    replacing_lines = []
    for line in lines:
        if line.strip():  
            replacing_lines.append(line)

    with open(file_name, "w", encoding='utf-8') as file:
        for line in replacing_lines:
            file.write(line)


def change_data():
    remove_empty_lines("D:\Telephone\data_second_variant.csv")
    remove_empty_lines("D:\Telephone\data_second_variant.csv")
    selection = int(input("Внести изменения в варианты файла: \n 1 \n 2 \n "))
    while selection != 1 and selection != 2:
        print("Неправильный ввод")
        selection = int(input("Введите число: \n "))

    if selection == 1:
        with open("D:\Telephone\data_first_variant.csv", "r", encoding='utf-8') as f:
            data = f.readlines()        
        print("Доступные данные для изменения:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки: "))
        new_data = input("Введите новые данные: ") 
        data[line_number-1] = new_data + " \n"

        with open("D:\Telephone\data_first_variant.csv", "w", encoding='utf-8') as f:
            f.writelines(data)
        print ("Данные сохранены")

    elif selection == 2:
        with open("D:\Telephone\data_second_variant.csv", "r", encoding='utf-8') as f:
            data = f.readlines()            
        print("Доступные данные для изменения:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки: "))
        new_data = name_data() + "; " + surname_data() + "; " + phone_data() + "; " + address_data()
        data[line_number-1] = new_data + "\n"

        with open("D:\Telephone\data_second_variant.csv", "w", encoding='utf-8') as f:
            f.writelines(data)
        print ("Данные сохранены")

   

def delete_data():
    selection = int(input("Внести изменения в варианты файла: \n 1 \n 2 "))
    while selection != 1 and selection != 2:
        print("Неправильный ввод")
        selection = int(input("Выберите вариант: "))

    if selection == 1:
        with open("D:\Telephone\data_first_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные данные для удаления: ")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки: "))

        del data[line_number-1]

        with open("D:\Telephone\data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Данные удалены")

    elif selection == 2:
        with open("D:\Telephone\data_second_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные данные для удаления: ")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки: "))

        del data[line_number-1]

        with open("dD:\Telephone\data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Данные удалены")