from note import Note
from notebook import Notebook
import json

class ReadWriteJson:

    def write(self, notebook):
        data_list_of_notes = []
        for note in notebook.get_listOfNotes():
            data_note = {
                "id": note.get_id(),
                "date": note.get_date(),
                "title": note.get_title(),
                "message": note.get_message()
            }
            data_list_of_notes.append(data_note)

        data_notebook = {
            "counter": notebook.get_counter(),
            "listOfNotes": data_list_of_notes
        }

        with open('my_notebook_file_1.json', 'w', encoding='utf-8') as save:
            json.dump(data_notebook, save, indent=2, ensure_ascii=False)

    def read(self):
        with open('my_notebook_file_1.json', 'r', encoding='utf-8') as load:
            data_notebook = json.load(load)

        list_of_notes = self.__create_list_of_notes(data_notebook)
        notebook = self.__create_notebook(data_notebook, list_of_notes)
        return notebook
    
    def __create_notebook(self, data_notebook, list_of_notes):
        notebook = Notebook()
        notebook.set_counter(data_notebook.get('counter'))
        notebook.set_listOfNotes(list_of_notes)
        return notebook
    
    def __create_list_of_notes(self, data_notebook):
        list_of_notes = []

        for data_note in data_notebook.get('listOfNotes'):
            _id = data_note.get('id')
            date = data_note.get('date')
            title = data_note.get('title')
            message = data_note.get('message')

            list_of_notes.append(Note(_id, date, title, message))

        return list_of_notes
    
