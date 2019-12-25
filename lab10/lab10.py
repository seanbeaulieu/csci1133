import turtle
class Rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
       
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
   
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return '0'
        else:
            return str(self.numerator) + '/' + str(self.denominator)


class SpaceCoins:
    def __init__(self, pues=0, ningis=0):

        self.pues = pues
        self.ningis = ningis
        while self.ningis >= 8:
            self.ningis -= 8
            self.pues += 1
        while self.ningis < 0:
            self.ningis += 8
            self.pues -= 1

    def __str__(self):
        if self.ningis == 0 or self.pues == 0:
            if self.ningis == 0 and self.pues == 0:
                return '0*'
            elif self.ningis == 0:
                return str(self.pues) + '^'
            elif self.pues == 0:
                return str(self.ningis) + '*'
        else:
            return str(self.pues) + '^' + str(self.ningis) + '*'
        
    def __add__(self,other):
        return SpaceCoins(self.pues + other.pues, self.ningis + other.ningis)

    def __sub__(self,other):
        return SpaceCoins(self.pues - other.pues, self.ningis - other.ningis)


class Vec2:
    def __init__(self, x=0, y=0):
        self.xcor = x
        self.ycor = y

    def __str__(self):
        return '<' + str(self.xcor) + ', ' + str(self.ycor) + '>'

    def get_values(self):
        return [self.xcor, self.ycor]

    def set_values(self, l1):
        self.xcor = l1[0]
        self.ycor = l1[1]

    def __add__(self, other):
        return Vec2(self.xcor + other.xcor, self.ycor + other.ycor)

    def __sub__(self, other):
        return Vec2(self.xcor - other.xcor, self.ycor - other.ycor)

    def __mul__(self, val):
        return Vec2(self.xcor * val, self.ycor * val)


class Particle:
    def __init__(self, mass=0,position=Vec2(),velocity=Vec2()):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        turtle1 = turtle.Turtle()
        turtle1.shape() = circle
        turtle1.speed() = 0
    

    















    
