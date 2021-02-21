def increment(index, row=[1], depth=0):
  if depth == index:
    return row

  tmp = [1]
  for i in range(len(row) - 1):
    tmp.append(row[i] + row[i + 1])

  tmp.append(1)

  return increment(index, tmp, depth + 1)