from Auto import *
from AutoElectrico import *

auto = Auto("Toyota", "Corolla", 500)
auto.marca = 'Nissan'
auto.modelo = 'March'

auto.mostrar_info()

auto2 = AutoElectrico('Toyota', 'Prius', 5000, '43')
auto2.marca = 'Huawuei'
auto2.modelo = 'Smart'
auto2.mostrar_info()