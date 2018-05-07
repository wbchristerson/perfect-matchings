from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    def __init__(self, sprite_image, x_coor, y_coor):
        super(Pan, self).__init__(image = sprite_image, x = x_coor, y = y_coor)
        self.is_selected = False
        self.set_counter = False
        # count number of steps since a change in vertex color
        self.step_count = 0
#        self.was_clicked = False
#        self.x = x_coor
#        self.y = y_coor
    pan = games.load_image("vertex.png")
    hovered_pan = games.load_image("hovered-vertex.png")
    selected_pan = games.load_image("selected-vertex.png")
    
    def update(self):
        if (self.set_counter and (self.step_count == 19)):
            self.step_count = 0
            self.set_counter = False
        elif (self.set_counter):
            self.step_count += 1
            
        if ((len(self.overlapping_sprites) > 0) and (not self.is_selected) and
            (games.keyboard.is_pressed(games.K_SPACE)) and
            (not self.set_counter)):
            self.set_counter = True
            self.image = self.selected_pan
            self.is_selected = True
        elif ((len(self.overlapping_sprites) > 0) and self.is_selected and
              (games.keyboard.is_pressed(games.K_SPACE)) and
              (not self.set_counter)):
            self.set_counter = True
            self.image = self.pan
            self.is_selected = False
        elif ((len(self.overlapping_sprites) > 0) and (not self.is_selected)):
            self.image = self.hovered_pan
        elif (not self.is_selected):
            self.image = self.pan

# check mouse hovers by having an imageless sprite follow the mouse
class PhantomMouse(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y

def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image
    pizza_image = games.load_image("vertex.png")
    phantom_pizza_image = games.load_image("phantom-pizza.bmp")
    pizza_list = []
    for i in range(5):
        for j in range(2):
            pizza_list.append(Pan(pizza_image, 200 + 240 * j, 80 * i + 80))
    pm = PhantomMouse(image = phantom_pizza_image)
    for pizza in pizza_list:
        games.screen.add(pizza)
    games.screen.add(pm)
    games.screen.mainloop()

main()
