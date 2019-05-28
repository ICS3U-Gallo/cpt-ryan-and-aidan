import arcade
import math
import random

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10

bullet_speed = 5



class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/enemy.png", scale=sprite_scale)
        self.change_x = 0
        self.change_y = 0


    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def get_ang(self, player_x, player_y):
        # Get the destination location for the bullet
        dest_x = player_x
        dest_y = player_y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - self.center_x
        y_diff = dest_y - self.center_y
        self.ang = math.atan2(y_diff, x_diff)

        # Set the enemy to face the player.
        self.angle = math.degrees(self.ang) - 90

    def fire(self):
        bullet = arcade.Sprite("images/laserBlue01.png", sprite_scale)
        bullet.center_x = self.center_x
        bullet.center_y = self.center_y

        # Angle the bullet sprite
        bullet.angle = math.degrees(self.ang)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        bullet.change_x = math.cos(self.ang) * bullet_speed
        bullet.change_y = math.sin(self.ang) * bullet_speed

        return bullet

    def get_move(self):
        self.change_x = random.randrange(-1,2)
        self.change_y = random.randrange(-1,2)




def room2_setup():
    enemy_list = arcade.SpriteList()

    enemy = Enemy()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy.angle = 180
    enemy_list.append(enemy)

    enemy = Enemy()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy.angle = 180
    enemy_list.append(enemy)

    return enemy_list

def create():
    room2 = room2_setup()
    room3 = []
    room4 = []
    room5 = []

    enemy_list = [None, room2, room3, room4, room5]
    return enemy_list