from turtle import *
import math
import decimal

trt = Turtle()
trt.screen.setup(800, 800)


def coordinates():
    trt.hideturtle()
    trt.speed("fast")
    trt.up()
    trt.goto(-400, 0)
    trt.down()
    trt.fd(800)
    trt.up()
    trt.goto(0, 400)
    trt.down()
    trt.left(270)
    trt.fd(800)
    trt.up()
    trt.goto(0, 300)
    trt.down()
    trt.speed("normal")
    trt.showturtle()




K = 1
R = float(input("Введите радиус шара(в метрах):\n")) # радиус шара.
V = 4 / 3 * 3.14 * R * R *R
s = 15 # коэффициент сопротивления.
g = 9.81  # ускорение свободного падения.
Pm_temp = str(input("""Выберите один из указанных материалов:
    1.Железо
    2.Аллюминий
    3.Дерево(сосна)\n
    """))


def material(Pm_temp):
    global Pm
    if Pm_temp == "1":
        Pm = 7800
    elif Pm_temp == "2":
        Pm = 2700
    elif Pm_temp == "3":
        Pm = 400
    else:
        Pm_temp1 = str(input("Ошибка. Введите корректное значение( 1 2 или 3)\n"))
        material(Pm_temp1)
material(Pm_temp)
v0 = int(input("Введите начальную скорость (м/c)"))  # начальная скорость броска.
while v0 < 0:
    v0 = int(input("Начальная скорость не может быть отрицательной\nВведите начальную скорость (м/c)"))

angle = int(input("Введите угол под которым совершается бросок(градусы)\n")) # угол броска.
while angle > 0 & angle < -90:
    angle = int(input("Введите угол под которым совершается бросок(градусы)(От -90 до 0)\n"))
m = float(V*Pm)  # масса шара.
print(m,'кг')
G = 9.81

alfa = math.radians(angle)  # угол подбрасывания (в радианах).
dt = 0.01
hmax = 300  # вводим переменные для определения координат.
xmax = 0
v = v0      # начальная скорость.
t = 0       # начальное время.
y = 300       # начальная ордината шара.
h = 300      # начальная высота
x = 0       # // начальная абсцисса шара.
# раскладываем вектор скорости на проекции на оси.
vx = v * math.cos(alfa)
vy = v * math.sin(alfa)
xk = 0
coordinates()
trt.speed(10)

while (y >= 0):
    yk = 590 - K * y
    xk = 100 + x
    Fcx = - s * R * vx
    Fcy = - s * R * vy
    ay = Fcy / m - g
    ax = Fcx / m
    y = y + vy * dt + ay * G*dt * dt / 2
    h = y
    vy = vy + ay * dt
    x = x + vx * dt + ax * dt * dt / 2
    vx = vx + ax * dt
    v = math.sqrt(vx * vx + vy * vy)
    t = t + dt

    # if (h > hmax):
    #      hmax = h
    if (x > xmax):
        xmax = x

    trt.goto(x, y)

print("Time: ",t)
# print("Max height: ",hmax)
print("Lenght: ",xmax)
trt.screen.exitonclick()
trt.screen.mainloop()