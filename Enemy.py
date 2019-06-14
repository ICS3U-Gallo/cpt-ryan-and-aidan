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
        self.hit_timer = 0

    def update(self):
        # Move the enemy
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.hit_timer += 1

    def get_ang(self, player_x, player_y):
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

    def random_move(self):
        # Get random movement
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(-1, 2)

    def hit_player(self,player):
        # Check direct collision with player
        if arcade.check_for_collision(player, self) > 0:
            if self.hit_timer > 80 and not player.stuned:
                player.stuned = True
                player.orgin_x = player.center_x
                player.orgin_y= player.center_y
                player.health -= 1
                self.hit_timer = 0

    def hit_walls(self, walls):
        # Check collision with walls
        if len(arcade.check_for_collision_with_list(self, walls)) > 0:
            self.change_x *= -1
            self.center_x += self.change_x
            self.change_y *= -1
            self.center_y += self.change_y
        if self.top >= screen_height or self.bottom <= 0:
            self.change_y *= -1
        if self.left <= 0 or self.right >= screen_width:
            self.change_x *= -1

class Range_Enemy_cross(Range_Enemy):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/enemy.png", scale=sprite_scale)
        self.change_x = 0
        self.change_y = 0
        self.hit_timer = 0
        self.fire_rate = 210

    def fire(self, game):
        # Fire at 4 direction
        for angle in range(0, 360, 90):
            bullet = arcade.Sprite("images/laserBlue01.png", sprite_scale/math.sqrt(2))
            bullet.center_x = self.center_x
            bullet.center_y = self.center_y
            bullet.change_x = math.cos(math.radians(angle)) * bullet_speed
            bullet.change_y = math.sin(math.radians(angle)) * bullet_speed
            game.bullet_list.append(bullet)

class Range_Enemy_X(Range_Enemy):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/enemy.png", scale=sprite_scale)
        self.change_x = 0
        self.change_y = 0
        self.hit_timer = 0
        self.fire_rate = 210

    def fire(self, game):
        # Fire at 4 direction
        for angle in range(45, 360, 90):
            bullet = arcade.Sprite("images/laserBlue01.png", sprite_scale/math.sqrt(2))
            bullet.center_x = self.center_x
            bullet.center_y = self.center_y
            bullet.change_x = math.cos(math.radians(angle)) * bullet_speed
            bullet.change_y = math.sin(math.radians(angle)) * bullet_speed
            game.bullet_list.append(bullet)

class Range_Enemy_Aim(Range_Enemy):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/enemy.png", scale=sprite_scale)
        self.change_x = 0
        self.change_y = 0
        self.hit_timer = 0
        self.fire_rate = 150

    def fire(self, game):
        # Fire at player
        bullet = arcade.Sprite("images/laserBlue01.png", sprite_scale)
        bullet.center_x = self.center_x
        bullet.center_y = self.center_y
        bullet.angle = math.degrees(self.ang)
        bullet.change_x = math.cos(self.ang) * bullet_speed
        bullet.change_y = math.sin(self.ang) * bullet_speed
        game.bullet_list.append(bullet)

class Range_Enemy_Aim_2(Range_Enemy):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/enemy.png", scale=sprite_scale)
        self.change_x = 0
        self.change_y = 0
        self.hit_timer = 0
        self.fire_rate = 180

    def fire(self, game):
        # Fire 3 bullet aim at player
        for ang in range(int(math.degrees(self.ang))-30, int(math.degrees(self.ang))+31, 30):
            bullet = arcade.Sprite("images/laserBlue01.png", sprite_scale)
            bullet.center_x = self.center_x
            bullet.center_y = self.center_y
            bullet.angle = ang
            bullet.change_x = math.cos(math.radians(ang)) * bullet_speed
            bullet.change_y = math.sin(math.radians(ang)) * bullet_speed
            game.bullet_list.append(bullet)


