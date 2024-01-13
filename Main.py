from View.ViewCar import ViewCar
from Controller.ControllerCar import ControllerCar
from Model.ModelCar import ModelCar


server = 'ADMIN-PC'
database = 'CAR_MANAGEMENT_SYSTEM'

view = ViewCar(server, database)
model = ModelCar(server, database)
controller = ControllerCar(view, model, server, database)

view.mainloop()
