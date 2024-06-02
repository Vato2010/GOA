from turtle import *
#draw a square
speed(5)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#draw a door
penup() 
goto(75, 0)
pendown()
color("yellow")
begin_fill()
left(180)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
#draw a window  
penup()
goto(50, 150)
pendown()
color("green")
begin_fill()
forward(40)
right(90)
forward(40)

right(90)
forward(40)
right(90)
forward(40)
end_fill()
#draw a roof
penup()
goto(200, 200)
pendown()
color("brown")
begin_fill()
left(135)
forward(150)
left(93)
forward(150)
end_fill()




exitonclick()