import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self , w, h):
        super().__init__("my-project\session13\monster1.png")
        self.center_x=  w+50
        self.center_y=random.randint(0,h)
        self.width=60
        self.height=60
        self.speed=3
        self.bomb_sound = arcade.load_sound("my-project\session14\K1629287274_B3uO5.mp3")

    def move(self):
        self.center_x -= self.speed