from livewires import games, color
import NavigationButton as NB

games.init(screen_width = 832, screen_height = 624, fps = 50)

####################################
# IDs:
#   0 - PhantomMouse
#   1 - MyText
####################################

####################################
# States:
#   0 - Not entered application
#   1 - Choose left branch size (1 - 10)
#   2 - Choose right branch size (1 - 10)
#   3 - Choose edges (manually or randomly)
#   4 - If choosing edges manually, make choices on provided bipartite graph
#   5 - Choose operation:
#         - automatically find a maximum matching
#         - find a maximum matching manually
#         - watch procedure of algorithm to find a maximum matching
#         - watch procedure of algorithm to find a maximum matching with steps
####################################

# this class is used to check mouse hovers by having a very small sprite image
# follow the path of the mouse
class PhantomMouse(games.Sprite):
    def __init__(self, sprite_image):
        super(PhantomMouse, self).__init__(image = sprite_image)
        self.id = 0

    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y

# wrapper class for Text object (in turn a subclass of Sprites), to include id
class MyText(games.Text):
    def __init__(self, new_value, new_size, new_color, new_x, new_y):
        super(MyText, self).__init__(value = new_value, size = new_size,
                                     color = new_color, x = new_x, y = new_y)
        self.id = 1


# class to monitor changes in input; this class is loosely based on the 'Game'
# class of the final astrocrash game described on page 402 of 'Python
# Programming for the Absolute Beginner, Third Edition', by Michael Dawson,
# Chapter 12: Sound, Animation, and Program Development: The Astrocrash Game
class Responses(object):
    def __init__(self):
        self.state = 0
        self.main_text_sprite = None # Text sprite for main content
        self.button_list = [] # list of navigation buttons
        self.text_list = [] # list of text sprites appearing on buttons

    # remove all buttons from the screen
    def clear_buttons(self):
        for b in self.button_list:
            b.destroy() # remove the corresponding sprite from the screen
        self.button_list = []
        for t in self.text_list:
            t.destroy() # remove the corresponding text sprite from the screen
        self.text_list = []

    # change text
    def reset_text(self, new_text):
        if (self.main_text_sprite):
            self.main_text_sprite.set_value(new_text)
        else:
            self.main_text_sprite = MyText(new_text, 30, color.black, 600, 30)
            games.screen.add(self.main_text_sprite)

    # place all buttons (with their corresponding text) on screen, based on the
    # contents of self.button_list and self.text_list
    def render_buttons(self):
        for b in self.button_list:
            games.screen.add(b)
        for t in self.text_list:
            games.screen.add(t)

    # include initial application graphics
    def initialize_board(self):
        self.state = 1
        wall_image = games.load_image("images/wall-large.jpg")
        games.screen.background = wall_image
        self.set_left_branch_query()
        games.screen.mainloop()
        #wall_image = games.load_image("images/wall-large.jpg")
        #games.screen.background = wall_image
        #games.screen.mainloop()

    # to state 1
    def set_left_branch_query(self):
        self.state = 1
        self.reset_text('Left branch size:')
        #if (self.main_text_sprite):
        #    self.main_text_sprite.set_value('Left branch size:')
        #else:
        #    self.main_text_sprite = MyText('Left branch size:', 30, color.black,
        #                                   600, 30)
        #    games.screen.add(self.main_text_sprite)
        self.clear_buttons()
        button_image = games.load_image("images/button.png")
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    150, 3, 2))
        self.text_list.append(MyText('3', 20, color.black, 600, 150))
        self.render_buttons()

    # to state 2
    def set_right_branch_query(self):
        self.state = 2
        self.reset_text('Right branch size:')
        self.clear_buttons()
        button_image = games.load_image("images/button.png")
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    150, 4, 3))
        self.text_list.append(MyText('4', 20, color.black, 600, 150))
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    240, 4, 1))
        self.text_list.append(MyText('Go Back', 20, color.black, 600, 240))
        self.render_buttons()

    #def advance(self, old_state, new_state):
    def advance(self, new_state):
        if (new_state == 1):
            self.set_left_branch_query()
        elif (new_state == 2):
            self.set_right_branch_query()
        else:
            print('hi')
        #if ((old_state == 0) and (new_state == 1)):
        #    self.state = 1
        #    wall_image = games.load_image("images/wall-large.jpg")
        #    games.screen.background = wall_image
        #    self.set_left_branch_query()
        #    games.screen.mainloop()

def main():
    # set up sprite to follow mouse path, so as to register sprite overlaps
    phantom_mouse_image = games.load_image("images/phantom-pizza.bmp")
    pm = PhantomMouse(phantom_mouse_image)
    games.screen.add(pm)

    # object to control responses to buttons and navigation through options
    controller = Responses()
    #controller.advance(0, 1)
    controller.initialize_board()

main()
