import arcade


class Rocket(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = arcade.color.GRAY
        self.change_x = 0
        self.change_y = 0
        self.width = 80
        self.height = 10
        self.speed = 3
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__()


class House(arcade.Sprite):
    def __init__(self):
        super().__init__()


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=600, title="Break out")
        arcade.set_background_color(arcade.color.NAVY_BLUE)
        self.rocket = Rocket(self.width//2, 40)

    def on_draw(self):
        arcade.start_render()
        self.rocket.draw()

        arcade.finish_render()


if __name__ == "__main__":
    game = Game()
    arcade.run()
