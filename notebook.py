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
    
   