from livewires import games
import constants

class Edge(games.Sprite):
    def __init__(self, responder, left_vertex, right_vertex, left_branch_size,
                 right_branch_size):
        left_y = 60 * left_vertex + 270 - 60 * int((left_branch_size - 1) / 2)
        right_y = 60 * right_vertex + 270 - 60 * int((right_branch_size - 1) / 2)
        offset = int((right_y - left_y) / 60)
        x_offset = 0
        y_offset = 0
        new_y = 0
        if (offset <= 0):
            (x_offset, y_offset) = constants.UP_OFFSETS[-offset]
            edge_image = games.load_image("images/up-edge-" + str(-offset) +
                                          ".png")
        else:
            (x_offset, y_offset) = constants.DOWN_OFFSETS[offset]
            edge_image = games.load_image("images/down-edge-" + str(offset) +
                                          ".png")
        left_y += y_offset
        super(Edge, self).__init__(image = edge_image, x = 60 + x_offset,
                                   y = left_y, is_collideable = False)
        self.left_vertex = left_vertex
        self.right_vertex = right_vertex
