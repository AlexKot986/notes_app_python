class Note:
        
    def __init__(self, _id, date, title, message):
        self.__id = _id
        self.__date = date
        self.__title = title
        self.__message = message

    def get_id(self):
        return self.__id
    def get_date(self):
        return self.__date
    def get_title(self):
        return self.__title
    def get_message(self):
        return self.__message
    
    def set_id(self, number):
        self.__id = number
    def set_date(self, text):
        self.__date = text
    def set_title(self, text):
        self.__title = text
    def set_message(self, text):
        self.__message = text
    
    def show_note(self):
        print('-------------------------------------------')
        print('id:', self.get_id())
        print('date -->', self.get_date())
        print('title -->', self.get_title())
        print('message -->', self.get_message())
        print('-------------------------------------------')

