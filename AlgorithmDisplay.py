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
        else:
            if ((self.left_index < self.left_size) and
                (self.right_index < len(self.left_neighbors[self.left_index]))):
                edge = self.get_edge(self.left_index,
                                     self.left_neighbors[self.left_index][self.right_index])
                #print(self.left_neighbors[self.right_index])
                edge.set_image(edge.hovered_image)
                self.is_counting = True
                if (self.right_index == (len(self.left_neighbors[self.left_index]) - 1)):
                    self.left_index += 1
                    self.right_index = 0
                else:
                    self.right_index += 1


    #def greedy_matching(self, left_size, left_neighbors):
    #    matching = []
    #    for i in range(left_size):
    #        for j in left_neighbors[i]:
    #            edge = self.get_edge(i, j)
    #            edge.set_image(edge.hovered_image)
    #            t = TI.Timer(self.responder)
    #            
    #            if (not GA.right_is_already_matched(j, matching)):
    #                matching.append((i,j))
    #                edge.set_image(edge.selected_image)
    #                break
    #            else:
    #                edge.set_image(edge.edge_image)
                
