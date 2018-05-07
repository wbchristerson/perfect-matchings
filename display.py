# New Graphics Window

from livewires import games
#import pygame

games.init(screen_width = 640, screen_height = 480, fps = 50)
#pygame.init()

class Pan(games.Sprite):

#    def __init__(self, sprite_image, x_coor, y_coor):
#        super(Pan, self).__init__(image = sprite_image, x = x_coor, y = y_coor)
#        self.was_clicked = False
#        self.x = x_coor
#        self.y = y_coor
    
    def update(self):
#        for event in pygame.event.get():
#            if (event.type == pygame.MOUSEBUTTONDOWN):
#                print('Click')
        self.x = games.mouse.x
        self.y = games.mouse.y
        

def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image
    pizza_image = games.load_image("pizza.bmp")

#    done = False
#    pygame.init()
    pizza = Pan(image = pizza_image, x = 320, y = 240)
    games.screen.add(pizza)
    #while (not done):
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            done = True
    games.screen.mainloop()

main()
