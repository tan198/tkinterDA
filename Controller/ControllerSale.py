from database.connectdb import Connect
from tkinter import ttk, messagebox
import tkinter as tk
from Model.ModelSale import *
from View.formSale import *


class ControllerSale:
    def __init__(self, view, model, server, database, username=None, password=None):
        self.view = view
        self.model = model

        self.selected_sale = None

        self.ID_Entry = self.view.ID_Entry
        self.FirstName_Entry = self.view.FirstName_Entry
        self.LastName_Entry = self.view.LastName_Entry
        self.BasicSalary_Entry = self.view.BasicSalary_Entry
        self.SignCon_Entry = self.view.SignCon_Entry
        self.RFC_Entry = self.view.RFC_Entry
        self.HireDate_Entry = self.view.HireDate_Entry
        self.Age_Entry = self.view.Age_Entry
        self.Gender_Entry = self.view.Age_Entry
        self.Email_Entry = self.view.Age_Entry
        self.PhoneNumber_Entry = self.view.Age_Entry
        self.Search_Entry = self.view.Search_Entry
        super().__init__()

        self.connectt = Connect(server, database, username, password)
        self.dsSales = []
        self.view.buttons["INSERT"].config(command=lambda: self.add_sales())
        self.view.buttons["UPDATE"].config(command=lambda: self.update_sale())
        self.view.buttons["DELETE"].config(command=lambda: self.delete_sale())
        self.view.buttons["LOAD"].config(command=lambda: self.load_sale())
        self.view.buttons1["SEARCH"].config(command=lambda: self.search_sale())

        self.view.treeview.bind("<Double-1>", self.load_treeview)

    def load_sale(self):
        try:
            self.model.load_sales()

            for row in self.view.treeview.get_children():
                self.view.treeview.delete(row)

            for index, sales in enumerate(self.model.dsSales, start=1):
                self.view.treeview.insert('', 'end', values=(
                    index,
                    sales['SalespersonID'],
                    sales['FirstName'],
                    sales['LastName'],
                    sales['BasicSalary'],
                    sales['SignedContracts'],
                    sales['RevenueFromContracts'],
                    sales['HireDate'],
                    sales['Age'],
                    sales['Gender'],
                    sales['Email'],
                    sales['PhoneNumber']
                ))
            # self.update_treeview()
            messagebox.showinfo("Thành công", "Tải danh sách xe thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def update_treeview(self):
        print("Cập nhật dữ liệu trong Treeview")
        # Xóa dữ liệu cũ trong Treeview
        for row in self.view.treeview.get_children():
            self.view.treeview.delete(row)

        # Hiển thị dữ liệu mới trong Treeview
        for index, sales in enumerate(self.model.dsSales, start=1):
            self.view.treeview.insert('', 'end', values=(
                index,
                sales['SalespersonID'],
                sales['FirstName'],
                sales['LastName'],
                sales['BasicSalary'],
                sales['SignedContracts'],
                sales['RevenueFromContracts'],
                sales['HireDate'],
                sales['Age'],
                sales['Gender'],
                sales['Email'],
                sales['PhoneNumber']
            ))

    def add_sales(self):
        try:
            SalespersonID = self.view.ID_Entry
            FirstName = self.view.FirstName_Entry
            LastName = self.view.LastName_Entry
            BasicSalary = self.view.BasicSalary_Entry
            SignedContracts = self.view.SignCon_Entry
            RevenueFromContracts = self.view.RFC_Entry
            HireDate = self.view.HireDate_Entry
            Age = self.view.Age_Entry
            Gender = self.view.Gender_Entry
            Email = self.view.Email_Entry
            PhoneNumber = self.view.PhoneNumber_Entry

            self.model.create_sales(SalespersonID, FirstName, LastName,
                                    BasicSalary, SignedContracts, RevenueFromContracts, HireDate, Age, Gender,
                                    Email, PhoneNumber)

            self.model.load_sales()
            self.update_treeview()
            messagebox.showinfo("Thành công", "Thêm xe thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def update_sale(self):
        try:
            SalespersonID = self.view.SalespersonID
            FirstName = self.view.FirstName
            LastName = self.view.LastName_Entry
            BasicSalary = self.view.BasicSalary_Entry
            SignedContracts = self.view.SignCon_Entry
            RevenueFromContracts = self.view.RFC_Entry
            HireDate = self.view.HireDate_Entry
            Age = self.view.Age_Entry
            Gender = self.view.Gender_Entry
            Email = self.view.Email_Entry
            PhoneNumber = self.view.PhoneNumber_Entry

            self.model.update_sales(SalespersonID, FirstName, LastName,
                                    BasicSalary, SignedContracts, RevenueFromContracts, HireDate, Age, Gender,
                                    Email, PhoneNumber)
            self.model.load_sales()
            self.update_treeview()
            messagebox.showinfo("Thông báo", f"Chỉnh sửa chỉnh sửa có mã  {SalespersonID} thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def load_treeview(self, event):
        try:
            # Xác định hàng được chọn
            selected_item = self.view.treeview.selection()
            if selected_item:
                # Lấy giá trị Mã NV từ hàng được chọn

                selected_id = self.view.treeview.item(selected_item, 'values')[1]
                selected_id = int(selected_id)
                print(f"Selected ID: {type(selected_id)}")

                self.selected_sale = next((sales for sales in self.model.dsSales if sales['SalespersonID'] == selected_id), None)
                print(f"Selected Car: {self.selected_sale}")
                if self.selected_sale:
                    print(f"Selected Car: {self.selected_sale}")
                    print(f"Before update - ID_Entry: {self.view.ID_Entry.get()}")
                    # Load dữ liệu lên các widget Entry
                    self.view.ID_Entry.delete(0, tk.END)
                    self.view.ID_Entry.insert(0, self.selected_sale['SalespersonID'])

                    self.view.FirstName_Entry.delete(0, tk.END)
                    self.view.FirstName_Entry.insert(0, self.selected_sale['FirstName'])

                    self.view.LastName_Entry.delete(0, tk.END)
                    self.view.LastName_Entry.insert(0, self.selected_sale['LastName'])

                    self.view.BasicSalary_Entry.delete(0, tk.END)
                    self.view.BasicSalary_Entry.insert(0, self.selected_sale['BasicSalary'])

                    self.view.SignCon_Entry.delete(0, tk.END)
                    self.view.SignCon_Entry.insert(0, self.selected_sale['SignedContracts'])

                    self.view.RFC_Entry.delete(0, tk.END)
                    self.view.RFC_Entry.insert(0, self.selected_sale['RevenueFromContracts'])

                    self.view.HireDate_Entry.delete(0, tk.END)
                    self.view.HireDate_Entry    .insert(0, self.selected_sale['HireDate'])

                    self.view.Age_Entry.delete(0, tk.END)
                    self.view.Age_Entry.insert(0, self.selected_sale['Age'])

                    self.view.Gender_Entry.delete(0, tk.END)
                    self.view.Gender_Entry.insert(0, self.selected_sale['Gender'])

                    self.view.Email_Entry.delete(0, tk.END)
                    self.view.Email_Entry.insert(0, self.selected_sale['Email'])

                    self.view.PhoneNumber_Entry.delete(0, tk.END)
                    self.view.PhoneNumber_Entry.insert(0, self.selected_sale['PhoneNumber'])
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def delete_sale(self):
        selected_item = self.view.treeview.selection()[0]
        selected_index = self.view.treeview.index(selected_item)

        selected_id = self.view.treeview.item(selected_item, 'values')[1]
        print(f"Selected ID: {selected_id}")

        if selected_id and selected_id.strip():

            self.model.delete_sales(selected_id)

            self.model.load_sales()
            self.update_treeview()
            messagebox.showinfo("Thông báo", "Xóa nhân viên thành công.")
        else:
            messagebox.showwarning("Cảnh báo", "Chưa chọn nhân viên để xóa.")

    def search_sale(self):

        search = self.Search_Entry.get()
        search = int(search)
        data = self.model.search_sales(search)
        print(f"Day la: {type(data)}")
        if data:
            self.view.treeview.delete(*self.view.treeview.get_children())
            for index, sales in enumerate(data, start=1):
                self.view.treeview.insert('', 'end', values=(
                    index,
                    sales.SalespersonID,
                    sales.FirstName,
                    sales.LastName,
                    sales.BasicSalary,
                    sales.SignedContracts,
                    sales.RevenueFromContracts,
                    sales.HireDate,
                    sales.Age,
                    sales.Gender,
                    sales.Email,
                    sales.PhoneNumber
                ))
        else:
            messagebox.showinfo("Thông báo", "Không tìm thấy nhân viên!")
