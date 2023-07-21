class SortNotes:
    
    def __sort_date(self, note):
        return note.get_date()
    def __sort_id(self, note):
        return note.get_id()
    
    def sort_by_date(self, notebook):
        notebook.get_listOfNotes().sort(key=self.__sort_date)
    def sort_by_id(self, notebook):
        notebook.get_listOfNotes().sort(key=self.__sort_id)