#possibly ok?
def minesweeper(matrix):
  adjacentMines = []
  finalMatrix = []
  matrixB = padMatrix(matrix)
  print (matrixB)
  for i in range(1, len(matrixB) - 1):
    for j in range(1, len(matrixB[i]) - 1):
      sumAdjacentMines = matrixB[i - 1][j - 1] + matrixB[i - 1][j] + matrixB[i - 1][j + 1] + matrixB[i][j - 1] + matrixB[i][j + 1] + matrixB[i + 1][j - 1] + matrixB[i + 1][j] + matrixB[i + 1][j + 1]
      adjacentMines.append(sumAdjacentMines)
      


  for i in range(0, len(adjacentMines), len(matrix[0]) - 2):
    finalMatrix.append(adjacentMines[i: i + len(matrix[0]) - 2])
  return finalMatrix

#must fix, this makes no sense and doesn't work
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

