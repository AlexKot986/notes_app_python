from note import Note
from datetime import datetime

class Notebook:

    def __init__(self):
        self.__counter = 0
        self.__listOfNotes = []

    def get_counter(self):
        return self.__counter
    def set_counter(self, number):
        self.__counter = number
    
    def get_listOfNotes(self):
        return self.__listOfNotes
    def set_listOfNotes(self, list_of_notes):
        self.__listOfNotes = list_of_notes
    
    def add_note(self):
        _id = self.__counter + 1
        title = input('title: ')
        message = input('message: ')
        date = datetime.now().strftime('%B %d, %Y, %H:%M:%S')
        self.__listOfNotes.append(Note(_id, date, title, message))
        self.__counter += 1

    def show_note(self, indx):
        self.__listOfNotes[indx].show_note()

    def show_notebook(self):
        for note in self.__listOfNotes:
            note.show_note()


