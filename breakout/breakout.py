import random
import time
import arcade
from rocket import Rocket
from ball import Ball
from house import House


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=400, height=500, title="Breakout")
        arcade.set_background_color(arcade.color.NAVY_BLUE)
        self.GM_background = arcade.load_texture(
            "episode16\photo_2023-03-23_21-50-37.jpg")
        self.rocket = Rocket(self.width, 40)
        self.ball = Ball(self)
        self.hearts = 3
        self.house = []
        self.house_list = arcade.SpriteList()
        self.status = "normal"
        self.level = 1
        self.laying_house_2()

    def laying_house_0(self):
        for row in range(0, 6, 2):
            for com in range(6):
                x = 60*com + 50
                y = 30*row + 250
                self.house.append(House(x, y))
                self.house_list.append(self.house[-1])

    def laying_house_1(self):
        for row in range(6):
            for com in range(0, 6, 2):
                x = 60*com + 80
                y = 30*row + 250
                self.house.append(House(x, y))
                self.house_list.append(self.house[-1])

    def laying_house_2(self):
        for row in range(6):
            for com in range(6):
                if (row + com) % 2:
                    x = 60*com + 50
                    y = 30*row + 250
                    self.house.append(House(x, y))
                    self.house_list.append(self.house[-1])

    def laying_house_3(self):
        for row in range(6):
            for com in range(6):
                x = 60*com + 50
                y = 30*row + 200
                self.house.append(House(x, y))
                self.house_list.append(self.house[-1])

    def on_draw(self):
        arcade.start_render()

        if self.status == "normal":
            self.rocket.draw()
            arcade.draw_text(f"Score: {self.rocket.score}", 20, self.height -
                             25, arcade.color.WHITE, 15)
            self.ball.draw()

            for heart in range(self.hearts):
                arcade.draw_rectangle_filled(
                    25*(heart+1), 20, 20, 8, arcade.color.WHITE_SMOKE)

            for house in self.house:
                arcade.draw_rectangle_filled(
                    house.center_x, house.center_y, house.width, house.height, house.color)

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

        house_collision_list = arcade.check_for_collision_with_list(
            self.ball, self.house_list)
        for house in house_collision_list:
            self.house_list.remove(house)
            self.house.remove(house)
            self.rocket.score += self.level

            if self.ball.center_y < house.center_y - house.height//2:
                self.ball.change_y = -1
            elif self.ball.center_y > house.center_y + house.height//2:
                self.ball.change_y = 1
            elif self.ball.center_x > house.center_x + house.width//2:
                self.ball.change_x = 1
            else:
                self.ball.change_x = -1

            if len(self.house) == 0:
                del self.ball
                self.ball = Ball(self)
                self.ball.speed += self.level-1
                plot_number = self.level % 4
                if plot_number == 0:
                    self.laying_house_3()
                elif plot_number == 1:
                    self.laying_house_0()
                elif plot_number == 2:
                    self.laying_house_1()
                elif plot_number == 3:
                    self.laying_house_2()

        if self.ball.center_y < 0:
            self.hearts -= 1
            del self.ball
            if self.hearts > 0:
                self.ball = Ball(self)
                self.ball.speed += self.level-1

            else:
                self.status = "game over"
                self.on_draw()
                time.sleep(1)
                exit(0)


if __name__ == "__main__":
    game = Game()
    arcade.run()
