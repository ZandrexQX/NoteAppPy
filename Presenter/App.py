from NotesApp.Model.Note import Note
from NotesApp.Model.NotesList import NotesList

note_list = NotesList()
def create_note(title, descr):
    note = Note(title, descr)

def add_list(note: Note):
    note_list.add_note(note)