import turtle as t

w = t.Screen()
t.speed(0)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def square(a):
    for _ in range(4):
        t.forward(a)
        t.right(90)

def rectangle(a, b):
    for _ in range(2):
        t.forward(a)
        t.right(90)
        t.forward(b)
        t.right(90)

def triangle(a):
    for _ in range(3):
        t.forward(a)
        t.left(120)

def rhombus(a):
    for _ in range(2):
        t.forward(a)
        t.left(60)
        t.forward(a)
        t.left(120)

def parallelogram(a, b):
    for i in range(2):
        t.forward(a)
        t.left(45)
        t.forward(b)
        t.left(135)

def right_triangle(a, b):
    t.forward(a)
    t.left(135)
    t.forward(b)
    t.left(90)
    t.forward(b)
    t.left(135)

# Функция для рисования круга
def circle(radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# синий квадрат
move_to(100, 0)
t.color("blue")
t.begin_fill()
square(100)
t.end_fill()

# жёлтый круг
move_to(150, -150)
t.color("yellow")
t.begin_fill()
t.circle(25)
t.end_fill()

# жёлтый прямоугольник
move_to(125, 25)
t.color("yellow")
t.begin_fill()
rectangle(50, 25)
t.end_fill()

# красный треугольник
move_to(125, 25)
t.color("red")
t.begin_fill()
triangle(50)
t.end_fill()

# большой жёлтый прямоугольник
move_to(200, 50)
t.color("yellow")
t.begin_fill()
rectangle(75, 150)
t.end_fill()

# зелёный треугольник
move_to(225, 50)
t.color("green")
t.begin_fill()
triangle(25)
t.end_fill()

# зелёный круг
move_to(238, -140)
t.color("green")
t.begin_fill()
t.circle(35)
t.end_fill()

# синий квадрат
move_to(220, 20)
t.color("blue")
t.begin_fill()
square(40)
t.end_fill()

# красный квадрат
move_to(275, 0)
t.color("red")
t.begin_fill()
square(100)
t.end_fill()

# зелёный прямоугольник
move_to(320, 100)
t.color("green")
t.begin_fill()
rectangle(40, 100)
t.end_fill()

# синий круг
move_to(325, -140)
t.color("blue")
t.begin_fill()
t.circle(48)
t.end_fill()

# жёлтые круги
move_to(300, 100)
t.color("yellow")
t.begin_fill()
t.circle(25)
t.end_fill()

move_to(250, 135)
t.begin_fill()
t.circle(30)
t.end_fill()

move_to(170, 150)
t.begin_fill()
t.circle(40)
t.end_fill()

# красный прямоугольник
move_to(0, -25)
t.color("red")
t.begin_fill()
rectangle(100, 20)
t.end_fill()

# зелёный квадрат
move_to(0, -20)
t.right(90)
t.color('green')
t.begin_fill()
square(80)
t.end_fill()

# красный треугольник
move_to(0, -20)
t.right(150)
t.color('red')
t.begin_fill()
triangle(70)
t.end_fill()

# синий треугольник
move_to(-70, -20)
t.right(60)
t.color('blue')
t.begin_fill()
triangle(70)
t.end_fill()

# жёлтый треугольник
move_to(-95, 42)
t.right(60)
t.color('yellow')
t.begin_fill()
triangle(70)
t.end_fill()

# синий круг
move_to(-40, -100)
t.right(180)
t.color('blue')
t.begin_fill()
t.circle(30)
t.end_fill()

# жёлтый квадрат
move_to(-100, 0)
t.left(90)
t.color('yellow')
t.begin_fill()
square(100)
t.end_fill()

# синий ромб
move_to(-200, 0)
t.left(90)
t.color('blue')
t.begin_fill()
rhombus(60)
t.end_fill()

# зелёный круг
move_to(-150, -100)
t.right(180)
t.color('green')
t.begin_fill()
t.circle(30)
t.end_fill()

# синий квадрат
move_to(-210, -20)
t.left(90)
t.color('blue')
t.begin_fill()
square(80)
t.end_fill()

# зелёный треугольник
move_to(-215, -20)
t.right(150)
t.color('green')
t.begin_fill()
triangle(70)
t.end_fill()

# жёлтый круг
move_to(-250, -100)
t.left(45)
t.color('yellow')
t.begin_fill()
t.circle(30)
t.end_fill()

# -------------------------- 1. Ракета --------------------------



def draw_rocket():
    t.penup()
    t.goto(-500, 100)
    t.pendown()
    t.setheading(0)
    t.color("black")

    # Красный треугольник
    t.color('red')
    t.right(45)
    t.forward(100)
    t.left(135)
    t.begin_fill()
    right_triangle(141.5, 100)
    t.end_fill()

    # Желтый треугольник
    t.left(45)
    t.forward(100)
    t.right(45)
    t.color('yellow')
    t.forward(141.5)
    t.left(180)
    t.begin_fill()
    right_triangle(141.5, 100)
    t.end_fill()

    # Синий треугольник
    t.left(45)
    t.color('blue')
    t.begin_fill()
    right_triangle(100, 70.7)
    t.end_fill()

    # Розовый треугольник
    t.left(45)
    t.color('pink')
    t.begin_fill()
    right_triangle(70.7, 50)
    t.end_fill()

    # Оранжевый квадрат
    t.right(90)
    t.penup()
    t.forward(141.5)
    t.pendown()
    t.left(45)
    t.color('orange')
    t.begin_fill()
    square(50)
    t.end_fill()

    # Фиолетовый треугольник
    t.right(90)
    t.forward(50)
    t.left(45)
    t.color('purple')
    t.begin_fill()
    right_triangle(70.7, 50)
    t.end_fill()

    # Зеленый параллелограмм
    t.left(135)
    t.penup()
    t.forward(150)
    t.right(135)
    t.forward(71.5)
    t.pendown()
    t.color('green')
    t.begin_fill()
    parallelogram(70, 60)
    t.end_fill()

# -------------------------- 3. Муха --------------------------
def draw_fly():
    t.penup()
    t.goto(-600, -200)
    t.pendown()
    t.setheading(0)
    t.color("black")

    # Крылья
    t.begin_fill()
    t.color('pink')
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

    t.left(60)
    t.begin_fill()
    t.color('brown')
    t.circle(10)
    t.end_fill()

    t.circle(10, 250)
    t.begin_fill()
    t.color('pink')
    for i in range(3):
        t.backward(100)
        t.left(120)

    t.left(70)
    for i in range(3):
        t.backward(70)
        t.left(120)
    t.end_fill()

    t.up()
    t.setposition(-600, -200)
    t.down()
    t.right(90)
    t.begin_fill()
    for i in range(3):
        t.forward(70)
        t.left(120)
    t.end_fill()

    # Тело
    t.color('brown')
    t.right(110)
    t.forward(7)
    t.begin_fill()
    t.circle(10, 540)
    t.end_fill()
    t.begin_fill()
    t.circle(-8, 540)
    t.end_fill()
    t.begin_fill()
    t.circle(6, 540)
    t.end_fill()
    t.begin_fill()
    t.circle(-3, 540)
    t.end_fill()
    t.up()
    t.goto(-600, -200)
    t.left(60)
    t.circle(10, 120)
    t.goto(-608.66, -167)
    t.down()
    t.begin_fill()
    t.circle(-10, 540)
    t.end_fill()
    t.up()

draw_fly()
draw_rocket()
w.mainloop()