from NotesApp.Presenter.App import *
from colorama import Fore, Back, Style
print(Fore.BLUE + "Note_console")

flag = True
app = App()

while flag:
    print(Fore.YELLOW + "Введите команду:\n"
          "1. Создать заметку\n"
          "2. Редактировать заметку\n"
          "3. Удалить заметку\n"
          "4. Загрузить заметки\n"
          "5. Сохранить заметки\n"
          "6. Вывести все заметки\n"
          "7. Выход")
    in_data = input(Fore.BLUE + "Ввод: ")
    match in_data:
        case "1":
            title = input(Fore.BLUE + "Введите название: ")
            description = input(Fore.BLUE + "Введите описание: ")
            app.create_note(title, description)
            app.add_list()
            print(Fore.GREEN + f"Заметка {title} добавлена")
        case "2":
            title = input(Fore.BLUE + "Введите название редактируемой заметки: ")
            if app.note_list.check_note(title):
                note = app.note_list.get_note(title)
                descr = input(Fore.YELLOW + f"Заметка {title} найдена. Введите новое описание: ")
                note.set_description(descr)
                print(Fore.GREEN + "Заметка изменена")
        case "3":
            note = input(Fore.BLUE + "Введите название удаляемой заметки: ")
            if app.note_list.check_note(title):
                app.del_note(title)
                print(Fore.GREEN + f"Заметка {title} удалена")
            else:
                print(Fore.RED + "Такой заметки нет")
        case "4":
            app.read_from_csv()
            print(Fore.GREEN + "Заметки загружены")
        case "5":
            app.save_notes()
            print(Fore.GREEN + "Заметки сохранены")
        case "6":
            list = app.note_list.get_list()
            if len(list) != 0:
                print(Fore.GREEN + "Список заметок:")
                for note in list:
                    print(note.get_note())
            else: print(Fore.RED + "Cписок заметок пустой")

        case "7":
            flag = False
            print(Fore.BLUE + "Exit Note_console")
        case _:
            pass