from database.connectdb import Connect


class ModelCar:
    def __init__(self, server, database, username=None, password=None):

        self.connectt = Connect(server, database, username, password)
        self.dsCars = []

    def load_cars(self):
        try:
            query = """
                SELECT * FROM Cars;
            """
            result = self.connectt.execute_query(query).fetchall()

            self.dsCars = []
            for row in result:
                carID, make, model, year, transmission, bodytype, category, price = row

                cars = {'CarID': carID, 'Make': make, 'Model': model, 'Year': year, 'Transmission': transmission,
                        'BodyType': bodytype, 'Category': category, 'Price': price}
                self.dsCars.append(cars)
                print(cars)
            print("Loading Cars Successfully.")
        except Exception as e:
            print(f"Error loading Cars:{e} ")

    def create_cars(self, CarID, Make, Model, Year, Transmission, BodyType, Category, Price):
        try:
            query = f"""
                SET IDENTITY_INSERT Cars ON;
                INSERT INTO Cars(CarID, Make, Model, Year, Transmission, BodyType, Category, Price)
                VALUES('{CarID}', N'{Make}', N'{Model}', N'{Year}', N'{Transmission}', N'{BodyType}', N'{Category}',
                 N'{Price}');
                SET IDENTITY_INSERT Cars OFF;    
            """
            self.connectt.execute(query)
            self.connectt.commit()
            print(f"Add Cars {CarID} Successfully.")
        except Exception as e:
            print(f"Error Add Cars {CarID}: {e}")

    def update_cars(self, carID, make, model, year, transmission, bodytype, category, price):
        try:
            query = f"""
                UPDATE CARS SET Make = '{make}',Model = '{model}',Year = '{year}',Transmission = '{transmission}', 
                BodyType = '{bodytype}',Category = '{category}',Price = '{price}' WHERE CarID = '{carID}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Update Car {carID} successfully")

        except Exception as e:
            print(f"Error updating {carID} fail: {e}")

    def delete_cars(self, carID):
        try:
            query = f"""
                DELETE FROM CARS WHERE CarID = '{carID}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Delete Car {carID} Successfully")
        except Exception as e:
            print(f"Error Delete {carID} Fails: {e}")

    def search_car(self, carID):
        try:
            query = f"""
                SELECT * FROM Cars WHERE CarID = {carID},
            """
            check = self.connectt.execute_query(query).fetchone()[0]

            if check == 0:
                print(f"Car {carID} is not existed")
                return
            self.connectt.commit()
        except Exception as e:
            print(f"Error Searching {carID}: {e}")
