import arcade
import math
import random

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10

bullet_speed = 5



class Range_Enemy(arcade.Sprite):
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

    def random_move(self):
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(-1, 2)

    def hit_walls(self, walls):
        if len(arcade.check_for_collision_with_list(self, walls)) > 0:
            self.change_x *= -1
            self.center_x += self.change_x
            self.change_y *= -1
            self.center_y += self.change_y
        if self.top >= screen_height or self.bottom <= 0:
            self.change_y *= -1
        if self.left <= 0 or self.right >= screen_width:
            self.change_x *= -1


class Melee_Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/enemy.png", scale=sprite_scale)
        self.change_x = 0
        self.change_y = 0
        self.hit_timer = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.hit_timer += 1

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

    def get_move(self):
        self.change_x = math.cos(self.ang)*3
        self.change_y = math.sin(self.ang)*3

    def hit_player(self,player):
        if arcade.check_for_collision(player, self) > 0:
            if self.hit_timer > 60:
                player.health -= 1
                self.hit_timer = 0

    def hit_walls(self, walls):
        print(walls)
        print(arcade.check_for_collision_with_list(self, walls))
        for wall in arcade.check_for_collision_with_list(self, walls):
            if self.right > wall.left:
                self.right = wall.left
            elif self.left < wall.right:
                self.left = wall.right
            if self.top < wall.bottom:
                self.top = wall.bottom
            elif self.bottom > wall.top:
                self.bottom = wall.top


class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    # Static variable that holds all the explosion textures
    explosion_textures = []

    def __init__(self, texture_list):
        super().__init__("images/explosion/explosion0000.png")

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()

def bullet_hit(bullet, game):
    hit_player = arcade.check_for_collision(game.player_sprite, bullet)
    hit_wall = arcade.check_for_collision_with_list(bullet, game.rooms[game.current_room].wall_list)
    if bullet.top < 0:
        bullet.kill()
    elif len(hit_wall) > 0:
        explosion = Explosion(game.explosion_texture_list)
        explosion.center_x = bullet.center_x
        explosion.center_y = bullet.center_y
        game.explosions_list.append(explosion)
        bullet.kill()
    elif hit_player:
        game.player_sprite.health -= 1
        explosion = Explosion(game.explosion_texture_list)
        explosion.center_x = bullet.center_x
        explosion.center_y = bullet.center_y
        game.explosions_list.append(explosion)
        bullet.kill()




def outside1_setup():
    enemy_list = arcade.SpriteList()

    enemy = Range_Enemy()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = Melee_Enemy()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def create():
    startroom = None
    outside1 = outside1_setup()
    startcave = []
    outside2 = []
    outside3 = []
    outside4 = []
    cave2shop = []

    enemy_list = [startroom, outside1, startcave, outside2, outside3, outside4, cave2shop]
    return enemy_list