class Melee_Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/enemy.png", scale=sprite_scale)
        self.change_x = 0
        self.change_y = 0
        self.hit_timer = 0
        self.angle = 0

    def update(self):
        # Move the enemy
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.hit_timer += 1

    def get_ang(self, player_x, player_y):
        # Get the destination location for the bullet
        dest_x = player_x
        dest_y = player_y
        x_diff = dest_x - self.center_x
        y_diff = dest_y - self.center_y
        self.ang = math.atan2(y_diff, x_diff)

    def get_move(self):
        # Get enemy movement so it move toward player
        self.change_x = math.cos(self.ang)*3
        self.change_y = math.sin(self.ang)*3

    def hit_player(self,player):
        # Check collision with player
        if arcade.check_for_collision(player, self) > 0:
            if self.hit_timer > 80 and not player.stuned:
                player.stuned = True
                player.orgin_x = player.center_x
                player.orgin_y= player.center_y
                player.health -= 1
                self.hit_timer = 0

    def hit_walls(self, walls):
        # Check collision with wall
        for wall in arcade.check_for_collision_with_list(self, walls):
            if self.right - wall.left < self.change_x:
                self.right -= self.change_x
            elif self.left - wall.right > self.change_x:
                self.left -= self.change_x
            if self.top - wall.bottom < self.change_y:
                self.top -= self.change_y
            elif self.bottom - wall.top > self.change_y:
                self.bottom -= self.change_y

