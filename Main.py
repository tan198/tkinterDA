from View.formQL import ViewQL
from View.ViewCar import ViewCar
from View.formNV import ViewNV
from View.formSale import ViewSale
from View.formRegister import ViewRes

from Controller.ControllerCar import ControllerCar
from Controller.ControllerSale import ControllerSale
from Model.ModelSale import ModelSale
from Model.ModelCar import ModelCar

server = 'ADMIN-PC'
database = 'CAR_MANAGEMENT_SYSTEM'

def runformQL():
    view = ViewQL(server, database)
    model = ModelCar(server, database)
#    controller = ControllerCar(view, model, server, database)
    view.mainloop()
def runformNV():
    view = ViewNV(server, database)
    model = ModelCar(server, database)
    controller = ControllerCar(view, model, server, database)
    view.mainloop()

def runviewQLX():
    view = ViewCar(server, database)
    model = ModelCar(server, database)
    controller = ControllerCar(view, model, server, database)
    view.mainloop()

def runviewSale():
    view = ViewSale(server, database)
    model = ModelSale(server, database)
    controller = ControllerSale(view, model, server, database)
    view.mainloop()

def runRegister():
    view = ViewRes(server, database)
    model = ModelCar(server, database)
    controller = ControllerCar(view, model, server, database)
    view.mainloop()
