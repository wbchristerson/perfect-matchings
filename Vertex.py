from livewires import games

class Vertex(games.Sprite):
    def __init__(self, responder, x, y, data):
        vertex_image = games.load_image("images/vertex.png")
        hovered_image = games.load_image("images/hovered-vertex.png")
        selected_image = games.load_image("images/selected-vertex.png")
        super(Vertex, self).__init__(image = vertex_image, x = x, y = y,
                                     is_collideable = False)
        self.data = data
        self.plain_image = vertex_image
        self.hovered_image = hovered_image
        self.selected_image = selected_image
        self.is_selectable = False # whether the vertex may be selected
        self.responder = responder
        self.step_count = 0 # counter to give time between button selections
        self.is_counting = False # whether counter is currently incrementing
        self.is_hovered = False # whether the mouse is hovering over vertex

    def update(self):
        if (self.is_counting):
            self.step_count += 1
            if (self.step_count == 20):
                self.is_counting = False
                self.step_count = 0
        else:
            mouse_touching = False
            for item in self.overlapping_sprites:
                if (item.id == 0):
                    mouse_touching = True
                    break
            if (mouse_touching and (not self.is_hovered) and
                (self.responder.state == 4)):
                self.is_hovered = True
                self.set_image(self.hovered_image)
            elif ((not mouse_touching) and self.is_hovered):
                self.is_hovered = False
                self.set_image(self.plain_image)

        
