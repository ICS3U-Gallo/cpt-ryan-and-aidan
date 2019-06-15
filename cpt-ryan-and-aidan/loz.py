import arcade
import os
import Rooms
import Enemy
import RoomLogic
import Menu
import random

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10
screen_title = "Comp Sci CPT - Legend of Remaked"

move_speed = 10
arrow_speed = 15

tex_right = 1
tex_left = 0

boomboom = 60

shop_list = [6, 10, 11]


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        texture = arcade.load_texture("images/character.png",
                                      mirrored=True, scale=sprite_scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/character.png", scale=sprite_scale)
        self.textures.append(texture)

        # By default, face right.
        self.face_dir = 1
        # 0 = up, 1 = right, 2 = down, 3 = left
        self.set_texture(tex_right)

        # Set up Player stats
        self.coins = 999
        self.health = 6
        self.arrows_count = 999
        self.dead = False

        self.stuned = False
        self.stun_counter = 0

        self.got_sword = False
        self.got_bow = False
        self.weapon = arcade.SpriteList()
        self.arrows_list = arcade.SpriteList()

        self.hold_sword = False
        self.hold_bow = False
        self.sword_hit_timer = 0
        self.bow_canfire = True

    def update(self):

        # Figure out player facing direction
        if self.change_y < 0:
            self.face_dir = 2
        if self.change_y > 0:
            self.face_dir = 0
        if self.change_x < 0:
            self.face_dir = 3
            self.set_texture(tex_left)
        if self.change_x > 0:
            self.face_dir = 1
            self.set_texture(tex_right)

        # Update sword/bow
        if self.hold_sword:
            self.sword_hit_timer += 1
        elif self.hold_bow:
            self.bow_pos()

    def get_bow(self):
        # Create the bow
        self.bow = arcade.Sprite("images/bow.png", 64/256)
        self.weapon.append(self.bow)
        self.hold_bow = True
        self.bow_pos()

    def bow_pos(self):
        # Update bow position and angle base on player
        self.bow.center_x = self.center_x
        self.bow.center_y = self.center_y
        if self.face_dir == 3:
            self.bow.center_x = self.center_x - sprite_size / 2
            self.bow.angle = 45
        elif self.face_dir == 2:
            self.bow.center_y = self.center_y - sprite_size / 2
            self.bow.angle = 135
        elif self.face_dir == 1:
            self.bow.center_x = self.center_x + sprite_size / 2
            self.bow.angle = 225
        elif self.face_dir == 0:
            self.bow.center_y = self.center_y + sprite_size / 2
            self.bow.angle = 315

    def bow_fire(self):
        # Fire an arrow
        if not self.hold_bow:
            self.get_bow()
        if len(self.arrows_list) < 1 and self.arrows_count > 0:
            self.arrow = arcade.Sprite("images/arrow.png", 32/300)
            self.arrows_list.append(self.arrow)
            self.arrow_getdir()
            self.arrows_count -= 1

    def arrow_getdir(self):
        # Get arrow direction and speed
        self.arrow.center_x = self.bow.center_x
        self.arrow.center_y = self.bow.center_y
        if self.face_dir == 3:
            self.arrow.change_x = -arrow_speed
            self.arrow.angle = 135
        elif self.face_dir == 2:
            self.arrow.change_y = -arrow_speed
            self.arrow.angle = 225
        elif self.face_dir == 1:
            self.arrow.change_x = arrow_speed
            self.arrow.angle = 315
        elif self.face_dir == 0:
            self.arrow.change_y = arrow_speed
            self.arrow.angle = 45

    def arrow_hit(self, enemy_list, wall_list):
        # Check collision between arrow and objects
        hit_wall = arcade.check_for_collision_with_list(self.arrow, wall_list)
        hit_enemy = arcade.check_for_collision_with_list(self.arrow,
                                                         enemy_list)
        for enemy in hit_enemy:
            if type(enemy) != Enemy.Boss:
                enemy.kill()
                self.coins += Enemy.coins_drop()
            else:
                enemy.got_hit()
            self.arrows_list.remove(self.arrow)
            self.arrow.kill()
        if len(hit_wall) > 0:
            self.arrows_list.remove(self.arrow)
            self.arrow.kill()
        if (self.arrow.bottom > screen_height or self.arrow.top <
           0 or self.arrow.right < 0 or self.arrow.left > screen_width):
            self.arrows_list.remove(self.arrow)
            self.arrow.kill()

    def stop_hold_bow(self):
        # Remove the bow
        self.bow.kill()
        self.hold_bow = False

    def get_sword(self):
        # Create the sword
        if self.hold_bow:
            self.stop_hold_bow()
        self.sword = arcade.Sprite("images/sword.png", 64 / 1000)
        self.weapon.append(self.sword)
        self.hold_sword = True

    def melee_attack(self, enemy_list, wall_list):
        # Logic for melee attack
        if not self.hold_sword:
            self.get_sword()
        self.sword_pos()
        self.sword_hit(wall_list, enemy_list)

    def sword_pos(self):
        # Update sword position base on player
        self.sword.center_x = self.center_x
        self.sword.center_y = self.center_y
        if self.face_dir == 3:
            self.sword.center_x = self.center_x - sprite_size
            self.sword.angle = 0
        elif self.face_dir == 2:
            self.sword.center_y = self.center_y - sprite_size
            self.sword.angle = 90
        elif self.face_dir == 1:
            self.sword.center_x = self.center_x + sprite_size
            self.sword.angle = 270
        elif self.face_dir == 0:
            self.sword.center_y = self.center_y + sprite_size
            self.sword.angle = 0

    def sword_hit(self, wall_list, enemy_list):
        # Check sword collision with wall and enemy
        if len(arcade.check_for_collision_with_list(self.sword,
                                                    wall_list)) > 0:
            self.sword.kill()
        for enemy in arcade.check_for_collision_with_list(self.sword,
                                                          enemy_list):
            if type(enemy) != Enemy.Boss:
                enemy.kill()
                self.coins += Enemy.coins_drop()
            else:
                enemy.got_hit()

    def stop_melee_attack(self):
        # Remove the sword
        self.sword.kill()
        self.hold_sword = False
        self.sword_hit_timer = 0

    def stun(self):
        # Player get stunned
        if self.stun_counter <= 10:
            if self.hold_sword:
                self.stop_melee_attack()
            if self.hold_bow:
                self.stop_hold_bow()
            self.center_x += random.randrange(-1, 2)*5
            self.center_y += random.randrange(-1, 2)*5
            self.stun_counter += 1
        else:
            self.stuned = False
            self.center_x = self.orgin_x
            self.center_y = self.orgin_y
            self.stun_counter = 0


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.game_start = False
        self.paused = False
        self.menu_page = 0

        self.frame_count = 0

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.enemy_list = None
        self.enemy_physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.player_melee_attack = False
        self.player_range_attack = False

        # Pre-load the animation frames. We don't do this in the __init__
        # of the explosion sprite because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []

        for i in range(boomboom):
            # Files from http://www.explosiongenerator.com
            # are numbered sequentially.
            # This code loads all of the explosion0000.png to
            # explosion0270.png files
            # that are part of this explosion.
            texture_name = f"images/explosion/explosion{i:04d}.png"

            self.explosion_texture_list.append(arcade.load_texture
                                               (texture_name))

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        if self.game_start:
            self.player_sprite = Player()
            self.player_sprite.center_x = 100
            self.player_sprite.center_y = 100
            self.player_list = arcade.SpriteList()
            self.player_list.append(self.player_sprite)
            self.bullet_list = arcade.SpriteList()
            self.explosions_list = arcade.SpriteList()
            self.itemone = False
            self.itemtwo = False
            self.itemthree = False

            # List of Enemy
            self.enemy_list = Enemy.create()

            # Our list of rooms
            self.rooms = Rooms.create()

            # Our starting room number
            self.current_room = 0

            # Create a physics engine for this room
            self.physics_engine = arcade.PhysicsEngineSimple(
                self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        health_x = 20
        health_y = screen_height - 50
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.game_start and not self.paused:
            if self.player_sprite.dead:
                Menu.death_menu()
            else:

                # Draw the background texture
                arcade.draw_texture_rectangle(screen_width // 2,
                                              screen_height // 2,
                                              screen_width, screen_height,
                                              self.rooms[self.current_room].
                                              background)

                # Draw all the walls in this room
                self.rooms[self.current_room].wall_list.draw()

                # Draw enemies, bullets, explosions, and player
                self.enemy_list[self.current_room].draw()
                self.bullet_list.draw()
                self.explosions_list.draw()
                self.player_list.draw()

                # Draw the shop
                if self.current_room in shop_list:
                    RoomLogic.shopdraw(self)
                elif self.current_room == 2:
                    RoomLogic.start_pickup_draw(self)
                self.player_sprite.weapon.draw()
                self.player_sprite.arrows_list.draw()

                # Draw Player health and coins/arrows count
                for i in range(self.player_sprite.health):
                    arcade.draw_xywh_rectangle_filled(health_x, health_y, 20,
                                                      20, arcade.color.BLUE)
                    health_x += 50
                texture = arcade.load_texture("images/coins.png")
                arcade.draw_texture_rectangle(screen_width-2.5*sprite_size,
                                              screen_height-sprite_size/2,
                                              sprite_size, sprite_size,
                                              texture, 0)
                arcade.draw_text(f"{self.player_sprite.coins}",
                                 screen_width-2*sprite_size, screen_height-57,
                                 arcade.color.BLACK, 50)
                texture = arcade.load_texture("images/arrow.png")
                arcade.draw_texture_rectangle(screen_width-5.5*sprite_size,
                                              screen_height-sprite_size/2,
                                              sprite_size,
                                              sprite_size, texture, 0)
                arcade.draw_text(f"{self.player_sprite.arrows_count}",
                                 screen_width-5*sprite_size,
                                 screen_height-57, arcade.color.BLACK, 50)
        else:
            Menu.menu(self.menu_page)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.game_start:
            if key == arcade.key.ESCAPE:
                Menu.pause_game(self)
            if not self.paused:
                if key == arcade.key.W:
                    self.up_pressed = True
                elif key == arcade.key.S:
                    self.down_pressed = True
                elif key == arcade.key.A:
                    self.left_pressed = True
                elif key == arcade.key.D:
                    self.right_pressed = True
                if key == arcade.key.J:
                    self.player_melee_attack = True
                elif key == arcade.key.K:
                    self.player_range_attack = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if self.game_start and not self.paused:
            if key == arcade.key.W:
                self.up_pressed = False
            elif key == arcade.key.S:
                self.down_pressed = False
            elif key == arcade.key.A:
                self.left_pressed = False
            elif key == arcade.key.D:
                self.right_pressed = False
            if key == arcade.key.K:
                self.player_range_attack = False
                self.player_sprite.bow_canfire = True

    def update(self, delta_time):
        """ Movement and game logic """
        if self.game_start and not self.paused:
            if not self.player_sprite.dead:
                # Player Control(Movement and attack)
                self.player_sprite.change_x = 0
                self.player_sprite.change_y = 0
                if not self.player_sprite.stuned:
                    if self.up_pressed and not self.down_pressed:
                        self.player_sprite.change_y = move_speed
                    elif self.down_pressed and not self.up_pressed:
                        self.player_sprite.change_y = -move_speed
                    if self.left_pressed and not self.right_pressed:
                        self.player_sprite.change_x = -move_speed
                    elif self.right_pressed and not self.left_pressed:
                        self.player_sprite.change_x = move_speed
                    if (self.player_melee_attack and self.player_sprite.
                       sword_hit_timer <
                       20 and self.player_sprite.got_sword):
                        self.player_sprite.melee_attack(self.enemy_list[
                            self.current_room],
                            self.rooms[self.current_room].wall_list)
                    elif self.player_sprite.sword_hit_timer == 20:
                        self.player_sprite.stop_melee_attack()
                        self.player_melee_attack = False
                    if (self.player_range_attack and not
                       self.player_sprite.hold_sword and
                       self.player_sprite.bow_canfire and
                       self.player_sprite.got_bow):
                        self.player_sprite.bow_fire()
                        self.player_sprite.bow_canfire = False
                else:
                    # Get stunned if player gets hit
                    self.player_sprite.stun()
                if len(self.player_sprite.arrows_list) > 0:
                    self.player_sprite.arrow_hit(self.enemy_list[self.
                                                 current_room],
                                                 self.rooms[self.
                                                 current_room].wall_list)

                # Call update on player
                self.physics_engine.update()
                self.player_list.update()

                # Do some logic here to figure out what room we are in
                # and if we need to go to a different room.
                Enemy.bullet_removal(self)
                RoomLogic.RoomLogic(self)

                # Update the enemy(move, fire, collision)
                for enemy in self.enemy_list[self.current_room]:
                    if type(enemy) == Enemy.Boss:
                        enemy.update(self)
                        if self.frame_count % (enemy.hp*10+20) == 0:
                            self.bullet_list.append(enemy.fire(
                                self.player_sprite))
                    else:
                        enemy.get_ang(self.player_sprite.center_x,
                                      self.player_sprite.center_y)
                        enemy.update()
                        enemy.hit_player(self.player_sprite)
                        enemy.hit_walls(self.rooms[
                                                  self.current_room].wall_list)
                        if isinstance(enemy, Enemy.Range_Enemy):
                            if self.frame_count % enemy.fire_rate == 0:
                                enemy.fire(self)
                            if self.frame_count % 30 == 0:
                                enemy.random_move()
                        elif type(enemy) == Enemy.Melee_Enemy:
                            enemy.get_move()

                # Check bullet collision with object
                for bullet in self.bullet_list:
                    Enemy.bullet_hit(bullet, self)

                # Update the projectile
                self.bullet_list.update()
                self.explosions_list.update()
                self.player_sprite.arrows_list.update()

                # player death
                if self.player_sprite.health == 0:
                    self.player_sprite.dead = True

                self.frame_count += 1
        else:
            # if they click play game, start the game
            if self.menu_page == 1:
                self.game_start = True
                self.setup()

    def on_mouse_press(self, x, y, button, modifiers):
        # Mouse input to control menu
        if not self.game_start or self.paused:
            self.menu_page = Menu.menu_switch(self.menu_page, x, y)
        else:
            if self.player_sprite.dead:
                Menu.player_dead(self, x, y)


def main():
    """ Main method """
    window = MyGame(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
