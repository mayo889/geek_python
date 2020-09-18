class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        ans = ""
        for row in self.arr:
            for elem in row:
                ans += f"{str(elem):5s} "
            ans += '\n'
        return ans

    def __add__(self, other):
        arr = []
        for i in range(len(self.arr)):
            arr.append([])
            for j in range(len(self.arr[0])):
                arr[i].append(self.arr[i][j] + other.arr[i][j])
        return Matrix(arr)

    def __eq__(self, other):
        if len(self.arr) != len(other.arr):
            return False
        for i in range(len(self.arr)):
            if len(self.arr[i]) != len(other.arr[i]):
                return False
        return True


matrix_1 = Matrix([[1, -2, 4], [2, 0, -1]])
matrix_2 = Matrix([[5, 2, 3], [4, 6, 2]])
print(matrix_1)
print(matrix_2)
if matrix_1 == matrix_2:
    print("Матрицы равны, результат сложения:")
    print(matrix_1 + matrix_2)
else:
    print("Складывать матрицы можно только одинакового размера!")
