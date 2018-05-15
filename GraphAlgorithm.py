#class GraphAlgorithm(object):
#    def __init__(self, responder):
#        self.responder = responder
#        self.matching = []
#        self.left_size = responder.left_size
#        self.right_size = responder.right_size
#        self.left_neighbors = list(responder.left_neighbors) # deep copy
#        self.right_neighbors = list(responder.right_neighbors) # deep copy
#
#    # checks whether a vertex of the right branch is already matched in an edge
#    # within self.matching
#    def is_already_matched(self, vertex):
#        for (a,b) in self.matching:
#            if (b == vertex):
#                return True
#        return False
#
#    def greedy_matching(self):
#        for i in range(left_size):
#            for j in self.left_neighbors[i]:
#                if (not self.is_already_matched(j)):
#                    self.matching.append((i, j))
#                    break

# check if a vertex in the left branch is matched within 'matching'
import copy

def left_is_already_matched(vertex, matching):
    for (a,b) in matching:
        if (a == vertex):
            return True
    return False

# check if a vertex in the right branch is matched within 'matching'
def right_is_already_matched(vertex, matching):
    for (a,b) in matching:
        if (b == vertex):
            return True
    return False

def greedy_matching(left_size, left_neighbors):
    matching = []
    for i in range(left_size):
        for j in left_neighbors[i]:
            if (not right_is_already_matched(j, matching)):
                matching.append((i,j))
                break
    return matching

#def get_left_unmatched(left_size, matching):
#    left_unmatched = []
#    for i in range(left_size):
#        if (not


# return the list (path) in paths ending at vertex s in S
def get_path(paths, s):
    for path in paths:
        if (path[-1] == s):
            return path
    return None

# given an augmenting path aug_path in the bipartite graph, update the matching
# to take advantage aug_path
def flip_path(aug_path, matching):
    #new_matching = list(matching)
    new_matching = copy.deepcopy(matching)
    for i in range(int(len(aug_path) / 2) - 1):
        new_matching.append((aug_path[2 * i], aug_path[2 * i + 1]))
        new_matching.remove((aug_path[2 * i + 2], aug_path[2 * i + 1]))
    new_matching.append((aug_path[-2], aug_path[-1]))
    return new_matching
    

# given a vertex of the left branch which is matched, return its matched vertex
# in the right branch
def left_match(s, matching):
    for (a,b) in matching:
        if (a == s):
            return b
    return -1

# given a vertex of the right branc which is matched, return its matched vertex
# in the left branch
def right_match(s, matching):
    for (a,b) in matching:
        if (b == s):
            return a
    return -1

# update the matching
#def maximum_matching(left_size, right_size, left_neighbors):
def update_matching(left_size, right_size, matching, left_neighbors):
    # initialization
    #matching = greedy_matching(left_size, left_neighbors)

    # loop
    U = list(filter(lambda x: not left_is_already_matched(x, matching),
                    range(left_size)))
    W = list(filter(lambda y: not right_is_already_matched(y, matching),
                    range(right_size)))
    # set of reachable vertices in left branch using almost augmenting paths
    #S = list(U)
    S = copy.deepcopy(U)
    #queue = list(U) # queue of left-branch vertices to check
    queue = copy.deepcopy(U)
    paths = list(map(lambda x: [x], S))
    while (len(queue) > 0):
        s = queue[0]
        queue = queue[1:]
        # prevent extension of almost augmenting paths from left branch by an
        # edge of the matching
        #left_adjacency = list(left_neighbors)
        left_adjacency = copy.deepcopy(left_neighbors)
        if (left_is_already_matched(s, matching)):
            left_adjacency[s].remove(left_match(s, matching))
        for r in left_adjacency[s]:
            if (r in W):
                s_path = get_path(paths, s)
                r_path = list(s_path)
                r_path.append(r)
                #print('s_path: ', s_path)
                #r_path = s_path.append(r)
                return (flip_path(r_path, matching), 0)
            else:
                t = right_match(r, matching)
                if (not (t in S)):
                    S.append(t)
                    queue.append(t)
                    s_path = get_path(paths, s)
                    t_path = list(s_path)
                    t_path.append(r)
                    t_path.append(t)
                    paths.append(t_path)
    return (matching, -1)
    # if while loop finished, then there is no perfect matching, return matching
    # and None

def maximum_matching(left_size, right_size, left_neighbors):
    matching = greedy_matching(left_size, left_neighbors)
    status = 0
    while ((len(matching) < left_size) and (status == 0)):
        (new_matching, new_status) = update_matching(left_size, right_size,
                                                     matching, left_neighbors)
        matching = list(new_matching)
        status = new_status
    print('Matching: ', matching)
