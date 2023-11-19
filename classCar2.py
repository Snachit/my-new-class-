class Car:

    def __init__(self,speed,color,enginePower,name):
        self.speed = speed
        self.color = color
        self.enginePower = enginePower
        self.name = name

    def start(self):
        print("Car starting")

    def stop(self):
        print("Car stopping")

    def change_gear(self):
        print("Car changig gear")