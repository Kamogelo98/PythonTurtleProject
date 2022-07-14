import turtle as t

t.pen(pencolor = "hotpink" , fillcolor = "pink" , pensize = 5 , speed = 1)
t.bgcolor("pink")

t.penup()
t.bk(400)
t.pendown()
#K
t.rt(90)
t.fd(100)
t.bk(50)
t.lt(90 + 45)
t.fd(70)
t.bk(70)
t.rt(90)
t.fd(70)

t.penup()
t.lt(45)
t.fd(10)
t.pendown()

#A
t.lt(65)
t.fd(100)
t.rt(130)
t.fd(100)
t.bk(50)
t.lt(65)
t.bk(45)

t.penup()
t.fd(80)
t.pendown()

#M
t.rt(90)
t.fd(50)
t.bk(100)
t.lt(45)
t.fd(70)
t.lt(90)
t.fd(70)
t.rt(90 + 45)
t.fd(100)

t.lt(90)
t.penup()
t.fd(10)
t.fd(50)
t.pendown()

#O
t.circle(50)
t.penup()
t.fd(130)
t.pendown()

#G
t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.forward(10)
t.pendown()
t.circle(50,250)
t.left(20 + 90)
t.forward(30)
t.bk(50)

t.penup()
t.bk(30)
t.rt(90)
t.bk(30)
t.pendown()

#E
# t.rt(90)
t.fd(100)
t.rt(90)
t.fd(50)
t.bk(50)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(50)
t.bk(50)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(50)

t.penup()
t.fd(30)
t.pendown()

#L
t.fd(50)
t.bk(50)
t.lt(90)
t.fd(100)

t.rt(90)
t.penup()
t.fd(80)
t.rt(90)
t.fd(50)
t.pendown()

#O
t.circle(50)

t.done()