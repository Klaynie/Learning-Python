class Sphere:
    pi_ = 3.1415

    def __init__(self, rad_):
        self.rad_ = rad_
        self.volume = 4 / 3 * Sphere.pi_ * rad_ ** 3

sphere = Sphere(3)

print(sphere.volume)