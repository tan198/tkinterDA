from database.connectdb import Connect


class Model_Cars:
    def __init__(self, server, database, username=None, password=None):

        self.connectt = Connect(server, database, username, password)
        self.dsCars = []

    def loadCar(self):
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

    def createCar(self, carID, make, model, year, transmission, bodytype, category, price):
        try:
            query = f"""
                INSERT INTO Cars(CarID, Make, Model, Year, Transmission, BodyType, Category, Price)
                VALUES('{carID}', N'{make}', N'{model}', N'{year}', N'{transmission}', N'{bodytype}', N'{category}', N'{price}');       
            """
            self.connectt.execute(query)
            self.connectt.commit()
            print(f"Add Cars {carID} Successfully.")
        except Exception as e:
            print(f"Error Add Cars {carID}: {e}")

    def updateCars(self, carID, make, model, year, transmission, bodytype, category, price):
        try:
            query = f"""
                UPDATE CARS SET Make = '{make}',Model = '{model}',Year = '{year}',Transmission = '{transmission}',BodyType = '{bodytype}',Category = '{category}',Price = '{price}' WHERE CarID = '{carID}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Update Car {carID} successfully")
            self.connectt.close()
        except Exception as e:
            print(f"Error updating {carID} fail: {e}")

    def deleteCars(self, carID):
        try:
            query = f"""
                DELETE FROM CARS WHERE CarID = '{carID}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Delete Car {carID} Successfully")
            self.connectt.close()
        except Exception as e:
            print(f"Error Delete {carID} Fails")

    def searchCar(self, carID):
        try:
            query = f"""
                SELECT * FROM Cars WHERE CarID = {carID},
            """
            check = self.connectt.execute_query(query).fetchone()[0]

            if check == 0:
                print(f"Car {carID} is not existed")
                return
            self.connectt.commit()
            self.connectt.close()

        except Exception as e:
            print(f"Error Searching {carID}")
