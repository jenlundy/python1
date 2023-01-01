import turtle

def main():
    print("Face Lab by Jennifer Lundy")
    perform_turtle_boxtrot()
    turtle.speed(0)
    

    
def draw_square(turtle,size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
def draw_triangle(turtle,size):
    for i in range(8):
        turtle.forward(50)
        turtle.right(-120)
    
def draw_rectangle(turtle,width,height):
    for i in range(2):
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        
def perform_turtle_boxtrot():
    window = turtle.Screen()
    alex = turtle.Turtle()
    alex.up()
    alex.goto(-300,300)
    alex.down()

    draw_square(alex,300)
    alex.up()
    alex.goto(0,300)
    alex.down()
    draw_square(alex,300)
    
    #mycode
    #thisis mouth
    alex.up()
    alex.goto(-150,-90)
    alex.down()
    draw_rectangle(alex,0,0)

    

    #newtriangl nose
    alex.up()
    alex.goto(-15,-15)
    alex.down()
    draw_triangle(alex,100)

    #lefttrianglereal eye
    alex.up()
    alex.goto(-100,150)
    alex.down()
    draw_triangle(alex,-10)
    #righteyetriang
    alex.up()
    alex.goto(100,100)
    alex.down()
    draw_triangle(alex,-10)
    
    
    #l lefteyesquare
    alex.up()
    alex.goto(-100,100)
    alex.down()
    draw_square(alex,-50)
    #right nd eye square
    alex.up()
    alex.goto(100,100)
    alex.down()
    draw_square(alex,-50)

    #squareFACE
    alex.up()
    alex.goto(-200,200)
    alex.down()
    draw_square(alex,400)

    
    

   
                           
    #fangsnew
    #fangleft then fangright

    alex.up()
    alex.goto(-150,-150)
    alex.down()
    draw_triangle(alex,0)

    alex.up()
    alex.goto(150,-100)
    alex.down()
    draw_triangle(alex,0)
    
    #upside down triangle

    
    
    #stops working here
    
    #done does not work
    #trying triangle
    alex.down()
    
    
    
   
   



    #all code goes before this line    
main()
