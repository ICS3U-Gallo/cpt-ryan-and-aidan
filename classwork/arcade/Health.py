import arcade
import math

WIDTH = 640
HEIGHT = 480
player_health = 100
max_player_health = 350



def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    max_bar_width = 200
    bar_height = 50
    arcade.draw_xywh_rectangle_filled(WIDTH/2 - max_bar_width/2, HEIGHT/2 - bar_height/2, max_bar_width, bar_height, arcade.color.BLACK)

    health_width = player_health / max_player_health * max_bar_width
    arcade.draw_xywh_rectangle_filled(WIDTH/2 - max_bar_width/2, HEIGHT/2 - bar_height/2, health_width, bar_height, arcade.color.APPLE_GREEN)
    arcade.draw_text(f"{player_health}/{max_player_health} ({round(player_health/max_player_health*100,2)}%)", WIDTH/2 - max_bar_width/2, HEIGHT/2 + bar_height/2, arcade.color.BLACK)


    '''
    def placement(x, y, end, space):
        for tree in range(x, end):
            if x <= end:
                arcade.draw_xywh_rectangle_filled(x, y, 10, 30, arcade.color.GREEN)
            x += space

    placement(1, 450, 200, 15)
'''




def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()