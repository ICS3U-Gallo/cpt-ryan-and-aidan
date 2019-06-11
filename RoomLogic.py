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



def shopdraw(player):

    heart_boost = arcade.Sprite("images/heart.png", sprite_scale)
    arrow_boost = arcade.Sprite("images/arrow.png", sprite_scale / 2)
    charity = arcade.Sprite("images/trashcan.png", sprite_scale)

    heart_boost.center_x = 300
    heart_boost.center_y = 410
    arrow_boost.center_x = 580
    arrow_boost.center_y = 410
    charity.center_x = 870
    charity.center_y = 410

    if player.itemone is False:
        heart_boost.draw()
    if player.itemtwo is False:
        arrow_boost.draw()
    charity.draw()


def shoplogic(player):

    if player.player_sprite.center_x in range(269, 331) and player.player_sprite.center_y in range(389, 431):
        while player.itemone is False:
            if player.player_sprite.health < 6 and player.player_sprite.coins >= 10:
                player.player_sprite.coins -= 10
                player.player_sprite.health += 1
                player.itemone = True
            elif player.player_sprite.health == 6 or player.player_sprite.coins < 10:
                player.itemone = True


    elif player.player_sprite.center_x in range(572, 592) and player.player_sprite.center_y in range(389, 431):
        while player.itemtwo is False:
            if player.player_sprite.coins >= 20:
                player.player_sprite.coins -= 20
                player.player_sprite.arrows_count += 10
            player.itemtwo = True

    elif player.player_sprite.center_x in range(842, 902) and player.player_sprite.center_y in range(389, 431):
        while player.itemthree is False:
            player.player_sprite.coins -= 1
            player.itemthree = True

def RoomLogic(player):
    if player.current_room == 0:
        if player.player_sprite.center_x > screen_width:
            player.current_room = 1
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_x = 0
        elif player.player_sprite.center_x in range(670, 740) and player.player_sprite.center_y > screen_height:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = 0
        elif player.player_sprite.center_y > screen_height:
            player.current_room = 2
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = 0
    elif player.current_room == 1:
        if player.player_sprite.center_x < 0:
            player.current_room = 0
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_x = screen_width
        elif player.player_sprite.center_y > screen_height:
            player.current_room = 3
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = 0
    elif player.current_room == 2:
        if player.player_sprite.center_y < 0:
            player.current_room = 0
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = screen_height
    elif player.current_room == 3:
        if player.player_sprite.center_y < 0:
            player.current_room = 1
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = screen_height
        elif player.player_sprite.center_x < 0:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_x = screen_width
    elif player.current_room == 4:
        if player.player_sprite.center_y < 0:
            player.current_room = 0
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = screen_height
        elif player.player_sprite.center_x > screen_width:
            player.current_room = 3
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_x = 0
        elif player.player_sprite.center_x < 0:
            player.current_room = 5
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_x = screen_width
        elif player.player_sprite.center_y > screen_height:
            player.current_room = 6
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                               player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = 0
    elif player.current_room == 5:
        if player.player_sprite.center_x > screen_width:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                             player.rooms[player.current_room].wall_list)
            player.player_sprite.center_x = 0
    elif player.current_room == 6:
        shoplogic(player)
        if player.player_sprite.center_y < 0:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                               player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = screen_height
            player.itemone = False
            player.itemtwo = False
            player.itemthree = False


