from NotesApp.Presenter.App import *

print("Note_console")

flag = True
app = App()

while flag:
    print("Введите команду:\n"
          "1. Создать заметку\n"
          "2. Редактировать заметку\n"
          "3. Сохранить заметки\n"
          "4. Удалить заметку\n"
          "5. Вывести все заметки\n"
          "6. Выход")
    in_data = input("Ввод: ")
    match in_data:
        case "1":
            title = input("Введите название: ")
            description = input("Введите описание: ")
            app.create_note(title, description)
            app.add_list()
        case "2":
            pass
        case "3":
            app.save_notes()
            print("Заметки сохранены")
        case "4":
            note = input("Введите название удаляемой заметки: ")
            if app.note_list.check_note(note):
                app.del_note(note)
            else: print("Такой заметки нет")
        case "5":
            list = app.note_list.get_list()
            if len(list) != 0:
                for note in list:
                    print(note.get_note())
            else: print("Cписок заметок пустой")

        case "6":
            flag = False
            print("Exit Note_console")
        case _:
            pass