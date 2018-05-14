from livewires import games

class Edge(games.Sprite):
    def __init__(self, responder, left_vertex, right_vertex, left_branch_size,
                 right_branch_size):
        edge_image = games.load_image("images/down-edge-1.png")
        super(Edge, self).__init__(image = edge_image, x = 100, y = 100,
                                   is_collideable = False)
        self.left_vertex = left_vertex
        self.right_vertex = right_vertex
