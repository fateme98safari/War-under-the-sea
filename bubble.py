import arcade

class Bubble(arcade.Sprite):
    def __init__(self,host):
        super().__init__("my-project\session14\icons8-bubble-48.png")
        self.center_x= host.center_x + 30
        self.center_y=host.center_y
        self.change_x=1
        self.width=25
        self.height=25
        self.speed=3
        
  
    def move(self):
        self.center_x += self.speed