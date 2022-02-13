from modulefinder import packagePathMap
from tracemalloc import start


class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerating")

    def change_gear(self,gear_type):
        print("Gear Changed")
        "Gear Related Funcationalitity"

Audi = Car("A6","black","Audi",80)
print(Audi.start())
print(Audi.stop())
print(Audi.change_gear(1))