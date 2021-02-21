import random

class Graph:
  def __init__(self):
    self.points = []

  def generate_point(self):
    self.points.append((random.random(), random.random()))

  def in_circle(self, x, y):
    return x ** 2 + y ** 2 <= 1

  def calc_pi(self):
    total = 0

    for i in range(len(self.points)):
      if self.in_circle(self.points[i][0], self.points[i][1]):
        total += 1
    
    return 4 * total / len(self.points)