from View.ViewCar import ViewCars
from Controller.ControllerCar import ControllerCar
from Model.ModelCar import ModelCar


server = 'ADMIN-PC'
database = 'CAR_MANAGEMENT_SYSTEM'

view = ViewCars(server, database)
model = ModelCar(server, database)
controller = ControllerCar(view, model, server, database)

view.mainloop()
