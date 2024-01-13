from database.connectdb import Connect
from tkinter import messagebox


class ControllerCar:
    def __init__(self, view, model, server, database, username=None, password=None):
        self.view = view
        self.model = model
        super().__init__()

        self.connectt = Connect(server, database, username, password)
        self.dsCars = []
        # self.view.buttons["INSERT"].config(command=lambda: print('INSERT'))
        # self.view.buttons["UPDATE"].config(command=lambda: print('UPDATE'))
        # self.view.buttons["DELETE"].config(command=lambda: print('DELETE'))
        self.view.buttons["LOAD"].config(command=lambda: self.load_car())

        # self.view.treeview.bind("<Double-1>", self.load_treeview)

        # Call a function to populate the TreeView with data from the database

    def load_car(self):
        try:
            self.model.load_cars()

            for row in self.view.treeview.get_children():
                self.view.treeview.delete(row)

            for index, cars in enumerate(self.model.dsCars, start=1):
                self.view.treeview.insert('', 'end', values=(
                    index,
                    cars['CarID'],
                    cars['make'],
                    cars['model'],
                    cars['year'],
                    cars['transmission'],
                    cars['body_type'],
                    cars['category'],
                    cars['price']
                ))
            self.cap_nhat_du_lieu_treeview()
            messagebox.showinfo("Thành công", "Tải danh sách xe thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def cap_nhat_du_lieu_treeview(self):
        print("Cập nhật dữ liệu trong Treeview")
        # Xóa dữ liệu cũ trong Treeview
        for row in self.view.treeview.get_children():
            self.view.treeview.delete(row)

        # Hiển thị dữ liệu mới trong Treeview
        for index, car in enumerate(self.model.dsCars, start=1):
            #print(f"Thêm dữ liệu mới vào Treeview: {nv._maNV}, {nv._hoTen}, {nv._luongCoBan}, {nv._luongHT}")
            self.view.treeview.insert('', 'end', values=(
                index,
                car['carID'],
                car['make'],
                car['model'],
                car['year'],
                car['transmission'],
                car['body_type'],
                car['category'],
                car['price']
            ))
