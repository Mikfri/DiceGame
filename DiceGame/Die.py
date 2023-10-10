import time
import random

class Die:
    def __init__(self, name):
        self.faceValue = None
        self.name = name

    def getFaceValue(self):
        self.faceValue = random.randint(1, 6)
        print(f"   {self.name} rolled: {self.faceValue}")
        time.sleep(1)
        return self.faceValue
    
    def roll(self):
        print(f"\n{self.name} is rolling...")
        time.sleep(0.7)
        return self.getFaceValue()  # Returnerer den rullede værdi

    # def roll(self):
    #     print(f"\n{self.name} is rolling...")
    #     time.sleep(0.9)
    #     self.faceValue = random.randint(1, 6)
    #     print(f"{self.name} rolled: {self.faceValue}")
    #     time.sleep(1.5)

    
