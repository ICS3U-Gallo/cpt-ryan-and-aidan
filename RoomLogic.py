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

def shoplogic(player):

    if player.player_sprite.center_x in range(290, 310) and player.player_sprite.center_y in range(400, 420):
        player.player_sprite.coins -= 10
        player.player_sprite.health += 1

    elif player.player_sprite.center_x in range(572, 592) and player.player_sprite.center_y in range(400, 420):
        player.player_sprite.coins -= 20
        player.player_sprite.arrows += 2

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
        shoplogic()
        if player.player_sprite.center_y < 0:
            player.current_room = 4
            player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                               player.rooms[player.current_room].wall_list)
            player.player_sprite.center_y = screen_height
