from livewires import games, color

# 640, 480
games.init(screen_width = 832, screen_height = 624, fps = 50)


class ClickableSprite(games.Sprite):
    def __init__(self, sprite_image, x, y, hovered_image, selected_image,
                 responder):
        super(ClickableSprite, self).__init__(image = sprite_image, x = x,
                                              y = y)
        self.plain_image = sprite_image
        self.hovered_image = hovered_image
        self.selected_image = selected_image
        self.is_selected = False
        # set when to initiate the counter
        self.set_counter = False
        # count number of steps since a change in vertex color
        self.step_count = 0
        self.responder = responder

    def update(self):
        is_chosen = False
        if (self.set_counter and (self.step_count == 19)):
            self.step_count = 0
            self.set_counter = False
        elif (self.set_counter):
            self.step_count += 1
        for item in self.overlapping_sprites:
            if (item.id == 1):
                is_chosen = True
                break

        if (is_chosen and (not self.is_selected) and
            (games.keyboard.is_pressed(games.K_SPACE)) and
            (not self.set_counter)):
            self.set_counter = True
            self.image = self.selected_image
            self.is_selected = True
        elif (is_chosen and self.is_selected and
              (games.keyboard.is_pressed(games.K_SPACE)) and
              (not self.set_counter)):
            self.set_counter = True
            self.image = self.plain_image
            self.is_selected = False
        elif (is_chosen and (not self.is_selected)):
            self.image = self.hovered_image
        elif (not self.is_selected):
            self.image = self.plain_image


class Vertex(ClickableSprite):
    def __init__(self, sprite_image, x_coor, y_coor, new_hovered_image,
                 new_selected_image, responder):
        super(Vertex, self).__init__(sprite_image, x_coor, y_coor,
                                     new_hovered_image, new_selected_image,
                                     responder)
        self.id = 0


# check mouse hovers by having an imageless sprite follow the mouse
class PhantomMouse(games.Sprite):
    def __init__(self, sprite_image):
        super(PhantomMouse, self).__init__(image = sprite_image)
        self.id = 1
        
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y


# extend Text object to include an id
class MyText(games.Text):
    def __init__(self, new_value, new_size, new_color, new_x, new_y):
        super(MyText, self).__init__(value = new_value, size = new_size,
                                     color = new_color, x = new_x, y = new_y)
        self.id = 2


# create a class for buttons
class MyButton(ClickableSprite):
    def __init__(self, new_image, new_x, new_y, new_hovered_image,
                 new_selected_image, responder, new_text = ''):
        super(MyButton, self).__init__(new_image, new_x, new_y,
                                       new_hovered_image, new_selected_image,
                                       responder)
        self.id = 3
        self.text = new_text


# class to monitor changes in input; this class is loosely based on the 'Game'
# class of the final astrocrash game described on page 402 of 'Python
# Programming for the Absolute Beginner, Third Edition', by Michael Dawson,
# Chapter 12: Sound, Animation, and Program Development: The Astrocrash Game
class Responses(object):
    def __init__(self):
        self.state = 0
        self.left_size = 0
        self.right_size = 0
        self.left_branch = [] # list of vertices of left branch
        self.right_branch = [] # list of vertices of right branch
        self.button_list = [] # list of buttons as ClickableSprites
        self.main_text_sprite = None # Text sprite for main content
        self.text_list = [] # list of text sprites appearing on buttons

    def set_left_branch_query(self):
        self.main_text_sprite = MyText('Left branch size:', 30, color.black,
                                       600, 30)
        games.screen.add(self.main_text_sprite)
        button_image = games.load_image("button.png")
        hovered_button_image = games.load_image("hovered-button.png")
        selected_button_image = games.load_image("selected-button.png")

        for i in range(5):
            self.button_list.append(MyButton(button_image, 550, 90 + 55 * i,
                                             hovered_button_image,
                                             selected_button_image, self,
                                             str(i+1)))
            self.text_list.append(MyText(str(i+1), 20, color.black, 550,
                                         90 + 55 * i))
        for i in range(5):
            self.button_list.append(MyButton(button_image, 700, 90 + 55 * i,
                                             hovered_button_image,
                                             selected_button_image, str(i+6),
                                             self))
            self.text_list.append(MyText(str(i+6), 20, color.black, 700,
                                         90 + 55 * i))
        for b in self.button_list:
            games.screen.add(b)
        for t in self.text_list:
            games.screen.add(t)
        #vertex = games.load_image("vertex.png")
        #hovered_vertex = games.load_image("hovered-vertex.png")
        #selected_vertex = games.load_image("selected-vertex.png")
        #for i in range(10):
        #    for j in range(2):
        #        self.button_list.append(Vertex(vertex, 100 + 340 * j,
        #                                       70 * i + 30, hovered_vertex,
        #                                       selected_vertex))

    def advance(self):
        self.state += 1
        if (self.state == 1):
            self.set_left_branch_query()

    def play(self):
        wall_image = games.load_image("wall-large.jpg")
        games.screen.background = wall_image
        self.advance()
        games.screen.mainloop()


def main():
    phantom_mouse_image = games.load_image("phantom-pizza.bmp")
    pm = PhantomMouse(phantom_mouse_image)
    games.screen.add(pm)

    # class object to control responses to buttons
    controller = Responses()
    controller.play()

main()
