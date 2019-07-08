"BY Krishna"


import turtle

hbday=turtle.Turtle()
hbday.width(8)
hbday.color("red")
new=turtle.getscreen()
hbday.speed(4)

new.bgcolor("lightblue")

# Hidden Work(penup)
hbday.left(180)
hbday.penup()
hbday.forward(300)
hbday.right(90)
hbday.forward(100)
hbday.pendown()

# Printing H


#start to draw
hbday.forward(50)
hbday.right(90)
hbday.forward(50)
hbday.left(90)
hbday.forward(50)
hbday.left(90)

hbday.penup()
hbday.forward(50)
hbday.left(90)
hbday.pendown()
hbday.forward(50)
hbday.left(90)
hbday.forward(50)
hbday.right(90)
hbday.forward(50)


# printing A

hbday.penup()
hbday.left(90)
hbday.forward(15)
hbday.pendown()
hbday.left(70)
hbday.forward(110)
hbday.right(70)
hbday.right(70)
hbday.forward(110)
hbday.left(180)
hbday.forward(55)
hbday.left(70)
hbday.forward(38)
hbday.left(70)
hbday.penup()
hbday.forward(55)
hbday.left(110)

hbday.forward(100)

# printing P

hbday.left(90)
hbday.pendown()
hbday.forward(100)
hbday.right(90)
hbday.forward(50)
hbday.right(20)
hbday.forward(20)
hbday.right(70)
hbday.forward(40)
hbday.right(70)
hbday.forward(20)
hbday.right(20)
hbday.forward(50)
hbday.left(90)
hbday.forward(50)
hbday.left(90)
hbday.penup()
hbday.forward(100)


# printing P

hbday.left(90)
hbday.pendown()
hbday.forward(100)
hbday.right(90)
hbday.forward(50)
hbday.right(20)
hbday.forward(20)
hbday.right(70)
hbday.forward(40)
hbday.right(70)
hbday.forward(20)
hbday.right(20)
hbday.forward(50)
hbday.left(90)
hbday.forward(50)
hbday.left(90)
hbday.penup()
hbday.forward(100)

# printing Y

hbday.forward(20)
hbday.pendown()
hbday.left(90)
hbday.forward(50)
hbday.left(30)
hbday.forward(60)
hbday.backward(60)
hbday.right(60)
hbday.forward(60)
hbday.backward(60)
hbday.left(30)

# go to Home

hbday.penup()
hbday.home()

hbday.color("orange")
new.bgcolor("lightgreen")
# setting second row

hbday.backward(300)
hbday.right(90)
hbday.forward(60)
hbday.left(180)


# printing P


hbday.pendown()
hbday.forward(100)
hbday.right(90)
hbday.forward(50)
hbday.right(20)
hbday.forward(20)
hbday.right(70)
hbday.forward(40)
hbday.right(70)
hbday.forward(20)
hbday.right(20)
hbday.forward(50)
hbday.backward(50)
hbday.left(180)
hbday.right(20)
hbday.forward(20)
hbday.right(70)
hbday.forward(40)
hbday.right(70)
hbday.forward(20)
hbday.right(20)
hbday.forward(50)
hbday.right(90)
hbday.forward(10)


# go to Home

hbday.penup()
hbday.home()

# setting up

hbday.backward(200)
hbday.right(90)
hbday.forward(10)
hbday.left(90)
hbday.pendown()
hbday.forward(20)
hbday.penup()
hbday.home()

# D

hbday.backward(150)
hbday.right(90)
hbday.forward(60)
hbday.pendown()
hbday.backward(100)
hbday.right(90)
hbday.forward(10)
hbday.backward(70)
hbday.left(180)
hbday.right(20)
hbday.forward(20)
hbday.right(70)
hbday.forward(88)
hbday.right(70)
hbday.forward(20)
hbday.right(20)
hbday.forward(70)

hbday.penup()
hbday.home()

# set up for A

hbday.backward(50)
hbday.right(90)
hbday.forward(65)
hbday.left(90)



# printing A


hbday.pendown()
hbday.left(70)
hbday.forward(110)
hbday.right(70)
hbday.right(70)
hbday.forward(110)
hbday.left(180)
hbday.forward(55)
hbday.left(70)
hbday.forward(38)
hbday.left(70)
hbday.penup()
hbday.forward(55)
hbday.left(110)

hbday.forward(100)

# printing Y


# printing Y


hbday.pendown()
hbday.left(90)
hbday.forward(50)
hbday.left(30)
hbday.forward(60)
hbday.backward(60)
hbday.right(60)
hbday.forward(60)
hbday.backward(60)
hbday.left(30)

# go to Home 

hbday.penup()
hbday.home()


# settig pogition

hbday.right(90)
hbday.forward(215)
hbday.right(90)
hbday.forward(200)
hbday.right(90)

#color

hbday.color("green")
new.bgcolor("lightblue")

#printing name
# print whatever name you want
# design'''


#design pattern
hbday.home()
hbday.forward(200)
hbday.pendown()
hbday.color("hotpink")
hbday.width(3)
hbday.speed(0)

def squre(length, angle):
    
    hbday.forward(length)
    hbday.right(angle)
    hbday.forward(length)
    hbday.right(angle)
   
    hbday.forward(length)
    hbday.right(angle)
    hbday.forward(length)
    hbday.right(angle)

squre(80, 90)

for i in range(36):
      hbday.right(10)
      squre(80, 90)




turtle.mainloop()
