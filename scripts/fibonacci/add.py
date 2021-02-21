def add(index, num1=0, num2=1, depth=0):
  if (depth == index):
    return num2
  return add(index, num2, num1 + num2, depth + 1)