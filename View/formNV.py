from tkinter import *
import tkinter as tk
from database import connectdb
from Controller import ControllerCar as Ctrl
import Main
class ViewNV(tk.Tk):
    def __init__(self,server,database):
        super().__init__()
        self.title('MANAGERMENT')
        self.geometry('400x270')
        self.config(bg='lightblue')
        self.stt_counter = 0
        self.ket_noi = connectdb.Connect(server, database)

        LoginFrame = Frame(self.master,bg='lightblue')
        LoginFrame.grid()


        # TITLE FRAME
        Title_Frame=LabelFrame(LoginFrame,width=400,height=50, pady=20,padx=20,bg='lightblue',bd=0)
        Title_Frame.pack(side=TOP)
        self.titleF =Label(Title_Frame,width=30,bg='lightblue',text='EMPLOYEE MANAGERMENT',font=('TIME NEW ROMAN',14,'bold'))
        self.titleF.grid()

        # ENTRY FRAME
        Button_Frame = LabelFrame(LoginFrame, width=400, height=150,bg='lightblue', bd=0)
        Button_Frame.pack(side=TOP)


        self.btnQLX = Button(Button_Frame,width=30,height=2,text='CAR MANAGERMENT',font=('TIME NEW ROMAN',15,'bold'), command=lambda: self.run1())
        self.lblSpace1 = Label(Button_Frame, width=25, height=1, text='', bg='lightblue')
        self.btnExit = Button(Button_Frame,width=30,height=2,text='EXIT',font=('TIME NEW ROMAN',15,'bold'), command=lambda: self.destroy())

        self.btnQLX.grid()
        self.lblSpace1.grid()
        self.btnExit.grid()

    def run1(self):
        self.destroy()
        Main.runviewQLX()

