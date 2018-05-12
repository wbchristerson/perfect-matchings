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
#   5 - Choose operation after choosing edges manually:
#         - automatically find a maximum matching
#         - find a maximum matching manually
#         - watch procedure of algorithm to find a maximum matching
#         - watch procedure of algorithm to find a maximum matching with steps
#   6 - Choose operation after choosing edges randomly:
#         - automatically find a maximum matching
#         - find a maximum matching manually
#         - watch procedure of algorithm to find a maximum matching
#         - watch procedure of algorithm to find a maximum matching with steps
#   7 - Execute graph operation (edges chosen manually)
#   8 - Execute graph operation (edges chosen randomly)
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

    # to state 3
    def set_edge_choice_query(self):
        self.state = 3
        self.reset_text('How do you want to choose edges?')
        self.clear_buttons()
        button_image = games.load_image("images/button.png")
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    150, 5, 4))
        self.text_list.append(MyText('Manually', 20, color.black, 600, 150))
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    240, 6, 6))
        self.text_list.append(MyText('Randomly', 20, color.black, 600, 240))
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    330, 4, 2))
        self.text_list.append(MyText('Go Back', 20, color.black, 600, 330))
        self.render_buttons()

    # to state 4
    def set_manual_edge_choice_query(self):
        self.state = 4
        self.reset_text('Make your edge choices on the graph.')
        self.clear_buttons()
        button_image = games.load_image("images/button.png")
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    150, 7, 5))
        self.text_list.append(MyText('Done', 20, color.black, 600, 150))
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    240, 8, 3))
        self.text_list.append(MyText('Go Back', 20, color.black, 600, 240))
        self.render_buttons()

    # to state 5
    def manual_operations_query(self):
        self.state = 5
        self.reset_text('Choose Procedure For')
        self.clear_buttons()
        # add additional line of prompt text
        self.text_list.append(MyText('Maximal Matching (MM).', 30, color.black,
                                     600, 60))
        button_image = games.load_image("images/button.png")
        long_button_image = games.load_image("images/long_button.png")
        self.button_list.append(NB.NavigationButton(self, long_button_image,
                                                    600, 150, 1, 7))
        self.text_list.append(MyText('Automatically Find MM', 20, color.black,
                                     600, 150))
        self.button_list.append(NB.NavigationButton(self, long_button_image,
                                                    600, 240, 2, 7))
        self.text_list.append(MyText('Find MM Manually', 20, color.black, 600,
                                     240))
        self.button_list.append(NB.NavigationButton(self, long_button_image,
                                                    600, 330, 3, 7))
        self.text_list.append(MyText('Watch Algorithm To Find MM', 20,
                                     color.black, 600, 330))
        self.button_list.append(NB.NavigationButton(self, long_button_image,
                                                    600, 420, 4, 7))
        self.text_list.append(MyText('Watch Algorithm To Find MM With Steps',
                                     20, color.black, 600, 420))
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    510, 5, 4))
        self.text_list.append(MyText('Go Back', 20, color.black, 600, 510))
        self.render_buttons()

    # to state 7
    def execute_manual_operations(self):
        self.state = 7
        self.reset_text('')
        self.clear_buttons()
        button_image = games.load_image("images/button.png")
        self.button_list.append(NB.NavigationButton(self, button_image, 600,
                                                    510, 5, 5))
        self.text_list.append(MyText('Go Back', 20, color.black, 600, 510))
        self.render_buttons()
        

    #def advance(self, old_state, new_state):
    def advance(self, new_state):
        if (new_state == 1):
            self.set_left_branch_query()
        elif (new_state == 2):
            self.set_right_branch_query()
        elif (new_state == 3):
            self.set_edge_choice_query()
        elif (new_state == 4):
            self.set_manual_edge_choice_query()
        elif (new_state == 5):
            self.manual_operations_query()
        elif (new_state == 7):
            self.execute_manual_operations()
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
