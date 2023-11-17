class player:
    def __init__( self, name, age, rank):

        self.name=name
        self.age=age
        self.rank=rank;

    def Pass(self):
        print(f"{self.name} pass the ball")

    def Shoot(self):
        print(f"{self.name} shoot the ball to the goal")

    def Jump(self):
        print(f"{self.name} jumpe")

# main programme
player1 = player("Messi", 19, 1)
player1.Pass() 
player1.Shoot()
player1.Jump() 