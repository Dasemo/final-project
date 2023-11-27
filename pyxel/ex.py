import random
class Enemy:
    def __init__(self, x: int, y: int):
        # All the self.something are attributes
        self.x = x
        self.y = y
                # direct is a local variable
        direct = random.randint(0, 1)
        if direct == 1:
            self.direction = "right"
        else:
            self.direction = "left"
        self.image = "image.png"
    
    @property
    def x(self) -> int:
        return self.__x
    @x.setter
    def x(self, x2 : int):
        if(type(x2)) is not int:
            raise TypeError("The value of the position must be a number.")
        elif x2 < 0:
            raise ValueError("Enemies can not have negative positions!")
        else:
            self.__x = x2
    @property
    def y(self) -> int:
        return self.__y
    @y.setter
    def y(self, y2 : int):
        if(type(y2)) != int:
            raise TypeError("The value of the position must be a number.")
        elif y2 < 0:
            raise ValueError("Enemies can not have negative positions!")
        else:
            self.__y = y2

    def __str__(self):
        return f"Enemy at position({str(self.x)}, {str(self.y)}), going {self.direction}"

enemy3 = Enemy(23, 5)
print(enemy3)