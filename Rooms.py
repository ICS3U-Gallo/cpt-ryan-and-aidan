import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10
screen_title = "Temporary Title"

class Room:

    def __init__(self):
        self.wall_list = None
        self.background_list = None

        self.isshop = False

def startroom_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, screen_height - sprite_size):
        # Loop for each box going across
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 3 and x != sprite_size * 4 and x != sprite_size * 10 and x != sprite_size * 11) or y == 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, screen_width - sprite_size):
        # Loop for each box going across
        for y in range(sprite_size, screen_height - sprite_size, sprite_size):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != sprite_size * 4 and y != sprite_size * 5):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room


def outside1_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, screen_height - sprite_size):
        # Loop for each box going across
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 7 and x != sprite_size * 8) or y == 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, screen_width - sprite_size):
        # Loop for each box going across
        for y in range(sprite_size, screen_height - sprite_size, sprite_size):
            # Skip making a block 4 and 5 blocks up
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
    wall.left = 7 * sprite_size
    wall.bottom = 5 * sprite_size
    room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room


def startcave_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 3 and x != sprite_size * 4) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
    wall.left = 7 * sprite_size
    wall.bottom = 5 * sprite_size
    room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background.jpg")

    return room


def outside2_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 7 and x != sprite_size * 8) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room


def outside3_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (y == 0 and (x != sprite_size * 10 and x != sprite_size * 11)) or (y != 0 and (x != sprite_size * 5 and x != sprite_size * 6)):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def outside4_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (y == 0 and (x != sprite_size * 15 and x != sprite_size * 16)) or (y != 0 and (x != sprite_size * 5 and x != sprite_size * 6)):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def cave2shop_setup():
    room = Room()


    room.wall_list = arcade.SpriteList()




    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 5 and x != sprite_size * 6) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)


    room.background = arcade.load_texture("images/background.jpg")

    return room

def outside5_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if y == 0 or (x != sprite_size * 5 and x != sprite_size * 6 and x != sprite_size * 15 and x != sprite_size * 16):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def river1_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if y == 0 or (x != sprite_size * 2 and x != sprite_size * 3 and x != sprite_size * 5 and x != sprite_size * 6):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (sprite_size * 5, sprite_size * 6):
        for y in range(0, screen_height, sprite_size):
            river = arcade.Sprite("images/river.png", sprite_scale)
            river.left = x
            river.bottom = y
            room.wall_list.append(river)


    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def river2_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x == 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (y == 0 and (x != sprite_size * 2 and x != sprite_size * 3)) or (y != 0 and (x != sprite_size * 5 and x != sprite_size * 6)):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (sprite_size * 5, sprite_size * 6):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 5 and y != sprite_size * 6):
                river = arcade.Sprite("images/river.png", sprite_scale)
                river.left = x
                river.bottom = y
                room.wall_list.append(river)


    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def cave3shop_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 5 and x != sprite_size * 6) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)


    room.background = arcade.load_texture("images/background.jpg")

    return room


def cave4shop_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 5 and x != sprite_size * 6) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)


    room.background = arcade.load_texture("images/background.jpg")

    return room

def cave5boss_setup():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) and x == 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)


    room.background = arcade.load_texture("images/background.jpg")

    return room

def create():
    rooms_list = []
    room = startroom_setup()
    rooms_list.append(room)

    room = outside1_setup()
    rooms_list.append(room)

    room = startcave_setup()
    rooms_list.append(room)

    room = outside2_setup()
    rooms_list.append(room)

    room = outside3_setup()
    rooms_list.append(room)

    room = outside4_setup()
    rooms_list.append(room)

    room = cave2shop_setup()
    rooms_list.append(room)

    room = outside5_setup()
    rooms_list.append(room)

    room = river1_setup()
    rooms_list.append(room)

    room = river2_setup()
    rooms_list.append(room)

    room = cave3shop_setup()
    rooms_list.append(room)

    room = cave4shop_setup()
    rooms_list.append(room)

    room = cave5boss_setup()
    rooms_list.append(room)

    return rooms_list