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
