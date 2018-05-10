from livewires import games

class NavigationButton(games.Sprite):
    def __init__(self, responder, plain_image, x, y, data, state, button_type):
        super(NavigationButton, self).__init__(image = plain_image, x = x,
                                               y = y)
        self.data = data
        self.state = state
        self.button_type = button_type
        self.is_selected = False # whether button has been pushed
        self.set_counter = False # set true when counter is currently on
        self.step_count = 0 # count number of steps since a button push
        self.responder = responder # navigation object from main.py

    def update(self):
        mouse_touching = False
        
