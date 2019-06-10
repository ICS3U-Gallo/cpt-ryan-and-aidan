import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10


def main_menu():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Legend Of Remake", screen_width/2, 480, arcade.color.BLACK, 50,
                            align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-150, screen_height/2-25, 300, 75, arcade.color.BLACK, 5)
    arcade.draw_text("Play", screen_width/2, screen_height/2+13, arcade.color.BLACK, 30,
                            align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(screen_width/2-150, screen_height/2-125, 300, 75, arcade.color.BLACK, 5)
    arcade.draw_text("How to Play", screen_width/2, screen_height/2-87, arcade.color.BLACK, 30,
                            align="center", anchor_x="center", anchor_y="center")


def menu(page):
    if page == 0:
        main_menu()


def menu_switch(page, x, y):
    if x > screen_width/2-150 and x < screen_width/2+150 and y > screen_height/2-25 and y < screen_height/2+50:
        return 1
    else:
        return page
