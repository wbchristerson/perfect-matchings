from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
#    def __init__(self, sprite_image, x_coor, y_coor):
#        super(Pan, self).__init__(image = sprite_image, x = x_coor, y = y_coor)
#        self.was_clicked = False
#        self.x = x_coor
#        self.y = y_coor
    pan = games.load_image("hovered-vertex.png")
    def update(self):
        if (len(self.overlapping_sprites) > 0):
            self.image = self.pan
#        for event in pygame.event.get():
#            if (event.type == pygame.MOUSEBUTTONDOWN):
#                print('Click')
#        self.x = games.mouse.x
#        self.y = games.mouse.y

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
    pizza = Pan(image = pizza_image, x = 320, y = 240)
    pm = PhantomMouse(image = phantom_pizza_image)
    games.screen.add(pizza)
    games.screen.add(pm)
    games.screen.mainloop()

main()
