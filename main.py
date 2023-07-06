import turtle
import time
import random

s = turtle.getscreen()
s.clear()


# drawing the grid
grid = []

for y in range (0,10):
    new = []
    for x in range (0, 10):
        new.append (turtle.Turtle())
        new[x].shape("square")
        new[x].shapesize(1.5, 1.5)
        new[x].speed(500)
        new[x].penup()
        new[x].setx(-200 + x * 40)
        new[x].sety(-200 + y * 40)
    grid.append (new)

def make_cell():
    cell = turtle.Turtle()
    cell.shape("square")
    cell.shapesize(1.5, 1.5)
    cell.penup()
    cell.speed('fastest')
    cell.hideturtle()
    cell.color("blue")
    return cell

def make_apple(cell, head):
    apple = turtle.Turtle()
    apple.shape("square")
    apple.shapesize(1.5, 1.5)
    apple.penup()
    apple.speed('fastest')
    apple.hideturtle()
    apple.color("red")

    pos = (random.randint(-5,4) * 40, random.randint(-5,4) * 40)

    # this doesnt quite work yet! sometimes apples still spawns inside of body
    for item in cell:
        if fix_tuple(item.pos()) == pos or fix_tuple(head.pos()) == pos:
            pos = (random.randint(-5,4) * 40, random.randint(-5,4) * 40)       
    
    apple.setx(pos[0])
    apple.sety(pos[1])
    apple.showturtle()
    return apple

def fix_tuple(tuple):
    fix = list(tuple)
    fix[0] = int(fix[0])
    fix[1] = int(fix[1])
    
    return fix


# setup
head = turtle.Turtle()
head.setx(0)
head.sety(0)
head.shape("square")
head.color("green")
head.shapesize(1.5, 1.5)
head.penup()
head.speed(0.1)

cell = []
maxcell = 4
death = False

#drawing first body cells
for i in range(0,3):
    cell.append(make_cell())
    cell[i].setx(-40 - 40 * i)
    cell[i].sety(0)
    cell[i].showturtle()

apple = make_apple(cell, head)

# controls
def go_left():
    head.lt(90)

def go_right():
    head.rt(90)

s.listen()
s.onkeypress(go_left, "a")
s.onkeypress(go_right, "d")



# Main gameplay loop

while True:
    time.sleep(0.5)
    headpos = fix_tuple(head.pos())

    #make new cell directly behind head
    cell.insert(0, make_cell())
    cell[0].setx(headpos[0])
    cell[0].sety(headpos[1])
    cell[0].showturtle()

    #delete last cell (if player didn't just eat apple)
    if len(cell) > maxcell:
        cell[-1].hideturtle()
        cell.pop()
    
    #head moves forward
    head.fd(40)

    #check if apple has been eaten, makes new apple if it has
    if fix_tuple(head.pos()) == fix_tuple(apple.pos()):
        print('apple')
        maxcell += 1
        apple.hideturtle()
        apple = make_apple(cell, head)
    
    # checks if head is going outside grid, puts it on other side if it is
    headpos = fix_tuple(head.pos())
    if headpos[0] > 160:
        head.setx(-200)
        print(f'{headpos}, going left')

    elif headpos[0] < -200:
        head.setx(160)
        print(f'{headpos}, going right')

    elif headpos[1] > 160:
        head.sety(-200)
        print(f'{headpos}, going down')

    elif headpos[1] < -200:
        head.sety(160)
        print(f'{headpos}, going up')

    # checks if head is in body, ends game if it is
    for item in cell:
        cellpos = fix_tuple(item.pos())
        print(cellpos, headpos)
        if cellpos == headpos:
            print('DEATH')
            death = True
    
    if death:
        break


print(f'Your score is {maxcell}')



turtle.done()