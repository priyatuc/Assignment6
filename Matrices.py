class MyMatrix:
    def __init__(self, rows, cols):
        # Create a rows x cols matrix initialized with zeros
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def access(self, r, c):
        self._validate(r, c)
        return self.data[r][c]

    def insert_row(self, r, row_values):
        if len(row_values) != self.cols:
            raise Exception("Row length mismatch.")
        self.data.insert(r, row_values)
        self.rows += 1

    def delete_row(self, r):
        self._validate(r, 0)
        del self.data[r]
        self.rows -= 1

    def insert_col(self, c, col_values):
        if len(col_values) != self.rows:
            raise Exception("Column length mismatch.")
        for i in range(self.rows):
            self.data[i].insert(c, col_values[i])
        self.cols += 1

    def delete_col(self, c):
        for i in range(self.rows):
            del self.data[i][c]
        self.cols -= 1

    def update(self, r, c, value):
        self._validate(r, c)
        self.data[r][c] = value

    def _validate(self, r, c):
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            raise Exception("Invalid matrix index.")

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

print("\n========== MATRIX DEMO ==========\n")

mat = MyMatrix(2, 3)

print("Initial 2x3 matrix:")
print(mat, "\n")

print("Updating (0,1) to 5...")
mat.update(0, 1, 5)
print(mat, "\n")

print("Updating (1,2) to 8...")
mat.update(1, 2, 8)
print(mat, "\n")

print("Inserting a new row [9, 9, 9] at index 1...")
mat.insert_row(1, [9, 9, 9])
print(mat, "\n")

print("Deleting column 1...")
mat.delete_col(1)
print(mat)

print("\nAccessing element at (1,1):", mat.access(1, 1))

