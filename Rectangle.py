class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Custom iterator
    def __iter__(self):
        # Yielding the length first, followed by the width
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(10, 5)

for dimension in rect:
    print(dimension)
