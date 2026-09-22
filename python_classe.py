def add_numbers(num1, num2):
    return num1 + num2

class Bottle:
    def __init__(self, capacity, size, color, material):
        self.capacity = capacity
        self.size = size
        self.color = color
        self.material = material

    def fill(self):
        self.color = self.color.upper()
        print(f"The {self.color} bottle is filled with liquid.")

bottle1 = Bottle(500, "Medium", "Blue", "Plastic")
print(bottle1.capacity, bottle1.size, bottle1.color, bottle1.material)
print(f"Bottle 1: {bottle1.size}, {bottle1.color}, {bottle1.material}")
bottle2 = Bottle(1000, "Large", "Green", "Glass")
bottle2.fill()
print(f"Bottle 2: {bottle2.size}, {bottle2.color}, {bottle2.material}")
bottle3 = Bottle(250, "Small", "Red", "Metal")
bottle3.fill()
print(f"Bottle 3: {bottle3.size}, {bottle3.color}, {bottle3.material}")
