import arcade
import os
import Rooms
import Enemy
import RoomLogic

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10
screen_title = "Temporary Title"

move_speed = 10

tex_right = 1
tex_left = 0

boomboom = 60



class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        texture = arcade.load_texture("images/character.png", mirrored=True, scale=sprite_scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/character.png", scale=sprite_scale)
        self.textures.append(texture)

        # By default, face right.
        self.face_dir = 1
        self.set_texture(tex_right)

        self.coins = 0
        self.health = 6
        self.dead = False

        self.weapon = arcade.SpriteList()
        self.hold_sword = False
        self.sword_hit_timer = 0

    def update(self):

        # Figure out if we should face left or right
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
        if self.hold_sword:
           self.sword_hit_timer += 1

    def get_bow(self):
        self.bow = arcade.Sprite("images/bow.png", scale=64/256)
        self.weapon.append(self.bow)
        self.bow.center_x = self.center_x
        self.bow.center_y = self.center_y

    def bow_fire(self, enemy_list, wall_list):
        self.arrow = arcade.Sprite("images/arrow.png", scale=sprite_scale)
        self.arrow_getdir()


    def get_sword(self):
        self.sword = arcade.Sprite("images/sword.png", scale=64 / 1000)
        self.weapon.append(self.sword)
        self.hold_sword = True


    def melee_attack(self, enemy_list, wall_list):
        if not self.hold_sword:
            self.get_sword()
        self.sword_pos()
        self.sword_hit(wall_list, enemy_list)


    def sword_pos(self):
        if self.face_dir == 3:
            self.sword.center_x = self.center_x - sprite_size
            self.sword.center_y = self.center_y
            self.sword.angle = 0
        elif self.face_dir == 2:
            self.sword.center_x = self.center_x
            self.sword.center_y = self.center_y - sprite_size
            self.sword.angle = 90
        elif self.face_dir == 1:
            self.sword.center_x = self.center_x + sprite_size
            self.sword.center_y = self.center_y
            self.sword.angle = 270
        elif self.face_dir == 0:
            self.sword.center_x = self.center_x
            self.sword.center_y = self.center_y + sprite_size
            self.sword.angle = 0

    def sword_hit(self, wall_list, enemy_list):
        if len(arcade.check_for_collision_with_list(self.sword, wall_list)) > 0:
            self.sword.kill()
        for enemy in arcade.check_for_collision_with_list(self.sword, enemy_list):
            enemy.kill()
            self.coins += Enemy.coins_drop()

    def stop_melee_attack(self):
        self.sword.kill()
        self.hold_sword = False
        self.sword_hit_timer = 0


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
            # Files from http://www.explosiongenerator.com are numbered sequentially.
            # This code loads all of the explosion0000.png to explosion0270.png files
            # that are part of this explosion.
            texture_name = f"images/explosion/explosion{i:04d}.png"

            self.explosion_texture_list.append(arcade.load_texture(texture_name))

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.itemone = False

        self.enemy_list = Enemy.create()

        # Our list of rooms
        self.rooms = Rooms.create()

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        health_x = 20
        health_y = screen_height - 50
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.player_sprite.dead:
            arcade.draw_text("You died", screen_width/2, screen_height/2, arcade.color.WHITE, 50,
                             align="center", anchor_x="center", anchor_y="center")
        else:

            # Draw the background texture
            arcade.draw_texture_rectangle(screen_width // 2, screen_height // 2,
                                          screen_width, screen_height, self.rooms[self.current_room].background)

            # Draw all the walls in this room
            self.rooms[self.current_room].wall_list.draw()

            # If you have coins or monsters, then copy and modify the line
            # above for each list.
            if self.current_room != 0 and self.current_room == 1:
                self.enemy_list[self.current_room].draw()
                self.bullet_list.draw()
                self.explosions_list.draw()
            if self.current_room == 6:
                RoomLogic.shopdraw()
            self.player_list.draw()
            self.player_sprite.weapon.draw()



            for i in range(self.player_sprite.health):
                arcade.draw_xywh_rectangle_filled(health_x, health_y, 20, 20, arcade.color.BLUE)
                health_x += 50
            texture = arcade.load_texture("images/coins.png")
            arcade.draw_texture_rectangle(screen_width-2.5*sprite_size, screen_height-sprite_size/2, sprite_size, sprite_size, texture, 0)
            arcade.draw_text(f"{self.player_sprite.coins}", screen_width-2*sprite_size, screen_height-57, arcade.color.BLACK, 50)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

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

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False
        if key == arcade.key.J:
            pass

    def update(self, delta_time):
        """ Movement and game logic """
        if self.player_sprite.dead:
            pass
        else:

            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = move_speed
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -move_speed
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -move_speed
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = move_speed
            if self.player_melee_attack and self.player_sprite.sword_hit_timer < 20:
                self.player_sprite.melee_attack(self.enemy_list[self.current_room], self.rooms[self.current_room].wall_list)
            elif self.player_sprite.sword_hit_timer == 20:
                self.player_sprite.stop_melee_attack()
                self.player_melee_attack = False
            if self.player_range_attack and not self.player_melee_attack:
                self.player_sprite.bow_fire(self.enemy_list[self.current_room], self.rooms[self.current_room].wall_list)

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.physics_engine.update()
            self.player_list.update()

            # Do some logic here to figure out what room we are in, and if we need to go
            # to a different room.
            RoomLogic.RoomLogic(self)


            for enemy in self.enemy_list[self.current_room]:
                enemy.get_ang(self.player_sprite.center_x, self.player_sprite.center_y)
                enemy.update()
                enemy.hit_player(self.player_sprite)
                if type(enemy) == Enemy.Range_Enemy:
                    enemy.hit_walls(self.rooms[self.current_room].wall_list)
                    if self.frame_count % 180 == 0:
                        self.bullet_list.append(enemy.fire())
                    if self.frame_count % 30 == 0:
                        enemy.random_move()
                elif type(enemy) == Enemy.Melee_Enemy:
                    enemy.hit_walls(self.rooms[self.current_room].wall_list)
                    enemy.get_move()

                # Get rid of the bullet when it flies off-screen
                for bullet in self.bullet_list:
                    Enemy.bullet_hit(bullet, self)


            self.bullet_list.update()
            self.explosions_list.update()

            if self.player_sprite.health == 0:
                self.player_sprite.kill()
                self.player_sprite.dead = True

            self.frame_count += 1





def main():
    """ Main method """
    window = MyGame(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()