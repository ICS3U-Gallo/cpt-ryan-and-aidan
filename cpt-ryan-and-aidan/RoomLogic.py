import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10

move_speed = 10

tex_right = 1
tex_left = 0

health = 6

boomboom = 60


def start_pickup_draw(player):
    # Draws the sprites for the start items
    sword = arcade.Sprite("images/sword.png", 64/1000)
    bow = arcade.Sprite("images/bow.png", sprite_scale / 2)
    old_guy = arcade.Sprite("images/old man.jpg", sprite_scale / 2)

    sword.center_x = 500
    sword.center_y = 420
    bow.center_x = 600
    bow.center_y = 420
    old_guy.center_x = 550
    old_guy.center_y = 525

    if player.player_sprite.got_sword is False:
        sword.draw()
    if player.player_sprite.got_bow is False:
        bow.draw()
        arcade.draw_text("It's dangerous to go alone \nTake these",
                         280, 280, arcade.color.WHITE, 55)
    old_guy.draw()


def start_pickup_logic(player):
    # Does logic for the weapons
    if (player.player_sprite.center_x in range(480, 620) and
       player.player_sprite.center_y in range(410, 430)):
        player.player_sprite.got_sword = True
        player.player_sprite.got_bow = True


def shopdraw(player):
    # Draws the shop sprites
    heart_boost = arcade.Sprite("images/heart.png", sprite_scale)
    arrow_boost = arcade.Sprite("images/arrow.png", sprite_scale / 2)
    charity = arcade.Sprite("images/trashcan.png", sprite_scale)
    old_guy = arcade.Sprite("images/old man.jpg", sprite_scale / 2)

    heart_boost.center_x = 300
    heart_boost.center_y = 410
    arrow_boost.center_x = 580
    arrow_boost.center_y = 410
    charity.center_x = 870
    charity.center_y = 410
    old_guy.center_x = 550
    old_guy.center_y = 525

    if player.itemone is False:
        heart_boost.draw()
    if player.itemtwo is False:
        arrow_boost.draw()
    charity.draw()
    old_guy.draw()
    arcade.draw_text("10", 270, 310, arcade.color.WHITE, 55)
    arcade.draw_text("20", 540, 310, arcade.color.WHITE, 55)
    arcade.draw_text(" 1", 840, 310, arcade.color.WHITE, 55)
    arcade.draw_text("This is a shop", 320, 180,
                     arcade.color.WHITE, 55)


def shoplogic(player):
    # Does the logic for the shop
    if (player.player_sprite.center_x in range(269, 331) and
       player.player_sprite.center_y in range(389, 431)):
        while player.itemone is False:
            if (player.player_sprite.health < 6 and
               player.player_sprite.coins >= 10):
                player.player_sprite.coins -= 10
                player.player_sprite.health += 1
                player.itemone = True
            elif (player.player_sprite.health == 6 or
                  player.player_sprite.coins < 10):
                player.itemone = True

    elif (player.player_sprite.center_x in range(572, 592) and
          player.player_sprite.center_y in range(389, 431)):
        while player.itemtwo is False:
            if player.player_sprite.coins >= 20:
                player.player_sprite.coins -= 20
                player.player_sprite.arrows_count += 10
            player.itemtwo = True

    elif (player.player_sprite.center_x in range(842, 902) and
          player.player_sprite.center_y in range(389, 431)):
        while player.itemthree is False:
            player.player_sprite.coins -= 1
            player.itemthree = True


