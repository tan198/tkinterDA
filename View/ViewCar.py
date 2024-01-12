import tkinter as tk
from database.connectdb import Connect
from Model.ModelCar import ModelCar
import tkinter.simpledialog

from tkinter import font, ttk


class ViewCars(tk.Tk):
    def __init__(self, server, database, username=None, password=None):
        super().__init__()
        self.title("Car Management System")
        self.geometry("906x662")

        self.stt_counter = 0
        self.connectt = Connect(server, database)
        self.cars = ModelCar(server, database, self.connectt)

        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.lbTitle = tk.Label(text="Car Management System", font=title_font)
        self.lbTitle.grid(row=0, column=1, pady=5, columnspan=2)

        self.lbCarID = tk.Label(text="Search CarID:")
        self.lbCarID.grid(row=1, column=1)

        self.efCarID = tk.Entry()
        self.efCarID.grid(row=1, column=2)

        # Create frame buttons search
        self.btn_frame = tk.Frame()
        self.btn_frame.grid(row=1, column=3, columnspan=2, pady=10)

        self.buttons = {
            "Search": tk.Button(self, text="Search")
        }

        self.buttons["Search"].grid(row=2, column=4, padx=10)

        # Create treeview display data
        self.treeview = ttk.Treeview(columns=('', 'CarID', 'Make', 'Model', 'Year', 'Transmission', 'Body Type',
                                              'Category', 'Price'), show=["headings"])
        self.treeview.heading('', text='')
        self.treeview.heading('CarID', text='CarID')
        self.treeview.heading('Make', text='Make')
        self.treeview.heading('Model', text='Model')
        self.treeview.heading('Year', text='Year')
        self.treeview.heading('Transmission', text='Transmission')
        self.treeview.heading('Body Type', text='Body Type')
        self.treeview.heading('Category', text='Category')
        self.treeview.heading('Price', text='Price')
        self.treeview.grid(row=4, column=0, columnspan=5)

        # Create Frame buttons add,update, delete
        self.btn_frame = tk.Frame()
        self.btn_frame.grid(row=5, column=0, columnspan=4, pady=10)

        self.buttons = {
            "Add Car": tk.Button(self, text="Add Car"),
            "Delete": tk.Button(self, text="Delete"),
            "Update": tk.Button(self, text="Update")
        }

        #for button in self.buttons.values():
         #   button.pack(side=tk.LEFT, padx=5)

    def add_car_dialog(self):
        car_dialog = AddCarDialog(self)
        self.wait_window(car_dialog)

        # Retrieve data from the dialog if needed
        car_data = car_dialog.get_car_data()
        if car_data:
            # Add the new car data to the treeview or perform other actions
            pass


class AddCarDialog(tk.simpledialog.Dialog):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.car_data = {}  # Dictionary to store entered data
        self.entries = {}

    def body(self, master):
        # Labels and Entry fields for each column
        fields = ['CarID', 'Make', 'Model', 'Year', 'Transmission', 'Body Type', 'Category', 'Price']

        for row, field in enumerate(fields):
            label = tk.Label(master, text=field)
            label.grid(row=row, column=0, padx=5, pady=5, sticky="E")

            entry = tk.Entry(master)
            entry.grid(row=row, column=1, padx=5, pady=5, sticky="W")
            self.entries[field] = entry

        return self.entries[fields[0]]  # Initial focus on the first entry field

    def apply(self):
        # Validate and store the entered data
        for field, entry in self.entries.items():
            self.car_data[field] = entry.get()

    def get_car_data(self):
        return self.car_data
