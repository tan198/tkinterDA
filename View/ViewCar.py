import tkinter as tk
from database.connectdb import Connect
from Model.ModelCar import Model_Cars

from tkinter import *

class ViewCar(tk.Tk):
    def __int__(self, server, database, username=None, password=None):
        super().__init__()
        self.title("Quản Lý Xe")
        self.geometry("906x662")


