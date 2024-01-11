from View import ViewCar
from Controller.ControllerCar import ControllerCar
from Model.ModelCar import Model_Cars


server = 'Admin-PC'
database = 'CAR_MANAGEMENT_SYSTEM'

viewCar = ViewCar(server, database)
modelCar = Model_Cars(server, database)
controllerCar = ControllerCar(viewCar, modelCar, server, database)

viewCar.mainloop()
