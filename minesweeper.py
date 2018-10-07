def minesweeper(matrix):




def padMatrix(matrix):
  matrix.insert(0, [])
  for i in range(len(matrix[1])):
    matrix[0].insert(0, False)
  matrix.append([])
  for i in range(len(matrix[0])):
    matrix[len(matrix[0]) + 1].append(False)
  for i in range(len(matrix)):
    matrix[i].insert(0, False)
    matrix[i].append(False)
  return matrix
