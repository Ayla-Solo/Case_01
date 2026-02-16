import turtle as t

# -------------------------- Общие настройки экрана --------------------------
screen = t.Screen()
screen.setup(width=1400, height=900)
t.speed(-10)  # Максимальная скорость
t.hideturtle()


# -------------------------- 1. Ракета --------------------------
def rocket_triangle(a, b):
    t.forward(a)
    t.left(135)
    t.forward(b)
    t.left(90)
    t.forward(b)
    t.left(135)


def rocket_parallelogram(a, b):
    for i in range(2):
        t.forward(a)
        t.left(45)
        t.forward(b)
        t.left(135)


def rocket_square(a):
    for i in range(4):
        t.forward(a)
        t.right(90)


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
    rocket_triangle(141.5, 100)
    t.end_fill()

    # Желтый треугольник
    t.left(45)
    t.forward(100)
    t.right(45)
    t.color('yellow')
    t.forward(141.5)
    t.left(180)
    t.begin_fill()
    rocket_triangle(141.5, 100)
    t.end_fill()

    # Синий треугольник
    t.left(45)
    t.color('blue')
    t.begin_fill()
    rocket_triangle(100, 70.7)
    t.end_fill()

    # Розовый треугольник
    t.left(45)
    t.color('pink')
    t.begin_fill()
    rocket_triangle(70.7, 50)
    t.end_fill()

    # Оранжевый квадрат
    t.right(90)
    t.penup()
    t.forward(141.5)
    t.pendown()
    t.left(45)
    t.color('orange')
    t.begin_fill()
    rocket_square(50)
    t.end_fill()

    # Фиолетовый треугольник
    t.right(90)
    t.forward(50)
    t.left(45)
    t.color('purple')
    t.begin_fill()
    rocket_triangle(70.7, 50)
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
    rocket_parallelogram(70, 60)
    t.end_fill()


# -------------------------- 2. Медведь --------------------------
def draw_bear():
    t.penup()
    t.goto(200, 100)
    t.pendown()
    t.setheading(0)
    t.color("black")

    # Голова
    t.begin_fill()
    t.color('brown')
    t.circle(80)
    t.end_fill()

    t.begin_fill()
    t.color('salmon3')
    t.circle(40)
    t.end_fill()

    t.up()
    t.circle(40, 180)

    t.begin_fill()
    t.color('salmon')
    t.circle(20)
    t.end_fill()

    t.up()
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(50)
    t.down()
    t.color('black')
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.up()
    t.left(180)
    t.forward(100)
    t.down()
    t.color('black')
    t.begin_fill()
    t.circle(-5)
    t.end_fill()

    # Уши
    t.up()
    t.home()
    t.goto(200, 100)
    t.circle(80, 135)
    t.down()
    t.begin_fill()
    t.color('brown')
    t.circle(-38)
    t.end_fill()
    t.begin_fill()
    t.color('salmon3')
    t.circle(-28)
    t.end_fill()

    t.up()
    t.goto(200, 100)
    t.circle(80, -135)
    t.down()
    t.begin_fill()
    t.color('brown')
    t.circle(-38)
    t.end_fill()
    t.begin_fill()
    t.color('salmon3')
    t.circle(-28)
    t.end_fill()

    # Тело
    t.up()
    t.goto(200, 100)
    t.down()
    t.begin_fill()
    t.color('brown')
    t.circle(-100)
    t.end_fill()
    t.begin_fill()
    t.color('salmon3')
    t.circle(-85)
    t.end_fill()

    # Конечности
    t.up()
    t.goto(200, 100)
    t.circle(-100, 65)
    t.down()
    t.begin_fill()
    t.color('brown')
    t.forward(33)
    t.left(90)
    for i in range(3):
        t.forward(66)
        t.left(90)
    t.forward(33)
    t.end_fill()

    t.up()
    t.goto(200, 100)
    t.circle(-100, 70)
    t.down()
    t.begin_fill()
    t.color('brown')
    t.forward(33)
    t.left(90)
    for i in range(3):
        t.forward(66)
        t.left(90)
    t.forward(33)
    t.end_fill()

    t.up()
    t.goto(200, 100)
    t.circle(-100, 65)
    t.down()
    t.begin_fill()
    t.color('brown')
    t.forward(33)
    t.left(90)
    for i in range(3):
        t.forward(66)
        t.left(90)
    t.forward(33)
    t.end_fill()

    t.up()
    t.goto(200, 100)
    t.circle(-100, )
    t.down()
    t.begin_fill()
    t.color('brown')
    t.forward(33)
    t.left(90)
    for i in range(3):
        t.forward(66)
        t.left(90)
    t.forward(33)
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
    t.goto(-600, -200)
    t.left(60)
    t.circle(10, 120)

    t.begin_fill()
    t.circle(-9, 540)
    t.end_fill()

    # Щупальца
    t.pencolor('black')
    t.seth(90)
    t.circle(60, 50)
    t.circle(10, 180)
    t.circle(5, 160)
    t.up()
    t.setposition(-608.66, -167)
    t.down()
    t.seth(80)
    t.circle(-60, 55)
    t.circle(-10, 180)
    t.circle(-5, 160)


