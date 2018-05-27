import turtle

class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""

    def forward(self,pixel):
        super().backward(pixel)

    def backward(self,fixel):
        super().forward(fixel)

    def left(self,angle):
        super().right(angle)

    def right(self,angle):
        '''super().left(angle)'''
        print('I won\'t turn right, because I an ajob!')

if __name__=="__main__":
    montu=AjobTurtle()
    montu.speed(1)
    montu.color('blue')
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)

    jhontu=turtle.Turtle()
    jhontu.shape('turtle')
    jhontu.speed(9)
    jhontu.color('red')
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(45)
    jhontu.backward(100)
    jhontu.right(90)
    jhontu.forward(10)

    turtle.done()
