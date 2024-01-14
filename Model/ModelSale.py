from database.connectdb import Connect


class ModelSale:
    def __init__(self, server, database, username=None, password=None):

        self.connectt = Connect(server, database, username, password)
        self.dsSales = []

    def load_sales(self):
        try:
            query = """
                SELECT * FROM Salespeople;
            """
            result = self.connectt.execute_query(query).fetchall()

            self.dsSales = []
            for row in result:
                (SalespersonID, FirstName, LastName, BasicSalary,
                 SignedContracts, RevenueFromContracts, HireDate, Age, Gender, Email, PhoneNumber) = row

                sales = {'SalespersonID': SalespersonID, 'FirstName': FirstName, 'LastName': LastName,
                         'BasicSalary': BasicSalary, 'SignedContracts': SignedContracts,
                         'RevenueFromContracts': RevenueFromContracts, 'HireDate': HireDate, 'Age': Age
                    , 'Gender': Gender, 'Email': Email, 'PhoneNumber': PhoneNumber}
                self.dsSales.append(sales)
            print("Loading Sales Successfully.")
        except Exception as e:
            print(f"Error loading Sales:{e} ")

    def create_sales(self, SalespersonID, FirstName, LastName, BasicSalary,
                     SignedContracts, RevenueFromContracts, HireDate,
                     Age, Gender, Email, PhoneNumber):
        try:
            query = f"""
                SET IDENTITY_INSERT Salespeople ON;
                INSERT INTO Salespeople(SalespersonID, FirstName, LastName, BasicSalary, SignedContracts, 
                RevenueFromContracts, Age, Gender, Email, PhoneNumber)
                VALUES('{SalespersonID}', N'{FirstName}', N'{LastName}', N'{BasicSalary}', 
                N'{SignedContracts}', N'{RevenueFromContracts}', N'{HireDate}',
                 N'{Age}', , N'{Gender}', N'{Email}', N'{PhoneNumber}');
                SET IDENTITY_INSERT Salespeople OFF;    
            """
            self.connectt.execute(query)
            self.connectt.commit()
            print(f"Add Cars {FirstName} {LastName} Successfully.")
        except Exception as e:
            print(f"Error Add Cars {FirstName} {LastName}: {e}")

    def update_sales(self, SalespersonID, FirstName, LastName, BasicSalary,
                     SignedContracts, RevenueFromContracts, HireDate,
                     Age, Gender, Email, PhoneNumber):
        try:
            query = f"""
                UPDATE CARS SET FirstName = '{FirstName}',LastName = '{LastName}',BasicSalary = '{BasicSalary}',
                SignedContracts = '{SignedContracts}', RevenueFromContracts = '{RevenueFromContracts}',
                HireDate = '{HireDate}',Age = '{Age},Gender = '{Gender},Email = '{Email},PhoneNumber = '{PhoneNumber}' 
                WHERE SalespersonID = '{SalespersonID}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Update Car {SalespersonID} successfully")

        except Exception as e:
            print(f"Error updating {SalespersonID} fail: {e}")

    def delete_sales(self, SalespersonID):
        try:
            query = f"""
                DELETE FROM Salespeople WHERE SalespersonID = '{SalespersonID}';
                """
            self.connectt.execute_query(query)
            self.connectt.commit()
            print(f"Delete Car {SalespersonID} Successfully")
        except Exception as e:
            print(f"Error Delete {SalespersonID} Fails: {e}")

    def search_sales(self, SalespersonID):
        try:
            query = f"""
                SELECT * FROM Salespeople WHERE SalespersonID = '{SalespersonID}';
            """
            check = self.connectt.execute_query(query).fetchall()

            # print(check)
            if check == 0:
                print(f"Sales {SalespersonID} is not existed")
                return

            self.connectt.commit()
            return check
        except Exception as e:
            print(f"Error Searching {SalespersonID}: {e}")
