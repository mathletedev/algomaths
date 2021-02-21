from graph import Graph

if __name__ == "__main__":
  n = int(input("Enter the number of iterations that the program should run: "))

  graph = Graph()

  for i in range(n):
    graph.generate_point()

  print(graph.calc_pi())
