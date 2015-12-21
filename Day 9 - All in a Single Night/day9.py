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


def main():

    f = open('input.txt', 'r')
    dict = {}

    for line in f:     # Build the graph from the data in the file
       linestr = line.strip('\n')
       linestr = linestr.split(' ')

       source = linestr[0]
       dest = linestr[2]
       weight = int(linestr[4])

       if source not in dict.keys():
           dict[source] = list()

       dict[source].append((dest, weight))
         
    i = 0
    for d in dict:
        i += 1
        print('Node {}: {}\nx{} Neighbors: {}').format(i, d, len(dict.get(d)), dict.get(d))
        
                
if __name__ == '__main__':
    main()

