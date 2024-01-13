from Model import ModelCar
from tkinter import *
from tkinter import ttk
from tkinter import Canvas
import tkinter.messagebox
import datetime
import tkinter as tk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import time
from database.connectdb import Connect
from Model.ModelCar import ModelCar
from Controller import ControllerCar

class ViewCar(tk.Tk):
    def __init__(self,server,database):
        super().__init__()
        self.title('H? TH?NG XE')
        self.geometry('1200x650')
        self.config(bg='lightblue')
        self.stt_counter = 0
        self.connectt = Connect(server, database)
        self.model = ModelCar(server, database, self.connectt)

        MainFrame = Frame(self.master,bg='lightblue')
        MainFrame.grid()

        # TITLE FRAME
        TitleFrame=LabelFrame(MainFrame,width=1200,height=50,bg='lightblue',relief=RIDGE,bd=5)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame,width=100,font=('arial', 15), text='QU?N L� XE',bg='lightblue')
        self.lblTitle.grid()


        # MID FRAME
        MidFrame = LabelFrame(MainFrame, width=1100, height=400, bg='lightblue', relief=RIDGE, bd=5)
        MidFrame.pack(side=TOP)
        # TEXTBOX FRAME
        TextboxFrame = LabelFrame(MidFrame, width=550, height=200, bg='lightblue', relief=RIDGE, bd=5)
        TextboxFrame.pack(side=LEFT)
        # -------------------------------------------------------------
        self.lblID=Label(TextboxFrame,width=10,text='ID')
        self.lblID.grid(row=0,column=0)
        self.ID_Entry = Entry(TextboxFrame,width=50)
        self.ID_Entry.grid(row=0,column=1,padx=5,pady=5)

        self.lblMake=Label(TextboxFrame,width=10,text='Make')
        self.lblMake.grid(row=1,column=0)
        self.Make_Entry = Entry(TextboxFrame, width=50)
        self.Make_Entry.grid(row=1, column=1, padx=5, pady=5)

        self.lblModel=Label(TextboxFrame,width=10,text='Model')
        self.lblModel.grid(row=2,column=0)
        self.Model_Entry = Entry(TextboxFrame, width=50)
        self.Model_Entry.grid(row=2, column=1, padx=5, pady=5)

        self.lblYear=Label(TextboxFrame,width=10,text='Year')
        self.lblYear.grid(row=3,column=0)
        self.Year_Entry = Entry(TextboxFrame, width=50)
        self.Year_Entry.grid(row=3, column=1, padx=5, pady=5)

        self.lblTransmission=Label(TextboxFrame,width=10,text='Transmission')
        self.lblTransmission.grid(row=4,column=0)
        self.Transmission_Entry = Entry(TextboxFrame, width=50)
        self.Transmission_Entry.grid(row=4, column=1, padx=5, pady=5)

        self.lblBody=Label(TextboxFrame,width=10,text='Body')
        self.lblBody.grid(row=5,column=0)
        self.Body_Entry = Entry(TextboxFrame, width=50)
        self.Body_Entry.grid(row=5, column=1, padx=5, pady=5)

        self.lblCategory=Label(TextboxFrame,width=10,text='Category')
        self.lblCategory.grid(row=6,column=0)
        self.Category_Entry = Entry(TextboxFrame, width=50)
        self.Category_Entry.grid(row=6, column=1, padx=5, pady=5)

        self.lblPrice=Label(TextboxFrame,width=10,text='Price')
        self.lblPrice.grid(row=7,column=0)
        self.Price_Entry = Entry(TextboxFrame, width=50)
        self.Price_Entry.grid(row=7, column=1, padx=5, pady=5)
        # -------------------------------------------------------------

        # BUTTON FRAME
        ButtonFrame = LabelFrame(MidFrame, width=550, height=200, bg='lightblue', relief=RIDGE, bd=5)
        ButtonFrame.pack(side=RIGHT)
        # -------------------------------------------------------------
        self.buttons = {
            "INSERT": tk.Button(ButtonFrame, text="btnInsert", width=30),
            "UPDATE": tk.Button(ButtonFrame, text="btnUpdate", width=30),
            "DELETE": tk.Button(ButtonFrame, text="btnDelete", width=30),
            "LOAD": tk.Button(ButtonFrame, text="btnLoad", width=30)
        }
        self.buttons["INSERT"].grid(row=0, column=0, padx=10)
        self.buttons["UPDATE"].grid(row=1, column=0, padx=10)
        self.buttons["DELETE"].grid(row=2, column=0, padx=10)
        self.buttons["LOAD"].grid(row=3, column=0, padx=10)

        # -------------------------------------------------------------

        # TREEVIEW FRAME
        TreeFrame = LabelFrame(MainFrame, width=1100, height=200, bg='lightblue', relief=RIDGE, bd=5)
        TreeFrame.pack(side=TOP)

        sb = Scrollbar(TreeFrame)
        self.treeview = ttk.Treeview(TreeFrame,
                                     columns=('', 'CarID', 'Make', 'Model', 'Year', 'Transmission', 'Body_Type',
                                              'Category', 'Price'),
                                     show=["headings"], yscrollcommand=sb.set)
        self.treeview.heading('', text='')
        self.treeview.heading('CarID', text='CarID')
        self.treeview.heading('Make', text='Make')
        self.treeview.heading('Model', text='Model')
        self.treeview.heading('Year', text='Year')
        self.treeview.heading('Transmission', text='Transmission')
        self.treeview.heading('Body_Type', text='Body Type')
        self.treeview.heading('Category', text='Category')
        self.treeview.heading('Price', text='Price')

        self.treeview.column('', width=20, anchor=tk.CENTER)
        self.treeview.column('CarID', width=80, anchor=tk.CENTER)
        self.treeview.column('Make', width=150, anchor=tk.CENTER)
        self.treeview.column('Model', width=250, anchor=tk.CENTER)
        self.treeview.column('Year', width=150, anchor=tk.CENTER)
        self.treeview.column('Transmission', width=150, anchor=tk.CENTER)
        self.treeview.column('Body_Type', width=100, anchor=tk.CENTER)
        self.treeview.column('Category', width=120, anchor=tk.CENTER)
        self.treeview.column('Price', width=120, anchor=tk.CENTER)

        self.treeview.grid(row=7, column=0, columnspan=7)
        sb.grid(row=7, column=6, sticky='ns')