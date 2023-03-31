import random
import arcade


class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.color = arcade.color.GREEN
        self.radius = 15
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 3

    def move(self):
        self.center_x += self.change_x + self.speed
        self.center_y += self.change_y + self.speed

    def draw(self):
        arcade.draw_circle_filled(
            self.center_x, self.center_y, self.radius, self.color)


class Rocket(arcade.Sprite):
    def __init__(self, x, y, c, n):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.name = n
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.speed = 4
        self.score = 0

    def move(self):
        ...

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=720, height=480, title="Pong 🏓")
        arcade.set_background_color(arcade.color.DARK_JUNGLE_GREEN)
        self.player_1 = Rocket(
            40, self.height//2, arcade.color.RED, "player 1")
        self.player_2 = Rocket(self.width-40, self.height //
                               2, arcade.color.BLUE, "player 2")
        self.ball = Ball(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(
            self.width//2, self.height//2, self.width-10, self.height-10, arcade.color.WHITE_SMOKE, border_width=25)
        arcade.draw_line(self.width//2, 15, self.width//2,
                         self.height-15, arcade.color.WHITE_SMOKE, line_width=15)
        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        if 45 < y < self.height - 45:
            self.player_1.center_y = y

    def on_update(self, delta_time):
        self.ball.move()


if __name__ == "__main__":
    game = Game()
    arcade.run()
