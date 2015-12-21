# --- Day 9: All in a Single Night ---
# 
# Every year, Santa manages to deliver all of his presents in a single night.
# 
# This year, however, he has some new locations to visit; his elves have
# provided him the distances between every pair of locations. He can start
# and end at any two (different) locations he wants, but he must visit each
# location exactly once. What is the shortest distance he can travel to
# achieve this?
# 
# For example, given the following distances:
# 
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# 
# The possible routes are therefore:
# 
# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# 
# The shortest of these is London -> Dublin -> Belfast = 605, and so the
# answer is 605 in this example.
# 
# What is the distance of the shortest route?

## Graph data structure courtesy of
##  http://www.bogotobogo.com/python/python_graph_data_structures.php

import heapq

class Vertex:
    """ The VERTEX class represents a collection of the vertices in a graph.
    Each vertex  has a name (id) and a dictionary of its neighbors (key)
    associated weights (value).
    """
    
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str([x.id for x in self.adjacent])


    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    """ The GRAPH class contains the master list of VERTICES in a graph.

    It contains a dictionary of the vertices, as well as the control mechanisms
    to add vertices and their associated edge data to the graph.

    The GRAPH class considers the graph to be directed
    (e.g., an undirected graph will have a weight:edge pair)
        EX: A --(10)--> B       B --(10)--> A
    """
    
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def del_vertex(self, node):
        self.num_vertices = self.num_vertices - 1
        del self.vert_dict[node]
        return None

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)


    def get_vertices(self):
        return self.vert_dict.keys()

    def greedy(self, startnode, sum = None, path = None):

        if path is None:
            path = []

        if sum is None:
            sum = 0

        newsum = None
        node = self.get_vertex(startnode)

        i = 0

        # print('\tEntering greedy() with Node {} / Path {} / Sum {}').format(node.get_id(), path, sum)

        for neighbor in node.get_connections():
            i += 1
            # print('Node: {}:\t\tNeighbor ({}): {} ({})').format(node.get_id(), i, neighbor.get_id(), node.get_weight(neighbor))
            # print('\t\tChecking weight of {}').format(neighbor.get_id())

            # select the smallest neighbor
            if neighbor.get_id() in path:
            #    print('\t\t\tNeighbor {} is already in the path').format(neighbor.get_id())
                continue

            # elif (newsum is None) or (newsum > node.get_weight(neighbor)):        # PART I
            elif (newsum is None) or (newsum < node.get_weight(neighbor)):          # PART II
                # print('\t\t\tset lowest weight:\t{} {}').format(neighbor.get_id(), node.get_weight(neighbor))
                newsum = node.get_weight(neighbor)
                nextnode = neighbor.get_id()

        if newsum == None:
            return sum, path

        else:
            sum += newsum
            path.append(node.get_id())

            # print('\t\tDone checking {}. Lowest weight is {} ({})').format(node.get_id(),newsum, nextnode)
            # print('\t\tNew sum is {}\tThe Current path is {}').format(sum, path)

            newsum, newpath = self.greedy(nextnode, sum, path)

        # print('\tExiting greedy() with path {} and sum {}').format(newpath, newsum)
        return newsum, newpath

def main():
    

    f = open('input.txt', 'r')
    g = Graph()
    dict = {}

    for line in f:     # Build the graph from the data in the file
       linestr = line.strip('\n')
       linestr = linestr.split(' ')

       g.add_edge(linestr[0], linestr[2], int(linestr[4]))
            
    print('--- NODE LIST ---------------')
    for v in g:
        print('{}').format(v.get_id())

    print('\n--- ADJACENCY LIST ----------')
    for v in g:
        print('\n{}').format(v.get_id())
        for w in v.get_connections():
            print '\t{}\t{}'.format(v.get_weight(w), w.get_id())

    print('\n--- ALL PATHS ----------')
    for v in g:
        greedypath = g.greedy(v.get_id())
        dict[v.get_id()] = greedypath[0]

        print('\t{}\t(dist {} / {} hops)').format(greedypath[1], greedypath[0], len(greedypath[1]))

    # print ('\n\tOverall shortest greedy path is {} with a total distance of {}').format(min(dict, key=dict.get), dict[min(dict, key=dict.get)])   # PART I
    print ('\n\tOverall shortest greedy path is {} with a total distance of {}').format(max(dict, key=dict.get), dict[max(dict, key=dict.get)])     # PART II
                
if __name__ == '__main__':
    main()

