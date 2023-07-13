import csv

from NotesApp.Model.Note import Note
from NotesApp.Model.NotesList import NotesList

class App:
    def __init__(self):
        self.note = None
        self.note_list = NotesList()

    def create_note(self, title: str, descr: str):
        self.note = Note(title, descr)

    def add_list(self):
        self.note_list.add_note(self.note)
    def del_note(self, title):
        self.note_list.remove_by_title(title)
    def save_notes(self):
        with open("data.csv", "w", newline="") as data:
            writer = csv.writer(data)
            for note in self.note_list:
                writer.writerow([note.get_title(), note.get_description()])

    def read_from_csv(self):
        with open("data.csv", 'r') as file:
            self.note_list = NotesList()
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) == 2:
                    title = row[0]
                    content = row[1]
                    note = Note(title, content)
                    self.note_list.add_note(note)