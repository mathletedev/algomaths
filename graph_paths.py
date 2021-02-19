class Node:
  def __init__(self, name):
    self.connections = []
    self.name = name
  
  def add_connection(self, node):
    self.connections.append(node);

  def get_name(self):
    return self.name

  def get_connections(self):
    return self.connections

class Graph:
  def __init__(self, start, end):
    self.start = start;
    self.end = end
    self.counter = 0

  def get_paths(self, node, visited):
    counter = 0
    
    for connection in node.get_connections():
      if connection == self.end:
        counter += 1
        continue

      if connection in visited:
        continue

      counter += self.get_paths(connection, visited + [connection])

    return counter

  def get_all_paths(self):
    return self.get_paths(self.start, [self.start])

def connect_nodes(node1, node2):
  node1.add_connection(node2)
  node2.add_connection(node1)