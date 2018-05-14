from livewires import games
import constants

class Edge(games.Sprite):
    def __init__(self, responder, left_vertex, right_vertex, left_branch_size,
                 right_branch_size):
        left_y = 60 * left_vertex + 270 - 60 * int((left_branch_size - 1) / 2)
        right_y = 60 * right_vertex + 270 - 60 * int((right_branch_size - 1) / 2)
        stable_left_y = left_y
        stable_right_y = right_y
        offset = int((right_y - left_y) / 60)
        x_offset = 0
        y_offset = 0
        new_y = 0
        if (offset <= 0):
            (x_offset, y_offset) = constants.UP_OFFSETS[-offset]
            edge_image = games.load_image("images/up-edge-" + str(-offset) +
                                          ".png")
            self.edge_image = edge_image
            hovered_image = games.load_image("images/hovered-up-edge-" +
                                             str(-offset) + ".png")
            self.hovered_image = hovered_image
        else:
            (x_offset, y_offset) = constants.DOWN_OFFSETS[offset]
            edge_image = games.load_image("images/down-edge-" + str(offset) +
                                          ".png")
            self.edge_image = edge_image
            hovered_image = games.load_image("images/hovered-down-edge-" +
                                             str(offset) + ".png")
            self.hovered_image = hovered_image
        left_y += y_offset
        super(Edge, self).__init__(image = edge_image, x = 60 + x_offset,
                                   y = left_y, is_collideable = False)
        self.left_vertex = left_vertex
        self.right_vertex = right_vertex
        self.offset = offset
        self.hovered = False
        self.responder = responder
        # slope of edge on screen
        self.slope = (stable_right_y - stable_left_y) / 340
        # y-intercept of line through edge
        self.intercept = stable_left_y - 60 * self.slope

    def update(self):
        if ((self.responder.state == 7) and (not self.hovered) and
            self.mouse_touching()):
            self.set_image(self.hovered_image)
            self.hovered = True
        elif ((self.hovered) and (not self.mouse_touching())):
            self.hovered = False
            self.set_image(self.edge_image)

    def mouse_touching(self):
        if (games.mouse.x < 60):
            return False
        elif (games.mouse.x > 400):
            return False
        function_val = games.mouse.x * self.slope + self.intercept
        if ((-10 > (function_val - games.mouse.y)) or
            ((function_val - games.mouse.y) > 10)):
            return False
        return True
