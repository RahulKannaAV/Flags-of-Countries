from turtle import Turtle, Screen

sc = Screen()
sc.title('Bahrain Flag')

def bahrain():
    pen = Turtle()
    pen.penup()
    pen.goto(-200,0)
    pen.setheading(90)
    pen.pendown()
    pen.goto(-200,200)
    pen.setheading(360)
    pen.goto(200,200)
    pen.setheading(270)
    pen.goto(200,0)
    pen.setheading(180)
    pen.goto(-200, 0)
    pen.penup()
    pen.goto(-85, 0)
    pen.setheading(135)
    pen.pendown()
    pen.color('red')
    pen.goto(pen.xcor() + 40, pen.ycor() + 20)
    pen.begin_fill()
    pen.fillcolor('red')
    for i in range(4):
        pen.goto(pen.xcor()-40, pen.ycor()+20)
        pen.setheading(45)
        pen.goto(pen.xcor() + 40, pen.ycor() + 20)
    pen.goto(pen.xcor() - 40, pen.ycor() + 20)
    pen.setheading(0)
    pen.goto(pen.xcor()+40, pen.ycor())
    pen.setheading(360)
    pen.goto(200,200)
    pen.setheading(270)
    pen.goto(200, 0)
    pen.setheading(180)
    pen.goto(-85,0)
    pen.end_fill()


bahrain()


sc.exitonclick()
