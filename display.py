from livewires import games, color

# 640, 480
games.init(screen_width = 832, screen_height = 624, fps = 50)

class ClickableSprite(games.Sprite):
    def __init__(self, sprite_image, x, y, hovered_image, selected_image):
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
                 new_selected_image):
        super(Vertex, self).__init__(sprite_image, x_coor, y_coor,
                                     new_hovered_image, new_selected_image)
        #self.is_selected = False
        # set when to initiate the counter
        #self.set_counter = False
        # count number of steps since a change in vertex color
        #self.step_count = 0
        self.id = 0
        
    #pan = games.load_image("vertex.png")
    #hovered_pan = games.load_image("hovered-vertex.png")
    #selected_pan = games.load_image("selected-vertex.png")
    
#    def update(self):
#        is_chosen = False
#        if (self.set_counter and (self.step_count == 19)):
#            self.step_count = 0
#            self.set_counter = False
#        elif (self.set_counter):
#            self.step_count += 1
#
#        for item in self.overlapping_sprites:
#            if (item.id == 1):
#                is_chosen = True
#                break
#          
#        if (is_chosen and (not self.is_selected) and
#            (games.keyboard.is_pressed(games.K_SPACE)) and
#            (not self.set_counter)):
#            self.set_counter = True
#            self.image = self.selected_pan
#            self.is_selected = True
#        elif (is_chosen and self.is_selected and
#              (games.keyboard.is_pressed(games.K_SPACE)) and
#              (not self.set_counter)):
#            self.set_counter = True
#            self.image = self.pan
#            self.is_selected = False
#        elif (is_chosen and (not self.is_selected)):
#            self.image = self.hovered_pan
#        elif (not self.is_selected):
#            self.image = self.pan


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
                 new_selected_image, new_text = ''):
        super(MyButton, self).__init__(new_image, new_x, new_y,
                                       new_hovered_image, new_selected_image)
        self.id = 3
        self.text = new_text

# class to monitor changes in input
class Responses(games.Sprite):
    def __init__(self, screen, sprite_image):
        super(Responses, self).__init__(image = sprite_image, x = 0, y = 0)
        self.screen = screen
        self.state = 0

def main():
    wall_image = games.load_image("wall-large.jpg", transparent = False)
    games.screen.background = wall_image
    phantom_pizza_image = games.load_image("phantom-pizza.bmp")
    vertex = games.load_image("vertex.png")
    hovered_vertex = games.load_image("hovered-vertex.png")
    selected_vertex = games.load_image("selected-vertex.png")
    pizza_list = []
    #for i in range(5):
    #    for j in range(2):
    #        pizza_list.append(Vertex(pizza_image, 200 + 240 * j, 80 * i + 80))
    for i in range(10):
        for j in range(2):
            pizza_list.append(Vertex(vertex, 100 + 340 * j, 70 * i + 30,
                                     hovered_vertex, selected_vertex))
    pm = PhantomMouse(phantom_pizza_image)

    # class object to control responses to buttons
    controller = Responses(games.screen, phantom_pizza_image)
    
    for pizza in pizza_list:
        games.screen.add(pizza)
    games.screen.add(pm)

    left_choice_text = MyText('Left branch size:', 30, color.black, 600, 30)
    games.screen.add(left_choice_text)
    button_image = games.load_image("button.png")
    hovered_button_image = games.load_image("hovered-button.png")
    selected_button_image = games.load_image("selected-button.png")
    button_list = []
    text_list = []
    for i in range(5):
        button_list.append(MyButton(button_image, 550, 90 + 55 * i,
                                    hovered_button_image, selected_button_image,
                                    str(i+1)))
        text_list.append(MyText(str(i+1), 20, color.black, 550, 90 + 55 * i))
    for i in range(5):
        button_list.append(MyButton(button_image, 700, 90 + 55 * i,
                                    hovered_button_image, selected_button_image,
                                    str(i+6)))
        text_list.append(MyText(str(i+6), 20, color.black, 700, 90 + 55 * i))
    for b in button_list:
        games.screen.add(b)
    for t in text_list:
        games.screen.add(t)
        
    games.screen.mainloop()

main()
