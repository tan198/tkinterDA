from tkinter import *
import tkinter as tk
from database import connectdb

class ViewRes(tk.Tk):
    def __init__(self,server,database):
        super().__init__()
        self.title('REGISTER')
        self.geometry('469x215')
        self.config(bg='lightblue')
        self.stt_counter = 0
        self.ket_noi = connectdb.Connect(server, database)

        LoginFrame = Frame(self.master,bg='lightblue')
        LoginFrame.grid()


        # TITLE FRAME
        Title_Frame=LabelFrame(LoginFrame,width=400,height=50)
        Title_Frame.pack(side=TOP)
        # ENTRY FRAME
        Entry_Frame = LabelFrame(LoginFrame, width=400, height=150)
        Entry_Frame.pack(side=TOP)
        # ENTRY FRAME
        Button_Frame = LabelFrame(LoginFrame, width=400, height=150)
        Button_Frame.pack(side=TOP)

        # -------------  TITLE  ------------------
        self.TITLE = Label(Title_Frame, text='REGISTER', font=('TIME NEW ROMAN',15,'bold'),width='38')
        self.TITLE.grid(row=0,column=0)
        # -------------------------------

        # ENTRY FRAME
        # -------------  ENTRY  ------------------
        self.lblLogin=Label(Entry_Frame,width=20,text='USERNAME')
        self.lblLogin.grid(row=0,column=0)
        self.Login_Entry = Entry(Entry_Frame, width=50)
        self.Login_Entry.grid(row=0, column=1, padx=5, pady=5)

        self.lblPHONE = Label(Entry_Frame, width=20, text='PHONE')
        self.lblPHONE.grid(row=1, column=0)
        self.PHONE_Entry = Entry(Entry_Frame, width=50)
        self.PHONE_Entry.grid(row=1, column=1, padx=5, pady=5)

        self.lblPASSWORD = Label(Entry_Frame, width=20, text='PASSWORD')
        self.lblPASSWORD.grid(row=2, column=0)
        self.PASSWORD_Entry = Entry(Entry_Frame, width=50,show="*")
        self.PASSWORD_Entry.grid(row=2, column=1, padx=5, pady=5)

        self.lblCPass = Label(Entry_Frame, width=20, text='CONFIRM PASSWORD')
        self.lblCPass.grid(row=3, column=0)
        self.CPass_Entry = Entry(Entry_Frame, width=50, show="*")
        self.CPass_Entry.grid(row=3, column=1, padx=5, pady=5)
        # -------------------------------

        # BUTTON FRAME
        # -------------  BUTTON  ------------------
        self.btnRegister=Button(Button_Frame,width=65,text='REGISTER', command=lambda: print(''))
        self.btnRegister.grid(row=0,column=0)
        self.btnExit = Button(Button_Frame, width=65, text='EXIT',command=lambda: self.destroy())
        self.btnExit.grid(row=1,column=0)