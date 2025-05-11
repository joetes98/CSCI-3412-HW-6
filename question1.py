import sys
from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance

  # This method is for MST only
  def initializeDistances(self):
    for i in self.nodes:
        for j in self.nodes:
            self.distances[(i, j)] = sys.maxsize

    for i in self.nodes:
       self.distances[(i, "")] = 0


def dijkstra(graph, s):
    visited = {s: 0}; path = {}; selected = []
    nodes = set(graph.nodes)

    print(f"Source node: {s} (= 0)")
    print("All other nodes: infinity\n")

    while nodes: # while remaining nodes
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                  min_node = node
                elif visited[node] < visited[min_node]:
                  min_node = node

        if min_node is None:
          break

        selected.append(min_node) # append min_node to selected list
        print(f"Node({min_node}) with Weight:{visited[min_node]} is added to the 'Visited' {sorted(selected)}")
        nodes.remove(min_node) # selected
        current_weight = visited[min_node]

        relaxation = False
        for v in graph.edges[min_node]:
            old_weight = visited[v] if v in visited else float('inf')
            weight = current_weight + graph.distances[(min_node, v)] # relaxation
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                path[v] = min_node
                relaxation = True
                print(f"Relaxed: vertex[{v}]: OLD:{'Infinity' if old_weight == float('inf') else old_weight}, NEW:{weight}, Paths:{path}")

            # If no relaxation needed (print statement for output)
            if not relaxation:
              print(f"No edge relaxation is needed for node, {v}")

        # Check if the node has no outgoing edges
        if not graph.edges[min_node]:
            print(f"No outgoing edge from the node, {min_node}")

    return visited, path

def main():
   
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 3)
    graph.add_edge("B", "D", 2)
    graph.add_edge("B", "E", 3)
    graph.add_edge("C", "D", 4)
    graph.add_edge("C", "E", 5)
    graph.add_edge("C", "B", 1)
    graph.add_edge("E", "D", 1)

    startingNode = "A"

    visited, paths = dijkstra(graph, startingNode)

    print(f"{visited}, {paths}")

if __name__ == "__main__":
        main()