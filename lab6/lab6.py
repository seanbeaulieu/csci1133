import turtle 

def diagonal_fives():    
    mat = []
    for i in range(4):
        ls = [0,0,0,0]
        mat.append(ls)    
        mat[i][i] = 5
    print(mat)


def shortest_dist(ls):
    list1 = []
    x = 100000000
    y = 0
    for i in range(len(ls)):
        for j in range(len(ls) -1):
            if i != j:
                y = dist(ls[i], ls[j])
                if y < x:
                    x = y   
    return(x)
        
def dist(p1, p2):
    distance = (((p2[0]-p1[0])**2) + ((p2[1] - p1[1])**2))**(1/2)
    return distance 


def draw_grid(grid):
    t = turtle.Turtle()
    turtle.setworldcoordinates(-1, -1, 10, 10)
    t.speed(0)
    t.hideturtle()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[j][i] == 0:
                
                t.setpos(i + 0.5,j + 0.5)
                t.pendown()
                t.color("black")
                t.begin_fill()
                t.right(90)
                t.forward(1)
                t.right(90)
                t.forward(1)
                t.right(90)
                t.forward(1)
                t.right(90)
                t.forward(1)
                t.end_fill()
                t.penup()

def move_up():
    turtle.setheading(90)
    turtle.forward(1)

def move_down():
    turtle.setheading(270)
    turtle.forward(1)
def move_right():
    turtle.setheading(0)
    turtle.forward(1)
def move_left():
    turtle.setheading(180)
    turtle.forward(1)

def turtle_maze():
    turtle.delay(0)
    grid1 = [[0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,1,1,1,1,0],
            [0,1,0,1,1,1,0,0,1,0],
            [0,1,1,1,0,1,0,0,1,0],
            [0,1,0,1,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,1,1,0],
            [0,0,1,0,0,1,1,1,0,0],
            [0,0,1,1,1,0,0,1,0,0],
            [0,0,1,0,1,0,1,1,1,0],
           [0,0,0,0,0,0,0,0,0,0]]
    draw_grid(grid1)

    turtle.color("blue")
    turtle.pu()
    turtle.setpos(1,1)
    turtle.pd()
    turtle.speed(0)
    turtle.onkeypress(move_up, "Up")
    turtle.onkeypress(move_down, "Down")
    turtle.onkeypress(move_right, "Right")
    turtle.onkeypress(move_left, "Left")

    turtle.listen()
    turtle.mainloop()

    
    
