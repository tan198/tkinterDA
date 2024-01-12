from database.connectdb import Connect
from tkinter import ttk, messagebox


class ControllerCar:
    def __init__(self, view, model, server, database, username=None, password=None):
        self.view = view
        self.model = model
        super().__init__()

        self.connectt = Connect(server, database, username, password)
        self.dsCars = []
        # self.view.buttons["Update"].config(command=self.update)
        # self.view.buttons["Add Car"].config(command=self.create_car)
        # self.view.buttons["Delete"].config(command= self.delete_car)
