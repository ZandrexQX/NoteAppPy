from NotesApp.Presenter.App import *

print("Note_console")

flag = True
app = App()

while flag:
    print("Введите команду:\n"
          "1. Создать заметку\n"
          "2. Редактировать заметку\n"
          "3. Удалить заметку\n"
          "4. Загрузить заметки\n"
          "5. Сохранить заметки\n"
          "6. Вывести все заметки\n"
          "7. Выход")
    in_data = input("Ввод: ")
    match in_data:
        case "1":
            title = input("Введите название: ")
            description = input("Введите описание: ")
            app.create_note(title, description)
            app.add_list()
            print(f"Заметка {title} добавлена")
        case "2":
            pass
        case "3":
            note = input("Введите название удаляемой заметки: ")
            if app.note_list.check_note(note):
                app.del_note(note)
                print(f"Заметка {note} удалена")
            else:
                print("Такой заметки нет")
        case "4":
            app.read_from_csv()
            print("Заметки загружены")
        case "5":
            app.save_notes()
            print("Заметки сохранены")
        case "6":
            list = app.note_list.get_list()
            if len(list) != 0:
                print("Список заметок:")
                for note in list:
                    print(note.get_note())
            else: print("Cписок заметок пустой")

        case "7":
            flag = False
            print("Exit Note_console")
        case _:
            pass