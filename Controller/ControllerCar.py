from database.connectdb import Connect
from tkinter import ttk, messagebox
import tkinter as tk
from Model.ModelCar import *
from View.ViewCar import *

class ControllerCar:
    def __init__(self, view, model, server, database, username=None, password=None):
        self.view = view
        self.model = model

        self.selected_car = None

        self.ID_Entry = self.view.ID_Entry
        self.Make_Entry = self.view.Make_Entry
        self.Model_Entry = self.view.Model_Entry
        self.Year_Entry = self.view.Year_Entry
        self.Transmission_Entry = self.view.Transmission_Entry
        self.Body_Entry = self.view.Body_Entry
        self.Category_Entry = self.view.Category_Entry
        self.Price_Entry = self.view.Price_Entry
        super().__init__()

        self.connectt = Connect(server, database, username, password)
        self.dsCars = []
        self.view.buttons["INSERT"].config(command=lambda: self.add_car())
        self.view.buttons["UPDATE"].config(command=lambda: self.update_car())
        self.view.buttons["DELETE"].config(command=lambda: self.delete_car())
        self.view.buttons["LOAD"].config(command=lambda: self.load_car())

        self.view.treeview.bind("<Double-1>", self.load_treeview)

    def load_car(self):
        try:
            self.model.load_cars()

            for row in self.view.treeview.get_children():
                self.view.treeview.delete(row)

            for index, cars in enumerate(self.model.dsCars, start=1):
                self.view.treeview.insert('', 'end', values=(
                    index,
                    cars['CarID'],
                    cars['Make'],
                    cars['Model'],
                    cars['Year'],
                    cars['Transmission'],
                    cars['BodyType'],
                    cars['Category'],
                    cars['Price']
                ))
            #self.update_treeview()
            messagebox.showinfo("Thành công", "Tải danh sách xe thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def update_treeview(self):
        print("Cập nhật dữ liệu trong Treeview")
        # Xóa dữ liệu cũ trong Treeview
        for row in self.view.treeview.get_children():
            self.view.treeview.delete(row)

        # Hiển thị dữ liệu mới trong Treeview
        for index, cars in enumerate(self.model.dsCars, start=1):
            # print(f"Thêm dữ liệu mới vào Treeview: {nv._maNV}, {nv._hoTen}, {nv._luongCoBan}, {nv._luongHT}")
            self.view.treeview.insert('', 'end', values=(
                index,
                cars['CarID'],
                cars['Make'],
                cars['Model'],
                cars['Year'],
                cars['Transmission'],
                cars['BodyType'],
                cars['Category'],
                cars['Price']
            ))

    def add_car(self):
        try:
            carID = self.view.ID_Entry.get()
            make = self.view.Make_Entry.get()
            model = self.view.Model_Entry.get()
            year = self.view.Year_Entry.get()
            transmission = self.view.Transmission_Entry.get()
            bodytype = self.view.Body_Entry.get()
            category = self.view.Category_Entry.get()
            price = self.view.Price_Entry.get()

            self.model.create_cars(carID, make, model, year, transmission, bodytype, category, price)

            self.model.load_cars()
            self.update_treeview()
            messagebox.showinfo("Thành công", "Thêm xe thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def update_car(self):
        try:
            carID = self.view.ID_Entry.get()
            make = self.view.Make_Entry.get()
            model = self.view.Model_Entry.get()
            year = self.view.Year_Entry.get()
            transmission = self.view.Transmission_Entry.get()
            bodytype = self.view.Body_Entry.get()
            category = self.view.Category_Entry.get()
            price = self.view.Price_Entry.get()

            self.model.update_cars(carID, make, model, year, transmission, bodytype, category, price)
            self.model.load_cars()
            self.update_treeview()
            messagebox.showinfo("Thông báo", f"Chỉnh sửa xe có mã xe {carID} thành công.")
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

                #print(f"All cars in dsCars: {self.model.dsCars}")
                # Tìm nhân viên trong danh sách có mã là selected_id
                self.selected_car = next((cars for cars in self.model.dsCars if cars['CarID'] == selected_id), None)
                print(f"Selected Car: {self.selected_car}")
                print(f"Type of CarID in dsCars: {type(self.model.dsCars[0]['CarID'])}")
                if self.selected_car:
                    print(f"Selected Car: {self.selected_car}")
                    print(f"Before update - ID_Entry: {self.view.ID_Entry.get()}")
                    # Load dữ liệu lên các widget Entry
                    self.view.ID_Entry.delete(0, tk.END)
                    self.view.ID_Entry.insert(0, self.selected_car['CarID'])

                    self.view.Make_Entry.delete(0, tk.END)
                    self.view.Make_Entry.insert(0, self.selected_car['Make'])

                    self.view.Model_Entry.delete(0, tk.END)
                    self.view.Model_Entry.insert(0, self.selected_car['Model'])

                    self.view.Year_Entry.delete(0, tk.END)
                    self.view.Year_Entry.insert(0, self.selected_car['Year'])

                    self.view.Transmission_Entry.delete(0, tk.END)
                    self.view.Transmission_Entry.insert(0, self.selected_car['Transmission'])

                    self.view.Body_Entry.delete(0, tk.END)
                    self.view.Body_Entry.insert(0, self.selected_car['BodyType'])

                    self.view.Category_Entry.delete(0, tk.END)
                    self.view.Category_Entry.insert(0, self.selected_car['Category'])

                    self.view.Price_Entry.delete(0, tk.END)
                    self.view.Price_Entry.insert(0, self.selected_car['Price'])
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def delete_car(self):
        selected_item = self.view.treeview.selection()[0]
        selected_index = self.view.treeview.index(selected_item)

        selected_id = self.view.treeview.item(selected_item, 'values')[1]
        print(f"Selected ID: {selected_id}")

        if selected_id and selected_id.strip():

            self.model.delete_cars(selected_id)

            self.model.load_cars()
            self.update_treeview()
            messagebox.showinfo("Thông báo", "Xóa xe thành công.")
        else:
            messagebox.showwarning("Cảnh báo", "Chưa chọn xe để xóa.")
