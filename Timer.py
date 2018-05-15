from livewires import games

class Timer(games.Sprite):
    def __init__(self, responder):
        self.responder = responder
        image = games.load_image('images/phantom-pizza.bmp')
        super(Timer, self).__init__(image = image)
        self.tick = 0
        self.is_finished = False

    def update(self):
        if (not self.is_finished):
            self.tick += 1
        if (self.tick == 1):
            self.is_finished = True
