from note import Note
from datetime import datetime, date

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

    def find_note(self, _id):
        for indx in range(len(self.__listOfNotes)):
            if self.__listOfNotes[indx].get_id() == _id:
                return indx

    def change_note(self, indx):
        message = input('message: ')
        date = datetime.now().strftime('%B %d, %Y, %H:%M:%S')
        self.__listOfNotes[indx].set_message(message)
        self.__listOfNotes[indx].set_date(date)

    def remove_note(self, indx):
        self.__listOfNotes.pop(indx)

    def show_note(self, indx):
        self.__listOfNotes[indx].show_note()

    def show_notebook(self):
        for note in self.__listOfNotes:
            note.show_note()

    def show_notes_day(self):
        flag = True
        year = int(input('Введите год: '))
        month = int(input('Введите месяц: '))
        day = int(input('Введите день: '))
        find_day = date(year,month,day).strftime('%B %d, %Y')

        for note in self.__listOfNotes:  
            if note.get_date().__contains__(find_day):
                note.show_note()
                flag = False
        return flag
