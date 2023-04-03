import time
import arcade
from ball import Ball
from rocket import Rocket


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
        player1_score = f"Your score: {self.player_1.score}"
        arcade.draw_text(player1_score, 30, 30, arcade.color.WHITE, 12)
        player2_score = f"Computer score: {self.player_2.score}"
        arcade.draw_text(player2_score, self.width-170,
                         30, arcade.color.WHITE, 12)
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        if 45 < y < self.height - 45:
            self.player_1.center_y = y

    def on_update(self, delta_time):
        self.ball.move()
        self.player_2.move(self, self.ball)

        if self.ball.center_y < 45 or self.ball.center_y > self.height - 45:
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.ball, self.player_1) or \
                arcade.check_for_collision(self.ball, self.player_2):
            self.ball.change_x *= -1

        if self.ball.center_x < 0:
            self.player_2.score += 1
            del self.ball
            self.ball = Ball(self)
            time.sleep(1)

        if self.ball.center_x > self.width:
            self.player_1.score += 1
            del self.ball
            self.ball = Ball(self)
            time.sleep(1)


if __name__ == "__main__":
    game = Game()
    arcade.run()
