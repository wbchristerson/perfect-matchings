import GraphAlgorithm as GA
from livewires import games, color
import MyText as MT
import copy

#class AlgorithmDisplay(object):
class AlgorithmDisplay(games.Sprite):
    def __init__(self, responder):
        self.responder = responder
        self.left_size = responder.left_size
        self.right_size = responder.right_size
        self.left_neighbors = responder.left_neighbors
        image = games.load_image('images/phantom-pizza.bmp')
        super(AlgorithmDisplay, self).__init__(image = image, x = 0, y = 0,
                                               is_collideable = False)
        self.is_counting = False
        self.ticker = 0
        #self.left_index = 0
        #self.right_index = 0
        #self.in_greedy_stage = True # whether finding initial greedy matching
        self.has_highlighted_edge = False # whether an edge is being examined
        self.highlighted_edge = None # currently examined edge
        self.matching = []
        self.title_text = MT.MyText(new_value =
                                    'First find a matching greedily.',
                                    new_size = 30, new_color = color.black,
                                    new_x = 600, new_y = 50)
        games.screen.add(self.title_text)
        self.statement_text_A = MT.MyText(new_value = '', new_size = 30,
                                          new_color = color.black, new_x = 600,
                                          new_y = 150)
        self.statement_text_B = MT.MyText(new_value = '', new_size = 30,
                                          new_color = color.black, new_x = 600,
                                          new_y = 180)
        self.statement_text_C = MT.MyText(new_value = '', new_size = 30,
                                          new_color = color.black, new_x = 600,
                                          new_y = 210)
        games.screen.add(self.statement_text_A)
        games.screen.add(self.statement_text_B)
        games.screen.add(self.statement_text_C)
        ## whether in stage of using augmenting paths
        #self.in_augmenting_stage = False
        ## whether or not to terminate the algorithm upon finding a matching
        ## that does not use all vertices in the left branch
        #self.status = 1

        # state of algorithm: 1, 2, 3, or 4, see meanings below
        self.state = 1
        self.U = [] # list of left int vertices that are unmatched
        self.W = [] # list of right int vertices that are unmatched
        self.S = [] # list of reachable int vertices in left branch
        self.left_unmatched = [] # list of unmatched left vertex objects
        self.right_unmatched = [] # list of unmatched right vertex objects
        self.reachables = [] # list of reachable left vertex objects
        self.queue = []
        self.paths = []
        self.found_addition = 0
        self.left_index = 0
        self.right_index = 0
        
        
        #self.left_unmatched = [] # list of unmatched left vertex objects (U)
        #self.right_unmatched = [] # list of unmatched right vertex objects (W)
        ## list of vertex objects in left branch reachable from U (S)
        #self.left_reachables = []
        ## whether unmatched vertices have been selected
        #self.unmatched_displayed = False
        #self.queue = []
        #self.paths = []

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

        elif (self.state == 1):
            if (self.left_index == self.left_size):
                self.state = 2
                self.title_text.set_value('Search For Ways To Augment Paths')
                self.statement_text_A.set_value('')
                self.statement_text_B.set_value('')
                self.statement_text_C.set_value('')
                self.is_counting = True

            elif (not self.has_highlighted_edge):
                self.find_potential_edge()

            elif (self.has_highlighted_edge):
                self.add_or_reject_edge()

        elif (self.state == 2):
            if (len(self.matching) == self.left_size):
                self.state = 4
            else:
                self.left_unmatched = self.get_unmatched_left()
                self.right_unmatched = self.get_unmatched_right()
                self.reachables = self.get_unmatched_left()
                self.U = GA.set_left_unmatched(self.left_size, self.matching)
                self.W = GA.set_right_unmatched(self.right_size, self.matching)
                self.S = copy.deepcopy(self.U)
                self.queue = []
                self.paths = list(map(lambda x: [x], self.S))
                self.found_addition = 0
                self.left_index = 0
                self.right_index = 0
                self.display_unmatched()
                self.state = 3
                self.is_counting = True
        

        #elif (self.status and self.in_augmenting_stage and
        #      (not self.unmatched_displayed)):
        #    if (len(self.matching) < self.left_size):
        #        self.left_unmatched = self.get_unmatched_left()
        #        self.right_unmatched = self.get_unmatched_right()
        #        self.left_reachables = self.get_unmatched_left()
        #        self.queue = self.get_unmatched_left()
        #        self.paths = list(map(lambda x, [x.data], self.left_unmatched))
        #        #self.right_unmatched = GA.set_right_unmatched(self.right_size,
        #        #                                              self.matching)
        #        for vertex in self.left_unmatched:
        #            vertex.set_image(vertex.unmatched_image)
        #
        #        for vertex in self.right_unmatched:
        #            vertex.set_image(vertex.unmatched_image)
        #        self.unmatched_displayed = True
        #        self.statement_text.set_value('Highlight unmatched vertices ' +
        #                                      'in blue.')
        



        #elif (self.status and self.in_augmenting_stage and
        #      (len(self.queue) == 0)):
        #    self.status = 0

        #elif (self.status and self.in_augmenting_stage):
        #    found_addition = False
        #    while ((len(queue) > 0) and (not found_addition)):
        #        v = self.queue[0]
        #        self.queue = self.queue[1:]
        #        left_adjacency = copy.deepcopy(self.left_neighbors)
        #        if (GA.left_is_already_matched(v.data, self.matching)):
        #            left_adjacency[v.data].remove(GA.left_match(v.data,
        #                                                        self.matching))
        #        for r in left_adjacency[v.data]:
        #            if (self.is_in_right_unmatched(r)):
        #                v_path = GA.get_path(self.paths, v.data)
        #                r_path = copy.deepcopy(v_path)
        #                r_path.append(r)
        #                
        #                found_addition = True
        #                break


    def display_unmatched(self):
        for vertex in self.left_unmatched:
            vertex.set_image(vertex.unmatched_image)
        for vertex in self.right_unmatched:
            vertex.set_image(vertex.unmatched_image)
        self.statement_text_A.set_value('Highlight unmatched left vertices in ')
        self.statement_text_B.set_value('blue and unmatched right vertices in ')
        self.statement_text_C.set_value('yellow.')

    def is_in_right_unmatched(self, vertex_number):
        for v in self.right_unmatched:
            if (v.data == vertex_number):
                return True
        return False


    def get_unmatched_left(self):
        return list(filter(lambda x: not GA.left_is_already_matched(
            x.data, self.matching), self.responder.left_branch))

    def get_unmatched_right(self):
        return list(filter(lambda x: not GA.right_is_already_matched(
            x.data, self.matching), self.responder.right_branch))


    def find_potential_edge(self):
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
            self.statement_text_A.set_value('Test if this edge can be added.')

    def add_or_reject_edge(self):
        if (GA.right_is_already_matched(self.highlighted_edge.right_vertex,
                                        self.matching)):
            self.highlighted_edge.set_image(self.highlighted_edge.edge_image)
            if (self.right_index ==
                (len(self.left_neighbors[self.left_index]) - 1)):
                self.left_index += 1
                self.right_index = 0
            else:
                self.right_index += 1
            self.statement_text_A.set_value('The right vertex is already ' +
                                            'matched.')
            self.is_counting = True
        else:
            self.highlighted_edge.set_image(self.highlighted_edge.selected_image)
            self.matching.append((self.left_index,
                                  self.left_neighbors[self.left_index][self.right_index]))
            self.left_index += 1
            self.right_index = 0
            self.statement_text_A.set_value('The edge was added!')
            self.is_counting = True

        self.highlighted_edge = None
        self.has_highlighted_edge = False