# -------------------------- 4. Геометрическая фигура --------------------------
def squareTurtle(root, step, angle, colorPen=None, colorFill=None, rotate="left"):
    if colorPen != None:
        root.pencolor(colorPen)

    if colorFill != None:
        root.color(colorPen, colorFill)

    root.begin_fill()

    for _ in range(0, 4):
        root.forward(step)
        if rotate == "left":
            root.left(angle)
        else:
            root.right(angle)
    root.end_fill()
    root.pencolor(colorPen)


def draw_geo_shape():
    t.penup()
    t.goto(200, -200)
    t.pendown()
    t.setheading(0)
    t.color("black")

    root = t
    root.shape("turtle")
    root.pensize(3)

    root.penup()
    root.goto(200 - 200, -200 + 200)
    root.pendown()

    root.color("green", "green")
    root.begin_fill()
    for _ in range(0, 2):
        root.left(135)
        root.forward(100)
        root.left(45)
        root.forward(70)
    root.end_fill()

    root.penup()
    root.goto(200 - 235, -200 + 195)
    root.pendown()
    # Квадрат
    squareTurtle(root, 70, 90, "orange", "orange", "right")

    root.penup()
    root.goto(200 - 235, -200 + 195)
    root.pendown()
    # Параллелограмм
    root.color("black", "black")
    root.begin_fill()
    for _ in range(0, 2):
        root.left(135)
        root.forward(100)
        root.left(45)
        root.forward(70)
    root.end_fill()

    root.penup()
    root.goto(200 - 240, -200 + 160)
    root.pendown()
    # Треугольник
    root.color("red", "red")
    root.begin_fill()
    root.right(90)
    root.forward(130)
    root.right(90)
    root.forward(130)
    root.end_fill()

    root.penup()
    root.goto(200 - 370, -200 + 25)
    root.pendown()
    # Треугольник
    root.color("yellow", "yellow")
    root.begin_fill()
    root.left(90)
    root.forward(130)
    root.left(135)
    root.forward(185)
    root.end_fill()

    root.left(45)
    root.penup()
    root.goto(200 - 235, -200 - 10)
    root.pendown()

    # Треугольник
    root.color('purple', 'purple')
    root.begin_fill()
    root.forward(70)
    root.right(135)
    root.forward(50)
    root.end_fill()

    root.left(45)
    root.penup()
    root.goto(200 - 370, -200 - 110)
    root.pendown()
    # Треугольник
    root.color("blue", "blue")
    root.begin_fill()
    root.forward(90)
    root.left(90)
    root.forward(90)
    root.end_fill()

    root.left(45)
    root.penup()
    root.goto(200 - 275, -200 - 50)
    root.pendown()
    # Треугольник
    root.color("pink", "pink")
    root.begin_fill()
    root.left(135)
    root.forward(60)
    root.left(90)
    root.forward(60)
    root.end_fill()


# -------------------------- 5. Робогирль и корабль --------------------------
def robot_rectangle(a, b):
    t.fillcolor('red')
    t.begin_fill()
    t.up()
    t.left(135)
    t.down()
    t.left(45)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.end_fill()


