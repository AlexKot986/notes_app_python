from read_write_json import ReadWriteJson
from sort_notes import SortNotes

class Menu:
  
    def start(self, notebook):
        work = True
        print('Начало работы')
        
        while(work):
            print('------------------------')
            print('1. Добавить запись')
            print('2. Изменить запись')
            print('3. Удалить запись')
            print('4. Показать запись')
            print('5. Показать все записи')
            print('6. Сохранить блокнот')
            print('7. Загрузить блокнот')
            print('8. Отсортировать блокнот по дате')
            print('9. Отсортировать блокнот по id')
            print('10. Показать записи за один день')
            print('0. Завершить работу')
            print('------------------------')

            try:
                choose = int(input('Выбор действия: '))

                match choose:
                    case 1: 
                        notebook.add_note()
                        print('Запись добавлена')
                    case 2: 
                        notebook.change_note(notebook.find_note(int(input('id записи: '))))
                        print('Запись изменена')
                    case 3: 
                        notebook.remove_note(notebook.find_note(int(input('id записи: '))))
                        print('Запись удалина')
                    case 4: notebook.show_note(notebook.find_note(int(input('id записи: '))))
                    case 5: notebook.show_notebook()
                    case 6: 
                        ReadWriteJson().write(notebook)
                        print('Блокнот сохранен')
                    case 7: 
                        notebook = ReadWriteJson().read()
                        print('Блокнот загружен')
                    case 8: 
                        SortNotes().sort_by_date(notebook)
                        print('Блокнот отсортирован по дате')
                    case 9: 
                        SortNotes().sort_by_id(notebook)
                        print('Блокнот отсортирован по id')
                    case 10:                   
                        if (notebook.show_notes_day()):
                            print('За этот день данных нет')
                    case 0: 
                        work = False
                        print('Работа завершена')
                    case _: print('Действия с таким номером нет')
            except:
                print('Некорректный ввод')
                