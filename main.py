from notebook import Notebook
from read_write_json import ReadWriteJson
from menu import Menu

# my_notebook = Notebook()
# my_notebook.add_note()
# my_notebook.add_note()
# my_notebook.add_note()
# my_notebook.show_notebook()

# ReadWriteJson().write(my_notebook)

# some_notebook = ReadWriteJson().read()
# print()
# some_notebook.show_notebook()
# print()

# some_notebook.change_note(some_notebook.find_note(3))

# ReadWriteJson().write(some_notebook)

# new_notebook = ReadWriteJson().read()
# new_notebook.show_notebook()

Menu().start(Notebook())