def robot_rectangle1(a, b):
    t.fillcolor('pink')
    t.begin_fill()
    t.up()
    t.left(180)
    t.down()
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.end_fill()


def robot_rectangle2(a, b, c):
    t.fillcolor('red')
    t.begin_fill()
    t.up()
    t.right(180)
    t.forward(c)
    t.left(90)
    t.down()
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.end_fill()


def robot_rectangle3(a, b, c):
    t.fillcolor('pink')
    t.begin_fill()
    t.up()
    t.forward(c)
    t.left(90)
    t.down()
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.end_fill()


def robot_trapezoid(x, y, a, b, c):
    t.fillcolor('blue')
    t.begin_fill()
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(70)
    t.forward(c)
    t.right(110)
    t.forward(b)
    t.right(110)
    t.forward(c)
    t.end_fill()


def robot_trapezoid1(x, y, a, b, c):
    t.fillcolor('green')
    t.begin_fill()
    t.up()
    t.setposition(x, y)
    t.down()
    t.right(71)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(c)
    t.setposition(x, y)
    t.end_fill()


def robot_trapezoid2(x, y, a, b, c):
    t.fillcolor('green')
    t.begin_fill()
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
    t.forward(c)
    t.setposition(x, y)
    t.end_fill()


def ship_triangle(a, b):
    t.up()
    t.forward(200)
    t.left(90)
    t.forward(170)
    t.left(180)
    t.fillcolor('red')
    t.begin_fill()
    t.down()
    t.forward(a)
    t.left(120)
    t.forward(b)
    t.left(120)
    t.forward(b)
    t.left(30)
    t.end_fill()


def ship_triangle1(a, b):
    t.fillcolor('red')
    t.begin_fill()
    t.up()
    t.forward(10)
    t.left(90)
    t.down()
    t.forward(a)
    t.right(120)
    t.forward(b)
    t.right(120)
    t.forward(b)
    t.right(30)
    t.end_fill()


def ship_machta(a, b):
    t.fillcolor('black')
    t.begin_fill()
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.end_fill()


def ship_deck1(a, b):
    t.fillcolor('blue')
    t.begin_fill()
    t.up()
    t.right(180)
    t.forward(90)
    t.down()
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.end_fill()


def ship_deck2(a, b):
    t.fillcolor('blue')
    t.begin_fill()
    t.up()
    t.forward(10)
    t.down()
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.end_fill()


def ship_body(a, b, c, d):
    t.fillcolor('brown')
    t.begin_fill()
    t.up()
    t.right(180)
    t.forward(30)
    t.left(90)
    t.down()
    t.forward(a)
    t.right(150)
    t.forward(b)
    t.right(30)
    t.forward(c)
    t.right(30)
    t.forward(b)
    t.right(150)
    t.forward(d)
    t.end_fill()


def ship_triangle2(a, b):
    t.up()
    t.left(90)
    t.forward(70)
    t.left(180)
    t.fillcolor('red')
    t.begin_fill()
    t.down()
    t.forward(a)
    t.left(120)
    t.forward(b)
    t.left(120)
    t.forward(b)
    t.left(30)
    t.end_fill()
    t.left(90)


def draw_robot_ship():
    t.penup()
    t.goto(300, -200)
    t.pendown()
    t.setposition(300, -200)
    t.setheading(0)
    t.color("black")

    robot_rectangle(10, 40)
    robot_rectangle1(100, 60)
    robot_rectangle2(10, 40, 100)
    robot_rectangle3(20, 10, 35)
    robot_trapezoid(325, -200 - 10, 60, 128, 100)
    robot_trapezoid1(330 , -200 - 104, 20, 50, 40)
    robot_trapezoid2(390, -200 - 104, 20, 50, 40)

    ship_triangle(50, 50)
    ship_triangle1(50, 50)
    ship_machta(10, 120)
    ship_deck1(30, 40)
    ship_deck2(40, 30)
    ship_body(60, 40, 80, 89.7)
    ship_triangle2(25, 25)


# -------------------------- Запуск всех рисунков --------------------------
draw_rocket()
draw_bear()
draw_fly()
draw_geo_shape()
draw_robot_ship()

screen.exitonclick()
