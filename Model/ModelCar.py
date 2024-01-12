from database.connectdb import Connect


class ModelCar:
    def __init__(self, server, database, username=None, password=None):

        self.connectt = Connect(server, database, username, password)
        self.dsCars = []

    def load_car(self):
        try:
            query = """
                SELECT * FROM CARS WHERE CarID=?;
            """
            result = self.connectt.execute_query(query).fetchall()

            self.dsCars = []
            for row in result:
                carID, make, model, year, transmission, bodytype, category, price = row

                cars = {'CarID': carID, 'Make': make, 'Model': model, 'Year': year, 'Transmission': transmission,
                        'BodyType': bodytype, 'Category': category, 'Price': price}
                self.dsCars.append(cars)

            print("Loading Cars Successfully.")
        except Exception as e:
            print(f"Error loading Cars:{e} ")

    def create_car(self, carid, make, model, year, transmission, bodytype, category, price):
        try:
            query = f"""
                INSERT INTO Cars(CarID, Make, Model, Year, Transmission, BodyType, Category, Price)
                VALUES('{carid}', N'{make}', N'{model}', N'{year}', N'{transmission}', N'{bodytype}', N'{category}',
                 N'{price}');       
            """
            self.connectt.execute(query)
            self.connectt.commit()
            print(f"Add Cars {carid} Successfully.")
        except Exception as e:
            print(f"Error Add Cars {carid}: {e}")

    def update_cars(self, carid, make, model, year, transmission, bodytype, category, price):
        try:
            query = f"""
                UPDATE CARS SET Make = '{make}',Model = '{model}',Year = '{year}',Transmission = '{transmission}', 
                BodyType = '{bodytype}',Category = '{category}',Price = '{price}' WHERE CarID = '{carid}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Update Car {carid} successfully")
            self.connectt.close()
        except Exception as e:
            print(f"Error updating {carid} fail: {e}")

    def delete_cars(self, carid):
        try:
            query = f"""
                DELETE FROM CARS WHERE CarID = '{carid}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Delete Car {carid} Successfully")
            self.connectt.close()
        except Exception as e:
            print(f"Error Delete {carid} Fails: {e}")

    def search_car(self, carid):
        try:
            query = f"""
                SELECT * FROM Cars WHERE CarID = {carid},
            """
            check = self.connectt.execute_query(query).fetchone()[0]

            if check == 0:
                print(f"Car {carid} is not existed")
                return
            self.connectt.commit()
            self.connectt.close()
        except Exception as e:
            print(f"Error Searching {carid}: {e}")
