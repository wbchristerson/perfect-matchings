from livewires import games, color

games.init(screen_width = 832, screen_height = 624, fps = 50)

####################################
# IDs:
#   0 - PhantomMouse
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
        if (self.main_text_sprite):
            self.main_text_sprite.set_value('Left branch size:')
        else:
            self.main_text_sprite = games.Text(value = 'Left branch size:',
                                               size = 30, color = color.black,
                                               x = 600, y = 30)
            games.screen.add(self.main_text_sprite)

    #def advance(self, old_state, new_state):
    def advance(self, new_state):
        print('hello')
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
