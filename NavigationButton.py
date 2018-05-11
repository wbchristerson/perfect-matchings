from livewires import games

class NavigationButton(games.Sprite):
    def __init__(self, responder, plain_image, x, y, data, destination_state):
        super(NavigationButton, self).__init__(image = plain_image, x = x,
                                               y = y)
        self.data = data # data value obtained from selected this button
        # state to which button takes user
        self.destination_state = destination_state
        self.is_selected = False # whether button has been pushed
        self.step_count = 0 # count number of steps since a button push
        self.responder = responder # navigation object from main.py

    def update(self):
        if (self.step_count < 20): # provide time between transitions
            self.step_count += 1
        else:
            mouse_touching = False
            for item in self.overlapping_sprites:
                if (item.id == 0):
                    mouse_touching = True
                    break
            if (mouse_touching):
                self.responder.advance(self.destination_state)
