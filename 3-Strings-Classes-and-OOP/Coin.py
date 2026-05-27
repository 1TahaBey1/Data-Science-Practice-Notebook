#Q5
import random 
class Coin:
    
    def __init__(self):
        self.sideup = "heads"
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "heads"
        else:
            self.sideup = "tails" 
    
    def get_sideup(self):
        return self.sideup
    
coin1 = Coin()
print("this side is " + coin1.get_sideup())
print("I'm tossing the coin")
coin1.toss()
print("This side is up ", coin1.get_sideup())