import turtle as t

t.left(90)
k =20
t.speed(10**8)

t.right(315)
for i in range(7):
    t.forward(16*k)
    t.right(45)
    t.forward(8*k)
    t.right(135)

t.up()
for x in range(-15,3):
    for y in range(20):
        t.goto(x*k,y*k)
        t.dot(3,'red')

t.done()