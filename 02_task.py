class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, unit_of_weight, thickness):
        return f"{self._length * self._width * unit_of_weight * thickness / 1000:.2f} т"


road_1 = Road(20, 5000)
print(road_1.mass_of_asphalt(25, 5))
