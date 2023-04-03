import arcade


class Rocket(arcade.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = arcade.color.GRAY
        self.change_x = 0
        self.width = 80
        self.height = 10
        self.speed = 3
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)
        
    def move(self):
        if self.change_x == 1:
            if self.center_x < self.game.width - 40:
                self.center_x += self.speed

        elif self.change_x == -1:
            if self.center_x > 40:
                self.center_x -= self.speed


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__()


class House(arcade.Sprite):
    def __init__(self):
        super().__init__()


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=600, title="Breakout")
        arcade.set_background_color(arcade.color.NAVY_BLUE)
        self.rocket = Rocket(self, self.width//2, 40)

    def on_draw(self):
        arcade.start_render()
        self.rocket.draw()

        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        if 40 < x < self.width - 40:
            self.rocket.center_x = x

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.rocket.change_x = 1

        if symbol == arcade.key.LEFT:
            self.rocket.change_x = -1

    def on_key_release(self, symbol, modifiers):
        self.rocket.change_x = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()
