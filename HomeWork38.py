# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя,
# отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def load_file(filename):
    phonebook = []
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'phone_number': phone_number
                })
            print('Данные успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    return phonebook


def search_contacts(phonebook, search_key):
    results = []
    for contact in phonebook:
        if (search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower()):
            results.append(contact)
    return results

def views_contacts(phonebook):
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")


def save_to_file(filename, phonebook):
    with open(filename, 'w', encoding='UTF-8') as file:
        for contact in phonebook:
            file.write(f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")
    print('Данные сохранены в файле')

def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Контакт добавлен')
# Редактирование ___________________________________________________
def edit_contact(phonebook, edit_num):
        contact = phonebook[edit_num - 1]
        last_name = input('Новая фамилия: ')
        first_name = input('Новое имя: ')
        middle_name = input('Новое отчество: ')
        phone_number = input('Новый номер телефона: ')
        contact['last_name'] = last_name
        contact['first_name'] = first_name
        contact['middle_name'] = middle_name
        contact['phone_number'] = phone_number
    
        phonebook.append(contact)
        print('Контакт изменен')

def dlt_contact(phonebook, dlt_num):# УДАЛЕНИЕ____________________________________________
    phonebook.pop(dlt_num - 1)#Метод pop(): удаление по индексу
    filename = 'contacts.txt'# здесь не очень красиво, по другому не придумал
    save_to_file(filename, phonebook)
    print('Контакт удален')

def main():
    phonebook = []
    filename = 'contacts.txt'

    while True:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Поиск по имени/фамилии")
        print("5. Загрузить из файла")
        print("6. Выйти")
        print("7. Редактировать запись")
        print("8. Удалить запись")

        choice = input('Выберите действие: ')
        if choice == '1':
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            middle_name = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '2':
            save_to_file(filename, phonebook)
        elif choice == '3':
            views_contacts(phonebook)
        elif choice == '4':
            search_key = input("Введите имя или фамилию для поиска: ")
            results = list(search_contacts(phonebook, search_key))
            if (results):
                print('Найдены контакты: ')
                for cur_dict in results:
                    for item in cur_dict.values():
                        print(item, end='')
            else:
                print('Контактов по вашему запросу нет!')
        elif choice == '5':
            phonebook = load_file(filename)
        elif choice == '6':
            break
        elif choice == '7':            
            edit_num = int(input('Введите номер строки для редактирования: '))
            edit_contact(phonebook, edit_num)
        elif choice == '8':            
            dlt_num = int(input('Введите номер строки для удаления: '))
            dlt_contact(phonebook, dlt_num)
        else:
            print('Некорректный выбор. Попробуйте снова')


if __name__ == "__main__":
    main()
