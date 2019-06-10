import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10


def main_menu():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Legend Of Remake", screen_width/2, screen_height/2, arcade.color.BLACK, 50,
                             align="center", anchor_x="center", anchor_y="center")

def play():
    arcade.draw_text("Initalizing Game", screen_width/2, screen_height/2, arcade.color.BLACK, 50,
                             align="center", anchor_x="center", anchor_y="center")



def menu(page):
    if page == 0:
        main_menu()
    elif page == 1:
        play()

