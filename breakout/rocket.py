import arcade

class Rocket(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.center_x = x//2
        self.center_y = y
        self.color = arcade.color.GRAY
        self.change_x = 0
        self.width = 80
        self.height = 10
        self.speed = 5
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)

    def move(self, game):
        if self.change_x == 1:
            if self.center_x < game.width - 40:
                self.center_x += self.speed

        elif self.change_x == -1:
            if self.center_x > 40:
                self.center_x -= self.speed