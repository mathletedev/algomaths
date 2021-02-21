def increment(index, row=[1], depth=0):
  if depth == index:
    return row

  tmp = []
  zeros = [0] + row + [0]
  for i in range(len(zeros) - 1):
    tmp.append(zeros[i] + zeros[i + 1])

  return increment(index, tmp, depth + 1)
  