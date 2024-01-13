from database import connectdb
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
from database import connectdb
from Controller import ControllerCar

class View(tk.Tk):
    def __init__(self,server,database):
        super().__init__()
        self.title('H? TH?NG XE')
        self.geometry('1200x650')
        self.config(bg='lightblue')
        self.stt_counter = 0
        self.ket_noi = connectdb.Connect(server, database)

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
        TextboxFrame = LabelFrame(MidFrame, width=400, height=200, bg='lightblue', relief=RIDGE)
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
        Mid2Frame = LabelFrame(MidFrame, width=400, height=200, bg='lightblue', relief=RIDGE)
        Mid2Frame.pack(side=RIGHT)
        # BUTTON FRAME
        ButtonFrame = LabelFrame(Mid2Frame, width=200, height=200, bg='lightblue', relief=RIDGE,pady=12)
        ButtonFrame.pack(side=TOP)
        # -------------------------------------------------------------
        self.btnInsert=Button(ButtonFrame,width=30,relief=RIDGE,bd=5,text='btnInsert')
        self.btnInsert.grid(row=0,column=0)
        self.btnUpdate = Button(ButtonFrame, width=30, relief=RIDGE, bd=5, text='btnUpdate')
        self.btnUpdate.grid(row=1, column=0)
        self.btnDelete = Button(ButtonFrame, width=30, relief=RIDGE, bd=5, text='btnDelete')
        self.btnDelete.grid(row=2, column=0)
        self.btnLoad = Button(ButtonFrame, width=30, relief=RIDGE, bd=5, text='btnLoad')
        self.btnLoad.grid(row=3, column=0)
        # -------------------------------------------------------------

        # SEARCH FRAME
        SEARCHFrame = LabelFrame(Mid2Frame, width=200, height=200, bg='lightblue', relief=RIDGE,pady=12)
        SEARCHFrame.pack(side=BOTTOM)
        # -------------------------------------------------------------
        self.lblSearch = Label(SEARCHFrame, width=30, text='Search')
        self.lblSearch.grid(row=1, column=0)
        self.Search_Entry = Entry(SEARCHFrame, width=35)
        self.Search_Entry.grid(row=2, column=0, padx=5, pady=5)
        self.btnSearch = Button(SEARCHFrame, width=30, relief=RIDGE, bd=5, text='btnSearch')
        self.btnSearch.grid(row=3, column=0)

        # -------------------------------------------------------------

        # TREEVIEW FRAME
        TreeFrame = LabelFrame(MainFrame, width=1100, height=200, bg='lightblue', relief=RIDGE, bd=5)
        TreeFrame.pack(side=TOP)

        sb = Scrollbar(TreeFrame)
        self.treeview = ttk.Treeview(TreeFrame,
                                     columns=('', 'ID', 'Make', 'Model', 'Year', 'Transmission', 'Body_Type',
                                              'Category','Price'),
                                     show=["headings"], yscrollcommand=sb.set)
        self.treeview.heading('', text='')
        self.treeview.heading('ID', text='ID')
        self.treeview.heading('Make', text='Make')
        self.treeview.heading('Model', text='Model')
        self.treeview.heading('Year', text='Year')
        self.treeview.heading('Transmission', text='Transmission')
        self.treeview.heading('Body_Type', text='Body Type')
        self.treeview.heading('Category', text='Category')
        self.treeview.heading('Price', text='Price')

        self.treeview.column('', width=20, anchor=tk.CENTER)
        self.treeview.column('ID', width=80, anchor=tk.CENTER)
        self.treeview.column('Make', width=150, anchor=tk.CENTER)
        self.treeview.column('Model', width=250, anchor=tk.CENTER)
        self.treeview.column('Year', width=150, anchor=tk.CENTER)
        self.treeview.column('Transmission', width=150, anchor=tk.CENTER)
        self.treeview.column('Body_Type', width=100, anchor=tk.CENTER)
        self.treeview.column('Category', width=120, anchor=tk.CENTER)
        self.treeview.column('Price', width=120, anchor=tk.CENTER)

        self.treeview.grid(row=7, column=0, columnspan=7)
        sb.grid(row=7, column=6, sticky='ns')