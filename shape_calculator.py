class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return self.__class__.__name__ + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        to_print = ''
        for i in range(self.height):
            to_print += '*' * self.width
            to_print += '\n'
        return to_print

    def get_amount_inside(self, shape):
        r = self.get_area() // shape.get_area()
        return r


class Square(Rectangle):
        
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __str__(self) -> str:
        return self.__class__.__name__ + '(side=' + str(self.side) + ')'

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)
