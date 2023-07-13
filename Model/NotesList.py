import Note

class NotesList:
    def __init__(self):
        self.__notesList = []

    def add_note(self, note: Note):
        self.__notesList.append(note)
    def del_note(self, note: Note):
        if note in self.__notesList:
            self.__notesList.remove(note)
    def get_list(self):
        return self.__notesList