class Boss(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/wormGreen.png")

        self.isinvis = False
        self.appear_timer = 0
        self.invis_timer = 0

        self.hp = 6
        self.washit = False

    def update(self, game):
        # Boss movement (Disappear, reappear)
        self.check_dead(game)
        if self.isinvis:
            if self.invis_timer == self.invis_time:
                self.appear()
            self.invis_timer += 1
        else:
            if self.appear_timer > 90:
                self.invis(game)
            self.appear_timer += 1

        if self.washit and not self.isinvis:
            self.center_x += random.randrange(-1, 2)*5
            self.center_y += random.randrange(-1, 2)*5



    def fire_pos(self, player):
        # Get bullet position to fire from random
        if random.randrange(2) == 0:
            x = random.randrange(1, 7)*sprite_size + sprite_size/2
        else:
            x = random.randrange(11, 17)*sprite_size + sprite_size/2
        if random.randrange(2) == 0:
            y = random.randrange(1, 3)*sprite_size + sprite_size/2
        else:
            y = random.randrange(7, 9)*sprite_size + sprite_size/2

        x_diff = player.center_x - x
        y_diff = player.center_y - y
        ang = math.atan2(y_diff, x_diff)
        ang_2 = round(math.degrees(ang)/45)*45

        return x, y, ang_2

    def fire(self, player):
        # Fire bullet at random
        start_x, start_y, angle = self.fire_pos(player)

        bullet = arcade.Sprite("images/fireball.png", sprite_scale/2)
        bullet.center_x = start_x
        bullet.center_y = start_y
        bullet.angle = angle+90
        bullet.change_x = math.cos(math.radians(angle)) * bullet_speed
        bullet.change_y = math.sin(math.radians(angle)) * bullet_speed

        return bullet

    def fire_alldir(self, game):
        # Fire bullet from boss to 8 direction
        for angle in range(0, 360, 45):
            bullet = arcade.Sprite("images/fireball.png", sprite_scale/math.sqrt(2))
            bullet.center_x = self.center_x
            bullet.center_y = self.center_y
            bullet.angle = angle + 90
            bullet.change_x = math.cos(math.radians(angle)) * bullet_speed
            bullet.change_y = math.sin(math.radians(angle)) * bullet_speed
            game.bullet_list.append(bullet)

    def invis(self, game):
        # Boss disappear from the screen
        self.fire_alldir(game)
        self.center_x = -1000
        self.center_y = -1000
        self.isinvis = True
        self.invis_timer = 0
        self.invis_time = random.randrange(5, 8)*60

    def appear(self):
        # Boss reappear from the screen
        self.center_x = random.randrange(7, 11)*sprite_size
        self.center_y = random.randrange(3, 7)*sprite_size
        self.isinvis = False
        self.appear_timer = 0
        self.washit = False

    def got_hit(self):
        # Boss got hit by player
        if not self.washit:
            self.washit = True
            self.hp -= 1
            self.appear_timer = 60

    def check_dead(self, game):
        # Kill the boss if hp reaches 0
        if self.hp <= 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    explosion = Explosion(game.explosion_texture_list)
                    explosion.texture = arcade.load_texture("images/explosion/explosion0000.png", scale=3)
                    explosion.center_x = self.center_x+i*32
                    explosion.center_y = self.center_y+j*32
                    game.explosions_list.append(explosion)
            self.kill()




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

def coins_drop():
    # Random coins drop from killing enemy
    chance = random.randrange(10)
    if chance == 0:
        return 5
    else:
        return 1

def bullet_hit(bullet, game):
    # Check bullet collision with wall and player
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
        if not game.player_sprite.stuned:
            game.player_sprite.health -= 1
            game.player_sprite.stuned = True
            game.player_sprite.orgin_x = game.player_sprite.center_x
            game.player_sprite.orgin_y = game.player_sprite.center_y
        explosion = Explosion(game.explosion_texture_list)
        explosion.center_x = bullet.center_x
        explosion.center_y = bullet.center_y
        game.explosions_list.append(explosion)
        bullet.kill()

def bullet_removal(game):
    # Remove bullet, explosion, and arrow if player move to a different room
    if game.player_sprite.center_y < 0 or game.player_sprite.center_y > screen_height or game.player_sprite.center_x < 0 or game.player_sprite.center_x > screen_width:
        for i in range(len(game.bullet_list)):
            game.bullet_list[0].kill()
        for i in range(len(game.explosions_list)):
            game.explosions_list[0].kill()
        for arrow in game.player_sprite.arrows_list:
            arrow.kill()

def random_enemy_type():
    enemy_type = random.randrange(5)
    if enemy_type == 0:
        enemy = Melee_Enemy()
    elif enemy_type == 1:
        enemy = Range_Enemy_cross()
    elif enemy_type == 2:
        enemy = Range_Enemy_Aim()
    elif enemy_type == 3:
        enemy = Range_Enemy_Aim_2()
    elif enemy_type == 4:
        enemy = Range_Enemy_X()
    return enemy

def outside1_setup():
    # Create enemy in room outside1
    enemy_list = arcade.SpriteList()

    enemy = Range_Enemy_X()
    enemy.center_x = 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = Range_Enemy_cross()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = Range_Enemy_cross()
    enemy.center_x = screen_width - 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = Range_Enemy_X()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def startcave_setup():
    enemy_list = arcade.SpriteList()

    enemy = Boss()
    enemy.center_x = screen_width/2
    enemy.center_y = screen_height/2
    enemy_list.append(enemy)

    return enemy_list

def outside2_setup():
    # Create Enemy in room outside2
    enemy_list = arcade.SpriteList()

    enemy = Range_Enemy_Aim()
    enemy.center_x = 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = Range_Enemy_Aim()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = Range_Enemy_Aim()
    enemy.center_x = screen_width - 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = Range_Enemy_Aim_2()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def outside3_setup():
    # Create Enemy in room outside3
    enemy_list = arcade.SpriteList()

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def outside4_setup():
    # Create Enemy in room outside3
    enemy_list = arcade.SpriteList()

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def outside5_setup():
    # Create Enemy in room outside3
    enemy_list = arcade.SpriteList()

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def river1_setup():
    # Create Enemy in room outside3
    enemy_list = arcade.SpriteList()

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def river2_setup():
    # Create Enemy in room outside3
    enemy_list = arcade.SpriteList()

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = 160
    enemy_list.append(enemy)

    enemy = random_enemy_type()
    enemy.center_x = screen_width - 160
    enemy.center_y = screen_height - 160
    enemy_list.append(enemy)

    return enemy_list

def create():
    # Create the enemy list
    startroom = arcade.SpriteList()
    outside1 = outside1_setup()
    startcave = startcave_setup()
    outside2 = outside2_setup()
    outside3 = outside3_setup()
    outside4 = outside4_setup()
    cave2shop = arcade.SpriteList()
    outside5 = outside5_setup()
    river1 = river1_setup()
    river2 = river2_setup()
    cave3shop = arcade.SpriteList()

    enemy_list = [startroom, outside1, startcave, outside2, outside3, outside4, cave2shop, outside5, river1, river2, cave3shop]
    return enemy_list
