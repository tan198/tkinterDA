from database.connectdb import Connect
from tkinter import ttk, messagebox

class ControllerCar:
    def __init__(self, viewCar, modelCar, server, database, username=None, password=None):
        self.viewCar = viewCar
        self.modelCar = modelCar
        super().__init__()

        self.connectt = Connect(server, database, username, password)
        self.dsCars = []
        self.viewCar.buttons["Load"].config(command=self.load_car)
        self.viewCar.buttons["Add"].config(command=self.create_car)
        self.viewCar