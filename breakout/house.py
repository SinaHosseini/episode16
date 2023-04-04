import random
import arcade

class House(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        self.width = 58
        self.height = 28