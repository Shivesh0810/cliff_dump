import turtle as t


window = t.Screen()
window.title("game.py")
window.bgcolor("red")
window.setup(width=800, height=600)
window.tracer()

# creating text

text = t.Turtle()
text.hideturtle() 
text.penup()  
text.goto(0, 260)  
text.write("HEIL HITLER", align="center", font=("Courier", 26, "bold"))


# creating circle
cir = t.Turtle()
cir.speed(0)
cir.shape("circle")
cir.color("white")
cir.goto(20,25)
cir.penup()
cir.shapesize(stretch_wid=10, stretch_len=10)



# creating 1st
a = t.Turtle()
a.speed(0)
a.shape("square")
a.color("black")
a.goto(0,50)
a.penup()
a.shapesize(stretch_wid=4, stretch_len=1)
a.setheading(40)

# creating 1st tail
b = t.Turtle()
b.speed(0)
b.shape("square")
b.color("black")
b.goto(5,95)
b.penup()
b.shapesize(stretch_wid=3, stretch_len=1)
b.setheading(-48)

# creating 2nd
c = t.Turtle()
c.speed(0)
c.shape("square")
c.color("black")
c.goto(0,4)
c.penup()
c.shapesize(stretch_wid=4, stretch_len=1)
c.setheading(-50)

# creating 2nd tail
d = t.Turtle()
d.speed(0)
d.shape("square")
d.color("black")
d.goto(-38,0)
d.penup()
d.shapesize(stretch_wid=3, stretch_len=1)
d.setheading(40)

#creating 3rd
e = t.Turtle()
e.speed(0)
e.shape("square")
e.color("black")
e.goto(45,0)
e.penup()
e.shapesize(stretch_wid=4, stretch_len=1)
e.setheading(42)

# creating 3rd tail
f = t.Turtle()
f.speed(0)
f.shape("square")
f.color("black")
f.goto(48,-35)
f.penup()
f.shapesize(stretch_wid=3, stretch_len=1)
f.setheading(130)

# creating 4th
g = t.Turtle()
g.speed(0)
g.shape("square")
g.color("black")
g.goto(50,46)
g.penup()
g.shapesize(stretch_wid=4, stretch_len=1)
g.setheading(130)

# creating 4th tail
h = t.Turtle()
h.speed(0)
h.shape("square")
h.color("black")
h.goto(85,50)
h.penup()
h.shapesize(stretch_wid=3, stretch_len=1)
h.setheading(40)

window.mainloop()