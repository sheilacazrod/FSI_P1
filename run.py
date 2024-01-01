# Search methods

import search
options = [('A', 'B', 'Arad-Bucharest'), ('O', 'E', 'Oradea-Eforie'), ('G', 'Z', 'Giurgiu-Zerind'), ('N', 'D', 'Neamt-Dobreta'), ('M', 'F', 'Mehadia-Fagaras')]
for option in options:
    ab = search.GPSProblem(option[0], option[1], search.romania)

    print("\n>> ", option[2], " <<\n")
    print("Breadth: ", search.breadth_first_graph_search(ab).path())
    print("Depth: ", search.depth_first_graph_search(ab).path())
    print("Brand & Bound: ", search.branch_and_bound_search(ab).path())
    print("Branch & Bound H: ", search.branch_and_bound_search_sub(ab).path())
    print("-----------------------------------------------------------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