def RoomLogic(player):
    # Does logic for all rooms
    if player.current_room == 0:
        if player.player_sprite.center_x > screen_width:
            player.current_room = 1
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = 0
        elif (player.player_sprite.center_x in range(670, 740) and
              player.player_sprite.center_y > screen_height):
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
        elif player.player_sprite.center_y > screen_height:
            player.current_room = 2
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
        elif player.player_sprite.center_x < 0:
            player.current_room = 7
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = screen_width
    elif player.current_room == 1:
        if player.player_sprite.center_x < 0:
            player.current_room = 0
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = screen_width
        elif player.player_sprite.center_y > screen_height:
            player.current_room = 3
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
    elif player.current_room == 2:
        start_pickup_logic(player)
        if player.player_sprite.center_y < 0:
            player.current_room = 0
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
    elif player.current_room == 3:
        if player.player_sprite.center_y < 0:
            player.current_room = 1
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
        elif player.player_sprite.center_x < 0:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = screen_width
    elif player.current_room == 4:
        if player.player_sprite.center_y < 0:
            player.current_room = 0
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
        elif player.player_sprite.center_x > screen_width:
            player.current_room = 3
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = 0
        elif player.player_sprite.center_x < 0:
            player.current_room = 5
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = screen_width
        elif player.player_sprite.center_y > screen_height:
            player.current_room = 6
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
    elif player.current_room == 5:
        if player.player_sprite.center_x > screen_width:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = 0
        elif player.player_sprite.center_y < 0:
            player.current_room = 7
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
        elif player.player_sprite.center_x < 0:
            player.current_room = 9
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = screen_width
        elif player.player_sprite.center_y > screen_height:
            player.current_room = 11
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
    elif player.current_room == 6:
        shoplogic(player)
        if player.player_sprite.center_y < 0:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
            player.itemone = False
            player.itemtwo = False
            player.itemthree = False
    elif player.current_room == 7:
        if (player.player_sprite.center_x in range(350, 420) and
           player.player_sprite.center_y > screen_height):
            player.current_room = 10
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
        elif player.player_sprite.center_x < 0:
            player.current_room = 8
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = screen_width
        elif (player.player_sprite.center_x in range(990, 1058) and
              player.player_sprite.center_y > screen_height):
            player.current_room = 5
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
        elif player.player_sprite.center_x > screen_width:
            player.current_room = 0
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = 0
    elif player.current_room == 8:
        if player.player_sprite.center_y > screen_height:
            player.current_room = 9
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = 0
        elif player.player_sprite.center_x < 0:
            player.current_room = 12
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = screen_width
        elif player.player_sprite.center_x > screen_width:
            player.current_room = 7
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = 0
    elif player.current_room == 9:
        if player.player_sprite.center_y < 0:
            player.current_room = 8
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
        elif player.player_sprite.center_x > screen_width:
            player.current_room = 5
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_x = 0
    elif player.current_room == 10:
        shoplogic(player)
        if player.player_sprite.center_y < 0:
            player.current_room = 7
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
            player.itemone = False
            player.itemtwo = False
            player.itemthree = False
    elif player.current_room == 11:
        shoplogic(player)
        if player.player_sprite.center_y < 0:
            player.current_room = 5
            player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                               player_sprite,
                                                               player.
                                                               rooms
                                                               [player.
                                                                current_room].
                                                               wall_list)
            player.player_sprite.center_y = screen_height
            player.itemone = False
            player.itemtwo = False
            player.itemthree = False
    elif player.current_room == 12:
        if player.boss_defeated:
            if player.player_sprite.center_x > screen_width:
                player.current_room = 8
                player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                                   player_sprite,
                                                                   player.
                                                                   rooms
                                                                   [player.
                                                                    current_room].
                                                                   wall_list)
                player.player_sprite.center_x = 0
            elif player.player_sprite.center_x < 0:
                player.current_room = 13
                player.physics_engine = arcade.PhysicsEngineSimple(player.
                                                                   player_sprite,
                                                                   player.
                                                                   rooms
                                                                   [player.
                                                                    current_room].
                                                                   wall_list)
                player.player_sprite.center_x = screen_width
        else:
            if player.player_sprite.center_x > screen_width:
                player.player_sprite.center_x = screen_width
            if player.player_sprite.center_x < 0:
                player.player_sprite.center_x = 0
    elif player.current_room == 13:
        if player.player_sprite.center_x > screen_width:
            player.player_sprite.center_x = screen_width
        if player.player_sprite.center_x < 0:
            player.player_sprite.center_x = 0
        if player.player_sprite.center_y > screen_height:
            player.player_sprite.center_y = screen_height
        if player.player_sprite.center_y < 0:
            player.player_sprite.center_y = 0
