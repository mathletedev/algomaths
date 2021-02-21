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