from graph import Graph
from node import Node

if __name__ == "__main__":
  A = Node("A")
  B = Node("B")
  C = Node("C")

  graph = Graph(A, C)

  graph.connect_nodes(A, B)
  graph.connect_nodes(B, C)
  graph.connect_nodes(A, C)

  print(graph.get_all_paths())