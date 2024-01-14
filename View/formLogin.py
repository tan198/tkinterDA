from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pyodbc
from database import connectdb
import Main

def runMain(username, password):
    # Hàm chính của chương trình
    server = 'DESKTOP-6F8AHFS'
    database = 'CAR_MANAGEMENT_SYSTEM'
    print('chay den roi')
    Main.runMain()

# ---------------------------------------------------

class ViewLogin(tk.Tk):
    def __init__(self,server,database):
        super().__init__()
        self.title('LOG IN')
        self.geometry('460x285')
        self.config(bg='lightblue')
        self.stt_counter = 0
        self.ket_noi = connectdb.Connect(server, database)

        LoginFrame = Frame(self.master,bg='lightblue', padx=22, pady=20)
        LoginFrame.grid()



        # TITLE FRAME
        Title_Frame=LabelFrame(LoginFrame,width=400,height=50, padx=10, pady=10,bg='lightblue', bd=0)
        Title_Frame.pack(side=TOP)
        # ENTRY FRAME
        Entry_Frame = LabelFrame(LoginFrame, width=400, height=150, padx=10, pady=10,bg='lightblue', bd=0)
        Entry_Frame.pack(side=TOP)
        # ENTRY FRAME
        Button_Frame = LabelFrame(LoginFrame, width=400, height=150, padx=10, pady=10,bg='lightblue', bd=0)
        Button_Frame.pack(side=TOP)
        # ENTRY FRAME
        # frame4 = LabelFrame(LoginFrame, width=600, height=100)
        # frame4.pack(side=TOP)

        # TITLE FRAME
        # -------------  TITLE  ------------------
        self.TITLE = Label(Title_Frame, text='LOG IN', font=('TIME NEW ROMAN',15,'bold'), bg='lightblue', width='32')
        self.TITLE.grid(row=0,column=0)
        # -------------------------------

        # ENTRY FRAME
        # -------------  ENTRY  ------------------
        self.lblLogin=Label(Entry_Frame,width=10,text='USERNAME', bg='lightblue',)
        self.lblLogin.grid(row=0,column=0)
        self.loginEntry = Entry(Entry_Frame, width=50)
        self.loginEntry.grid(row=0, column=1, padx=5, pady=5)

        self.lblPass = Label(Entry_Frame, width=10, text='PASSWORD', bg='lightblue',)
        self.lblPass.grid(row=1, column=0)
        self.passEntry = Entry(Entry_Frame, width=50,show="*")
        self.passEntry.grid(row=1, column=1, padx=5, pady=5)
        # -------------------------------

        # BUTTON FRAME
        # -------------  BUTTON  ------------------
        self.btnLogin=Button(Button_Frame, width=50, height=1, text='LOG IN',font=('TIME NEW ROMAN',10,'bold'), command=lambda: self.login())
        self.btnLogin.grid(row=0,column=0)
        self.lblSpace = Label(Button_Frame, width=10,font=('TIME NEW ROMAN',5), text='', bg='lightblue',)
        self.lblSpace.grid(row=1, column=0)
        self.btnEXIT = Button(Button_Frame, width=50, height=1, text='EXIT', font=('TIME NEW ROMAN',10,'bold'),command=lambda: self.destroy())
        self.btnEXIT.grid(row=2, column=0)

    # --------------------------------------------------

    def login(self):
        # Lấy thông tin đăng nhập từ người dùng
        username = self.loginEntry.get()
        print(username)
        password = self.passEntry.get()
        print(password)

        # Kiểm tra thông tin đăng nhập với CSDL
        if self.check_user(username, password):
            # Nếu đăng nhập thành công, đóng cửa sổ đăng nhập và chạy chương trình chính
            self.destroy()
            runMain(username, password)
        else:
            messagebox.showerror("Đăng nhập không thành công", "Tên người dùng hoặc mật khẩu không đúng.")

    def check_user(self, username, password):
        try:
            # Kết nối đến CSDL
            connection = pyodbc.connect(
                "DRIVER={SQL Server};SERVER=DESKTOP-6F8AHFS;DATABASE=CAR_MANAGEMENT_SYSTEM;Trusted_Connection=yes")
            cursor = connection.cursor()

            # Truy vấn kiểm tra thông tin đăng nhập
            query = f"SELECT * FROM Account WHERE tk = ? AND mk = ?"
            result = cursor.execute(query, username, password).fetchone()

            # Đóng kết nối
            cursor.close()
            connection.close()

            return result is not None
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi kiểm tra thông tin đăng nhập: {e}")
            return False
# ----------------------------------------------------------

if __name__ == '__main__':
    server = 'DESKTOP-6F8AHFS'
    database = 'CAR_MANAGEMENT_SYSTEM'

    view = ViewLogin(server, database)
    view.mainloop()