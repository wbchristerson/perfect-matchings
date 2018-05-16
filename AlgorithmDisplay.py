import GraphAlgorithm as GA
#import Timer as TI
from livewires import games

#class AlgorithmDisplay(object):
class AlgorithmDisplay(games.Sprite):
    def __init__(self, responder):
        self.responder = responder
        self.left_size = responder.left_size
        self.left_neighbors = responder.left_neighbors
        image = games.load_image('images/phantom-pizza.bmp')
        super(AlgorithmDisplay, self).__init__(image = image, x = 0, y = 0)
        self.is_counting = False
        self.ticker = 0
        self.left_index = 0
        self.right_index = 0
        self.in_greedy_stage = True # whether finding initial greedy matching
        self.has_highlighted_edge = False # whether an edge is being examined
        self.highlighted_edge = None # currently examined edge
        self.matching = []

    def get_edge(self, left_vertex, right_vertex):
        for edge in self.responder.edges:
            if ((edge.left_vertex == left_vertex) and
                (edge.right_vertex == right_vertex)):
                return edge
        return None

    def update(self):
        if (self.is_counting):
            self.ticker += 1
            if (self.ticker == 100):
                self.ticker = 0
                self.is_counting = False
                
        elif (self.left_index == self.left_size):
            self.in_greedy_stage = False
            
        elif ((self.in_greedy_stage) and (not self.has_highlighted_edge)):
            while ((self.left_index < self.left_size) and
                   (len(self.left_neighbors[self.left_index]) == 0)):
                self.left_index += 1
            if ((self.left_index < self.left_size) and
                (self.right_index < len(self.left_neighbors[self.left_index]))):
                edge = self.get_edge(self.left_index,
                                     self.left_neighbors[self.left_index][self.right_index])
                #print(self.left_neighbors[self.right_index])
                edge.set_image(edge.hovered_image)
                self.is_counting = True
                self.has_highlighted_edge = True
                self.highlighted_edge = edge

        elif ((self.in_greedy_stage) and self.has_highlighted_edge):
            if (GA.right_is_already_matched(self.highlighted_edge.right_vertex,
                                            self.matching)):
                self.highlighted_edge.set_image(self.highlighted_edge.edge_image)
                self.highlighted_edge = None
                self.has_highlighted_edge = False
                if (self.right_index ==
                    (len(self.left_neighbors[self.left_index]) - 1)):
                    self.left_index += 1
                    self.right_index = 0
                else:
                    self.right_index += 1
            else:
                self.highlighted_edge.set_image(self.highlighted_edge.selected_image)
                self.matching.append((self.left_index,
                                      self.left_neighbors[self.left_index][self.right_index]))
                self.left_index += 1
                self.right_index = 0
