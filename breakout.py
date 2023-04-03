import random
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


class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = game.height//3
        self.color = arcade.color.GRAY
        self.radius = 10
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 3
        self.width = self.radius*2
        self.height = self.radius*2

    def draw(self):
        arcade.draw_circle_filled(
            self.center_x, self.center_y, self.radius, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class House(arcade.Sprite):
    def __init__(self):
        super().__init__()


class Hearts(arcade.Sprite):
    def __init__(self, x):
        super().__init__("episode16\heart.png")
        self.center_x = x*20 + 20
        self.center_y = 40
        self.width = 15
        self.height = 15


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=600, title="Breakout")
        arcade.set_background_color(arcade.color.NAVY_BLUE)
        self.GM_background = arcade.load_texture(
            "episode16\photo_2023-03-23_21-50-37.jpg")
        self.rocket = Rocket(self.width, 40)
        self.ball = Ball(self)
        self.hearts = []
        self.status = "normal"

        for i in range(3):
            heart = Hearts(i)
            self.hearts.append(heart)

    def on_draw(self):
        arcade.start_render()

        if self.status == "normal":
            self.rocket.draw()
            score_txt = f"Score: {self.rocket.score}"
            arcade.draw_text(score_txt, 20, self.height -
                             25, arcade.color.WHITE, 15)
            self.ball.draw()
            for heart in self.hearts:
                heart.draw()

        elif self.status == "game over":
            arcade.draw_lrwh_rectangle_textured(
                0, 0, self.width, self.height, self.GM_background)

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

    def on_update(self, delta_time):
        self.rocket.move(self)
        self.ball.move()

        if self.ball.center_x < 10 or self.ball.center_x > self.width-10:
            self.ball.change_x *= -1

        if self.ball.center_y > self.height-10:
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.rocket, self.ball):
            self.ball.change_y *= -1

        for heart in self.hearts:
            if self.ball.center_y < 0:
                self.hearts.remove(heart)


if __name__ == "__main__":
    game = Game()
    arcade.run()
