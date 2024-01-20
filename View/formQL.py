from tkinter import *
import tkinter as tk
from database import connectdb
import Main

class ViewQL(tk.Tk):
    def __init__(self,server,database):
        super().__init__()
        self.title('MANAGERMENT')
        self.geometry('394x470')
        self.config(bg='lightblue')
        self.stt_counter = 0
        self.ket_noi = connectdb.Connect(server, database)

        LoginFrame = Frame(self.master,bg='lightblue',pady=20,padx=10)
        LoginFrame.grid()


        # TITLE FRAME
        Title_Frame=LabelFrame(LoginFrame,width=400,height=50, bg='lightblue',pady=10, bd=0)
        Title_Frame.pack(side=TOP)
        self.titleLabel=Label(Title_Frame,width=20 , bg='lightblue',text=' ADMIN MANAGERMENT ', font=('TIME NEW ROMAN',15,'bold'),bd=0)
        self.titleLabel.grid()

        # ENTRY FRAME
        Button_Frame = LabelFrame(LoginFrame, width=400, height=150, bg='lightblue')
        Button_Frame.pack(side=TOP)

        self.lblSpace1 = Label(Button_Frame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace2 = Label(Button_Frame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace3 = Label(Button_Frame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace4 = Label(Button_Frame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace5 = Label(Button_Frame, width=25, height=1, text='', bg='lightblue')

        self.btnQLX = Button(Button_Frame,width=30,height=2,text='CAR',font=('TIME NEW ROMAN',15,'bold'),command=lambda: self.run1())
        self.btnSale = Button(Button_Frame,width=30,height=2,text='EMPLOYEE',font=('TIME NEW ROMAN',15,'bold'),command=lambda: self.run2())
        self.btnRegister = Button(Button_Frame, width=30, height=2, text='REGISTER',font=('TIME NEW ROMAN', 15, 'bold'), command=lambda: self.run3())
        self.btnExit = Button(Button_Frame,width=30,height=2,text='EXIT',font=('TIME NEW ROMAN',15,'bold'), command=lambda: self.destroy())

        self.lblSpace1.grid()
        self.btnQLX.grid()

        self.lblSpace2.grid()
        self.btnSale.grid()

        self.lblSpace3.grid()
        self.btnRegister.grid()

        self.lblSpace4.grid()
        self.btnExit.grid()

        self.lblSpace5.grid()

    def run1(self):

        Main.runviewQLX()
    def run2(self):

        Main.runviewSale()
    def run3(self):

        Main.runRegister()
