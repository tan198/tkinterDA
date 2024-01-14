from tkinter import *
from tkinter import ttk
import tkinter as tk
from database import connectdb

class ViewSale(tk.Tk):
    def __init__(self,server,database):
        super().__init__()
        self.title('CAR MANAGERMENT SYSTEM')
        self.geometry('1200x660')
        self.config(bg='lightblue')
        self.stt_counter = 0
        self.ket_noi = connectdb.Connect(server, database)

        MainFrame = Frame(self.master,bg='lightblue', padx=10)
        MainFrame.grid()

        # TITLE FRAME
        TitleFrame=LabelFrame(MainFrame,width=1200,height=50,bg='lightblue',relief=RIDGE, bd=0,pady=10)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame,width=40,font=('arial', 20), text='SALE MANAGERMENT',bg='lightblue', bd=0)
        self.lblTitle.grid()


        # MID FRAME

        MidFrame = LabelFrame(MainFrame, width=1100, height=400, bg='lightblue', relief=RIDGE, padx=20, pady=10, bd=0)
        MidFrame.pack(side=TOP)
        # TEXTBOX FRAME
        TextboxFrame = LabelFrame(MidFrame, width=400, height=200, bg='lightblue', relief=RIDGE, bd=1, pady=10, padx=10)
        TextboxFrame.pack(side=LEFT)
        # -------------------------------------------------------------
        self.lblID=Label(TextboxFrame,width=25,text='Sales ID')
        self.lblID.grid(row=0,column=0)
        self.ID_Entry = Entry(TextboxFrame,width=50)
        self.ID_Entry.grid(row=0,column=1,padx=5,pady=5)

        self.lblFirstName=Label(TextboxFrame,width=25,text='First Name')
        self.lblFirstName.grid(row=1,column=0)
        self.FirstName_Entry = Entry(TextboxFrame, width=50)
        self.FirstName_Entry.grid(row=1, column=1, padx=5, pady=5)

        self.lblLastName=Label(TextboxFrame,width=25,text='Last Name')
        self.lblLastName.grid(row=2,column=0)
        self.LastName_Entry = Entry(TextboxFrame, width=50)
        self.LastName_Entry.grid(row=2, column=1, padx=5, pady=5)

        self.lblBasicSalary=Label(TextboxFrame,width=25,text='Basic Salary')
        self.lblBasicSalary.grid(row=3,column=0)
        self.BasicSalary_Entry = Entry(TextboxFrame, width=50)
        self.BasicSalary_Entry.grid(row=3, column=1, padx=5, pady=5)

        self.lblSignCon=Label(TextboxFrame,width=25,text='Signed Contracts')
        self.lblSignCon.grid(row=4,column=0)
        self.SignCon_Entry = Entry(TextboxFrame, width=50)
        self.SignCon_Entry.grid(row=4, column=1, padx=5, pady=5)

        self.lblRFC=Label(TextboxFrame,width=25,text='Revenue From Contracts')
        self.lblRFC.grid(row=5,column=0)
        self.RFC_Entry = Entry(TextboxFrame, width=50)
        self.RFC_Entry.grid(row=5, column=1, padx=5, pady=5)

        self.lblHireDate=Label(TextboxFrame,width=25,text='HireDate')
        self.lblHireDate.grid(row=6,column=0)
        self.HireDate_Entry = Entry(TextboxFrame, width=50)
        self.HireDate_Entry.grid(row=6, column=1, padx=5, pady=5)

        self.lblAge=Label(TextboxFrame,width=25,text='Age')
        self.lblAge.grid(row=7,column=0)
        self.Age_Entry = Entry(TextboxFrame, width=50)
        self.Age_Entry.grid(row=7, column=1, padx=5, pady=5)

        self.lblGender=Label(TextboxFrame,width=25,text='Gender')
        self.lblGender.grid(row=8,column=0)
        self.Gender_Entry = Entry(TextboxFrame, width=50)
        self.Gender_Entry.grid(row=8, column=1, padx=5, pady=5)

        self.lblEmail=Label(TextboxFrame,width=25,text='Email')
        self.lblEmail.grid(row=9,column=0)
        self.Email_Entry = Entry(TextboxFrame, width=50)
        self.Email_Entry.grid(row=9, column=1, padx=5, pady=5)

        self.lblPhoneNumber=Label(TextboxFrame,width=25,text='PhoneNumber')
        self.lblPhoneNumber.grid(row=10,column=0)
        self.PhoneNumber_Entry = Entry(TextboxFrame, width=50)
        self.PhoneNumber_Entry.grid(row=10, column=1, padx=5, pady=5)
        # -------------------------------------------------------------
        # RIGHT MID FRAME
        Mid2Frame = LabelFrame(MidFrame, width=400, height=200, bg='lightblue', relief=RIDGE, bd=1, padx=20,pady=23)
        Mid2Frame.pack(side=RIGHT)
        # BUTTON FRAME
        ButtonFrame = LabelFrame(Mid2Frame,bd=0, width=200, height=200, bg='lightblue', relief=RIDGE,pady=12)
        ButtonFrame.pack(side=LEFT)
        # -------------------------------------------------------------
        self.lblSpace1 = Label(ButtonFrame, width=25, height=1, text='',bg='lightblue')
        self.lblSpace2 = Label(ButtonFrame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace3 = Label(ButtonFrame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace4 = Label(ButtonFrame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace5 = Label(ButtonFrame, width=25, height=1, text='', bg='lightblue')


        self.buttons = {
            "INSERT": tk.Button(ButtonFrame, text="INSERT", width=30,height=2),
            "UPDATE": tk.Button(ButtonFrame, text="UPDATE", width=30,height=2),
            "DELETE": tk.Button(ButtonFrame, text="DELETE", width=30,height=2),
            "LOAD": tk.Button(ButtonFrame, text="LOAD", width=30,height=2)
        }

        self.lblSpace1.grid(row=0, column=0)
        self.buttons["INSERT"].grid(row=1, column=0)
        self.lblSpace2.grid(row=2, column=0)
        self.buttons["UPDATE"].grid(row=3, column=0, padx=20)
        self.lblSpace3.grid(row=4, column=0)
        self.buttons["DELETE"].grid(row=5, column=0, padx=20)
        self.lblSpace4.grid(row=6, column=0)
        self.buttons["LOAD"].grid(row=7, column=0, padx=20)
        self.lblSpace5.grid(row=8, column=0)
        # -------------------------------------------------------------

        # SEARCH FRAME
        SEARCHFrame = LabelFrame(Mid2Frame, width=200, height=200, bg='lightblue', relief=RIDGE, pady=12, padx=20, bd=0)
        SEARCHFrame.pack(side=RIGHT)
        # -------------------------------------------------------------
        self.lblSpace6 = Label(SEARCHFrame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace7 = Label(SEARCHFrame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace8 = Label(SEARCHFrame, width=25, height=1, text='', bg='lightblue')
        self.lblSpace9 = Label(SEARCHFrame, width=25, height=1, text='', bg='lightblue')

        self.lblSpace6.grid(row=0, column=0)
        self.lblSearch = Label(SEARCHFrame, width=19,font=('TIME NEW ROMAN',15), text='Search',height=1)
        self.lblSearch.grid(row=1, column=0)

        self.lblSpace7.grid(row=2, column=0)
        self.Search_Entry = Entry(SEARCHFrame, width=14, font=('TIME NEW ROMAN',20))
        self.Search_Entry.grid(row=3, column=0, padx=5, pady=5)

        self.lblSpace8.grid(row=4, column=0)
        self.buttons1 = {
            "SEARCH": tk.Button(SEARCHFrame, text="SEARCH", width=30, relief=RIDGE, height=2),
        }
        self.buttons1["SEARCH"].grid(row=5, column=0)

        self.lblSpace9.grid(row=6, column=0)
        # -------------------------------------------------------------

        # TREEVIEW FRAME
        TreeFrame = LabelFrame(MainFrame, width=1100, height=200, bg='lightblue', relief=RIDGE, bd=5)
        TreeFrame.pack(side=TOP)

        sb = Scrollbar(TreeFrame)
        self.treeview = ttk.Treeview(TreeFrame,
        columns=('', 'SalespersonID', 'FirstName', 'LastName', 'BasicSalary',
                 'SignedContracts', 'RevenueFromContracts', 'HireDate','Age',
                 'Gender','Email','PhoneNumber'),
                                     show=["headings"], yscrollcommand=sb.set)
        self.treeview.heading('', text='')
        self.treeview.heading('SalespersonID', text='ID')
        self.treeview.heading('FirstName', text='FirstName')
        self.treeview.heading('LastName', text='LastName')
        self.treeview.heading('BasicSalary', text='BasicSalary')
        self.treeview.heading('SignedContracts', text='SignedContracts')
        self.treeview.heading('RevenueFromContracts', text='Revenue From Contracts')
        self.treeview.heading('HireDate', text='HireDate')
        self.treeview.heading('Age', text='Age')
        self.treeview.heading('Gender', text='Gender')
        self.treeview.heading('Email', text='Email')
        self.treeview.heading('PhoneNumber', text='Phone Number')


        self.treeview.column('', width=20, anchor=tk.CENTER)
        self.treeview.column('SalespersonID', width=40, anchor=tk.CENTER)
        self.treeview.column('FirstName', width=100, anchor=tk.CENTER)
        self.treeview.column('LastName', width=100, anchor=tk.CENTER)
        self.treeview.column('BasicSalary', width=120, anchor=tk.CENTER)
        self.treeview.column('SignedContracts', width=100, anchor=tk.CENTER)
        self.treeview.column('RevenueFromContracts', width=150, anchor=tk.CENTER)
        self.treeview.column('HireDate', width=120, anchor=tk.CENTER)
        self.treeview.column('Age', width=80, anchor=tk.CENTER)
        self.treeview.column('Gender', width=100, anchor=tk.CENTER)
        self.treeview.column('Email', width=120, anchor=tk.CENTER)
        self.treeview.column('PhoneNumber', width=120, anchor=tk.CENTER)

        self.treeview.grid(row=7, column=0, columnspan=7)
        sb.grid(row=7, column=6, sticky='ns')