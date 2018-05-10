from livewires import games, color

# 640, 480
games.init(screen_width = 832, screen_height = 624, fps = 50)

####################################
# IDs:
#   0 - Vertex
#   1 - PhantomMouse
#   2 - MyText
#   3 - MyButton, number button
#   4 - MyButton, back button
####################################

class ClickableSprite(games.Sprite):
    def __init__(self, sprite_image, x, y, hovered_image, selected_image,
                 responder, number_status = 0, button_type = -1):
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
        self.number_status = number_status
        self.button_type = button_type

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
            games.keyboard.is_pressed(games.K_SPACE) and
            (not self.set_counter)):
            self.set_counter = True
            self.image = self.selected_image
            self.is_selected = True
            # transition to next step of query
            if (self.button_type == 4):
                self.responder.advance(self.number_status, -1)
                #self.is_selected = False
            elif (self.button_type == 3):
                self.responder.advance(self.number_status, 1)
        elif (is_chosen and self.is_selected and
              games.keyboard.is_pressed(games.K_SPACE) and
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
                 new_selected_image, responder, number_status, button_type,
                 new_text = ''):
        super(MyButton, self).__init__(new_image, new_x, new_y,
                                       new_hovered_image, new_selected_image,
                                       responder, number_status, button_type)
        self.id = button_type
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
        self.back_button = None # A button for maneuvering backwards in query
        self.back_button_text = None # Text object for text on back button
        self.button_image = games.load_image("button.png")
        self.hovered_button_image = games.load_image("hovered-button.png")
        self.selected_button_image = games.load_image("selected-button.png")

    # set up the display of all number buttons and update the appropriate
    # attributes of the Responses object
    def set_number_buttons(self):
        for i in range(5):
            self.button_list.append(MyButton(self.button_image, 550,
                                             90 + 55 * i,
                                             self.hovered_button_image,
                                             self.selected_button_image, self,
                                             i+1, 3, str(i+1)))
            self.text_list.append(MyText(str(i+1), 20, color.black, 550,
                                         90 + 55 * i))
        for i in range(5):
            self.button_list.append(MyButton(self.button_image, 700,
                                             90 + 55 * i,
                                             self.hovered_button_image,
                                             self.selected_button_image, self,
                                             i+6, 3, str(i+6)))
            self.text_list.append(MyText(str(i+6), 20, color.black, 700,
                                         90 + 55 * i))
        for b in self.button_list:
            games.screen.add(b)
        for t in self.text_list:
            games.screen.add(t)

    def set_left_branch_query(self):
        if (self.main_text_sprite):
            self.main_text_sprite.set_value('Left branch size:')
        else:
            self.main_text_sprite = MyText('Left branch size:', 30,
                                           color.black, 600, 30)
            games.screen.add(self.main_text_sprite)

        # if the back button is present, remove it
        if (self.back_button):
            self.back_button.destroy()
            self.back_button = None
            self.back_button_text.destroy()
            self.back_button_text = None

        if (len(self.button_list) == 0):
            self.set_number_buttons()
            #for i in range(5):
            #    self.button_list.append(MyButton(self.button_image, 550,
            #                                     90 + 55 * i,
            #                                     self.hovered_button_image,
            #                                     self.selected_button_image,
            #                                     self, i+1, 3, str(i+1)))
            #    self.text_list.append(MyText(str(i+1), 20, color.black, 550,
            #                                 90 + 55 * i))
            #for i in range(5):
            #    self.button_list.append(MyButton(self.button_image, 700,
            #                                     90 + 55 * i,
            #                                     self.hovered_button_image,
            #                                     self.selected_button_image,
            #                                     self, i+6, 3, str(i+6)))
            #    self.text_list.append(MyText(str(i+6), 20, color.black, 700,
            #                                 90 + 55 * i))
            #for b in self.button_list:
            #    games.screen.add(b)
            #for t in self.text_list:
            #    games.screen.add(t)

    # add a request number of vertices to the screen in one of the two branches;
    # also set the appropriate list attribute for the Responses object; also
    # add text button suggesting to go back
    def add_vertices(self, branch, branch_size):
        vertex_image = games.load_image("vertex.png")
        hovered_vertex = games.load_image("hovered-vertex.png")
        selected_vertex = games.load_image("selected-vertex.png")
        # place middle vertex at vertical position 310
        start = 310 - 60 * ((branch_size - 1) / 2)
        if (branch == 'left'):
            # Remove any currently present left vertices
            for vertex in self.left_branch:
                vertex.destroy()
            self.left_branch = []

            #m = Vertex(vertex_image, 100, start, hovered_vertex,
            #           selected_vertex,self)
            #games.screen.add(m)
            #self.left_branch.append(m)
            for i in range(branch_size):
                self.left_branch.append(Vertex(vertex_image, 100,
                                               60 * i + start, hovered_vertex,
                                               selected_vertex, self))
            for vertex in self.left_branch:
                games.screen.add(vertex)
        else:
            # Remove any currently present right vertices
            for vertex in self.right_branch:
                vertex.destroy()
            self.right_branch = []
            
            for i in range(branch_size):
                self.right_branch.append(Vertex(vertex_image, 440,
                                                60 * i + start, hovered_vertex,
                                                selected_vertex, self))
            for vertex in self.right_branch:
                games.screen.add(vertex)
        # set a back button if it is not present
        if (not self.back_button):
            self.back_button = MyButton(self.button_image, 625, 400,
                                        self.hovered_button_image,
                                        self.selected_button_image,
                                        self, -1, 4, 'Go Back')
            games.screen.add(self.back_button)
            self.back_button_text = MyText('Go Back', 25, color.black, 625, 400)
            games.screen.add(self.back_button_text)
       # else:
       #     self.back_button.image = self.back_button.plain_image
        #for i in range(10):
        #    for j in range(2):
        #        self.button_list.append(Vertex(vertex, 100 + 340 * j,
        #                                       70 * i + 30, hovered_vertex,
        #                                       selected_vertex))

    def reset_right_query_display(self):
        print("hello")
        self.back_button.image = self.back_button.plain_image
        self.back_button.is_selected = False
        self.set_number_buttons()

    def set_right_branch_query(self, number_status):
        self.main_text_sprite.set_value('Right branch size:')
        for button in self.button_list:
            button.image = button.plain_image
        if (number_status == -1):
            self.reset_right_query_display()
        else:
            self.left_size = number_status
            self.add_vertices('left', self.left_size)

    # choose whether you want a random edge set or the ability to choose which
    # edges are present
    def set_edge_choice_query(self, number_status):
        self.main_text_sprite.set_value('How do you want to choose edges?')
        self.main_text_sprite.set_x(self.main_text_sprite.get_x() + 50)
        for button in self.button_list:
            button.destroy()
        self.button_list = []
        for text in self.text_list:
            text.destroy()
        self.text_list = []
        self.right_size = number_status
        self.add_vertices('right', self.right_size)

    # number_status describes the answers to button queries, for example, the
    # number of vertices chosen for a particular branch; direction indicates
    # whether to advance forward or to go backwards, depending upon whether
    # direction is -1 or 1
    def advance(self, number_status, direction):
        print(str(self.state) + ' --> ' + str(self.state + direction))
        self.state += direction
        if (self.state == 1):
            self.set_left_branch_query()
        elif (self.state == 2):
            print(number_status)
            self.set_right_branch_query(number_status)
        elif (self.state == 3):
            self.set_edge_choice_query(number_status)

    def play(self):
        wall_image = games.load_image("wall-large.jpg")
        games.screen.background = wall_image
        self.advance(0, 1)
        games.screen.mainloop()


def main():
    phantom_mouse_image = games.load_image("phantom-pizza.bmp")
    pm = PhantomMouse(phantom_mouse_image)
    games.screen.add(pm)

    # class object to control responses to buttons
    controller = Responses()
    controller.play()

main()
