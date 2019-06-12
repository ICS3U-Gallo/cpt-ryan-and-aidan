import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10


def main_menu():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Legend Of Remake", screen_width/2, 480, arcade.color.BLACK, 70,
                            align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-150, screen_height/2-25, 300, 75, arcade.color.BLACK, 5)
    arcade.draw_text("Play", screen_width/2, screen_height/2+13, arcade.color.BLACK, 30,
                            align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-150, screen_height/2-125, 300, 75, arcade.color.BLACK, 5)
    arcade.draw_text("How to Play", screen_width/2, screen_height/2-87, arcade.color.BLACK, 30,
                            align="center", anchor_x="center", anchor_y="center")

def help_menu():
    arcade.draw_text("How to play", screen_width/2, 580, arcade.color.BLACK, 50,
                            align="center", anchor_x="center", anchor_y="center")
    arcade.draw_text("Control", 300, 490, arcade.color.BLACK, 45)
    arcade.draw_text("W: Move Upward \nA: Move Left \nS: Move Downward \nD: Move Right \n\nJ: Melee Attack \nK: Range Attack",
                            300, 450, arcade.color.BLACK, 30)
    arcade.draw_xywh_rectangle_outline(sprite_size, sprite_size, sprite_size, sprite_size, arcade.color.BLACK, 2)
    texture = arcade.load_texture("images/backarrow.png")
    arcade.draw_texture_rectangle(sprite_size*1.5, sprite_size*1.5, sprite_size, sprite_size, texture, 0)

def death_menu():
    arcade.draw_text("You died", screen_width/2, screen_height/2+100, arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_text("Return to Menu", screen_width/2, screen_height/2-12 , arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-175, screen_height/2-50, 350, 75, arcade.color.BLACK, 5)
    arcade.draw_text("Revive", screen_width/2, screen_height/2-112, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-175, screen_height/2-150, 350, 75, arcade.color.BLACK, 5)

def menu(page):
    if page == 0:
        main_menu()
    elif page == 2:
        help_menu()


def menu_switch(page, x, y):
    if page == 0:
        if x > screen_width/2-150 and x < screen_width/2+150 and y > screen_height/2-25 and y < screen_height/2+50:
            return 1
        elif x > screen_width/2-150 and x < screen_width/2+150 and y > screen_height/2-125 and y < screen_height/2-50:
            return 2
    elif page == 2:
        if x > sprite_size and x < sprite_size*2 and y > sprite_size and y < sprite_size*2:
            return 0
    return page

def player_dead(game, x, y):
    if x > screen_width/2-175 and x < screen_width/2+175 and y > screen_height/2-50 and y < screen_height/2+25:
        game.game_start = False
        game.menu_page = 0
    elif x > screen_width/2-175 and x < screen_width/2+175 and y > screen_height/2-150 and y < screen_height/2-75:
        game.player_sprite.dead = False
        game.player_sprite.health = 6

