class MyArray:
    def __init__(self, capacity):
        # Create a fixed-size array
        self.capacity = capacity
        self.data = [None] * capacity
        self.length = 0

    def insert(self, index, value):
        if self.length == self.capacity:
            raise Exception("Array is full.")
        if index < 0 or index > self.length:
            raise Exception("Invalid index.")

        for i in range(self.length - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]

        self.data[index] = value
        self.length += 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid index.")

        deleted_value = self.data[index]

        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.length - 1] = None
        self.length -= 1
        return deleted_value

    def access(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid index.")
        return self.data[index]

    def update(self, index, value):
        if index < 0 or index >= self.length:
            raise Exception("Invalid index.")
        self.data[index] = value

    def __str__(self):
        return str(self.data[:self.length])

print("========== ARRAY DEMO ==========\n")

arr = MyArray(10)

print("Inserting 5 at index 0...")
arr.insert(0, 5)
print("Array now:", arr, "\n")

print("Inserting 10 at index 1...")
arr.insert(1, 10)
print("Array now:", arr, "\n")

print("Inserting 7 at index 1 (between 5 and 10)...")
arr.insert(1, 7)
print("Array now:", arr, "\n")

print("Deleting value at index 1 (which is 7)...")
deleted = arr.delete(1)
print("Deleted value:", deleted)
print("Array now:", arr, "\n")

print("Accessing element at index 1...")
value = arr.access(1)
print("Value at index 1:", value, "\n")

print("Updating index 1 to new value 20...")
arr.update(1, 20)
print("Array now:", arr)
