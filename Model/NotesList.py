from NotesApp.Model.Note import Note

class NotesList:
    def __init__(self):
        self.__notesList = []
        self.current_index = 0

    def add_note(self, note: Note):
        self.__notesList.append(note)
    def del_note(self, note: Note):
        if note in self.__notesList:
            self.__notesList.remove(note)
    def get_list(self):
        return self.__notesList

    def check_note(self, title):
        for note in self.__notesList:
            if note.get_title() == title:
                return True
        return False

    def remove_by_title(self, title):
        for note in self.__notesList:
            if note.get_title() == title:
                self.__notesList.remove(note)
                break

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.__notesList):
            result = self.__notesList[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration