import GraphAlgorithm as GA
#import Timer as TI

class AlgorithmDisplay(object):
    def __init__(self, responder):
        self.responder = responder
        self.left_size = responder.left_size
        self.left_neighbors = responder.left_neighbors

    def get_edge(self, left_vertex, right_vertex):
        for edge in self.responder.edges:
            if ((edge.left_vertex == left_vertex) and
                (edge.right_vertex == right_vertex)):
                return edge
        return None

    def greedy_matching(self, left_size, left_neighbors):
        matching = []
        for i in range(left_size):
            for j in left_neighbors[i]:
                edge = self.get_edge(i, j)
                edge.set_image(edge.hovered_image)
                #t = TI.Timer(self.responder)
                #while(not t.is_finished):
                #    print('hello')
                if (not GA.right_is_already_matched(j, matching)):
                    matching.append((i,j))
                    edge.set_image(edge.selected_image)
                    break
                else:
                    edge.set_image(edge.edge_image)
                
