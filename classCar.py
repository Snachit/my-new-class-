class Car:
    def __init__(self, speed, color, nitro_speed, model):
        self.speed = speed
        self.color = color
        self.nitro_speed = nitro_speed
        self.model = model
    
    def turn(self, direction):
        print(f"the car turn {direction}")

    def accelerate(self):
        self.speed += 10 
        print(f"the car accelerate to  {self.speed}km/h")
    
    def brak(self):
        self.speed -= 10
        print(f"the car slow down to {self.speed}km/h")

    def boost(self):
        if self.nitro_speed :
            self.speed +=50
            print(f"boost activated! speed is {self.speed} km/h")

car1 = Car(100, "red", True, "Ferrari")
car1.boost()
car1.brak()
car1.accelerate()