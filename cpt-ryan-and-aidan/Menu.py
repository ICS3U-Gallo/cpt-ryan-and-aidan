import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10


def main_menu():
    # Draw Main menu
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Legend Of Remake",
                     screen_width/2, 480, arcade.color.BLACK, 70,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-150,
                                       screen_height/2-25, 300, 75,
                                       arcade.color.BLACK, 5)
    arcade.draw_text("Play", screen_width/2,
                     screen_height/2+13, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-150,
                                       screen_height/2-125, 300,
                                       75, arcade.color.BLACK, 5)
    arcade.draw_text("How to Play", screen_width/2,
                     screen_height/2-87, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")


def help_menu():
    # Draw Help menu(Control)
    arcade.draw_text("How to play",
                     screen_width/2, 580, arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_text("Control", 300, 490, arcade.color.BLACK, 40)
    arcade.draw_text("W: Move Upward \nA: Move Left"
                     "\nS: Move Downward \nD: Move Right \n\n"
                     "J: Melee Attack \nK: Range Attack",
                     300, 450, arcade.color.BLACK, 30)
    arcade.draw_xywh_rectangle_outline(sprite_size, sprite_size,
                                       sprite_size, sprite_size,
                                       arcade.color.BLACK, 2)
    texture = arcade.load_texture("images/backarrow.png")
    arcade.draw_texture_rectangle(sprite_size*1.5, sprite_size*1.5,
                                  sprite_size,
                                  sprite_size, texture, 0)
    arcade.draw_xywh_rectangle_outline(screen_width-sprite_size*2, sprite_size,
                                       sprite_size, sprite_size,
                                       arcade.color.BLACK, 2)
    texture = arcade.load_texture("images/backarrow.png", mirrored=True)
    arcade.draw_texture_rectangle(screen_width-sprite_size*1.5,
                                  sprite_size*1.5,
                                  sprite_size, sprite_size, texture, 0)


def help_menu_2():
    arcade.draw_text("How to play", screen_width/2, 580,
                     arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_text("Gameplay", 300, 490, arcade.color.BLACK, 40)
    arcade.draw_text("Player statistic on top part of the screen \n"
                     "Kill Enemy to get coins \n"
                     "Walk over item to buy them at shop"
                     "\n\nDefeat the Boss to win",
                     300, 450, arcade.color.BLACK, 30)
    arcade.draw_xywh_rectangle_outline(sprite_size, sprite_size, sprite_size,
                                       sprite_size, arcade.color.BLACK, 2)
    texture = arcade.load_texture("images/backarrow.png")
    arcade.draw_texture_rectangle(sprite_size*1.5, sprite_size*1.5,
                                  sprite_size, sprite_size, texture, 0)


def death_menu():
    # Draw death menu
    arcade.draw_text("You died", screen_width/2, screen_height/2+100,
                     arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_text("Return to Menu", screen_width/2,
                     screen_height/2-12, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-175, screen_height/2-50,
                                       350, 75, arcade.color.BLACK, 5)
    arcade.draw_text("Revive", screen_width/2,
                     screen_height/2-112, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-175, screen_height/2-150,
                                       350, 75, arcade.color.BLACK, 5)

def win_screen():
    arcade.draw_text("You Win!", screen_width / 2, screen_height / 2 + 100,
                     arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width / 2 - 150,
                                       screen_height / 2 - 25, 300, 75,
                                       arcade.color.BLACK, 5)
    arcade.draw_text("Play again?", screen_width / 2,
                     screen_height / 2 + 13, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")

def pause_menu():
    # Draw pause manu
    arcade.draw_text("Paused", screen_width/2,
                     screen_height/2, arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")


def menu(page):
    # Determine which menu to draw
    if page == 0:
        main_menu()
    elif page == 2:
        help_menu()
    elif page == 3:
        help_menu_2()
    elif page == 4:
        pause_menu()


def menu_switch(page, x, y):
    # Changing menu
    if page == 0:
        if (x > screen_width/2-150 and x < screen_width/2+150 and
           y > screen_height/2-25 and y < screen_height/2+50):
            return 1
        elif (x > screen_width/2-150 and x < screen_width/2+150 and
              y > screen_height/2-125 and y < screen_height/2-50):
            return 2
    elif page == 2:
        if (x > sprite_size and x < sprite_size*2 and
           y > sprite_size and y < sprite_size*2):
            return 0
        elif (x > screen_width-sprite_size*2 and
              x < screen_width-sprite_size and
              y > sprite_size and y < sprite_size*2):
            return 3
    elif page == 3:
        if (x > sprite_size and x < sprite_size*2 and
           y > sprite_size and y < sprite_size*2):
            return 2

    return page


def pause_game(game):
    # Pausing the game
    if game.paused:
        game.paused = False
    elif not game.paused:
        game.paused = True
        game.menu_page = 4


def player_dead(game, x, y):
    # Changing menu for player death
    if (x > screen_width/2-175 and x < screen_width/2+175 and
       y > screen_height/2-50 and y < screen_height/2+25):
        game.game_start = False
        game.menu_page = 0
    elif (x > screen_width/2-175 and x < screen_width/2+175 and
          y > screen_height/2-150 and y < screen_height/2-75):
        game.player_sprite.dead = False
        game.player_sprite.health = 6
