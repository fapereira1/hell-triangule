class HellTriangule():
    _triangule = None

    def __init__(self, triangule):
        self._triangule = triangule

    def hell_triangule(self):
        for row in range(len(self._triangule) - 1, 0, -1):
            for col in range(0, row):
                self._triangule[row - 1][col] += max(self._triangule[row][col], self._triangule[row][col + 1])
        return self._triangule[0][0]
