
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    idi = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(idi)


#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for L in range(START_LENGTH):
    x_pos=snake.pos()[0]    #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()


def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    remove_tail # remove last piece of tail's positio

    
snake.direction = "Up" #Go to the top of your file, and after the line that says snake.direction = “Up”,  write:

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
     
def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!
def down():
    snake.direction="Down" #Change direction to up
    print("You pressed the up key!")

def right():
    snake.direction="Right" #Change directio
    print("You pressed the up key!")

def left():
    snake.direction="Left" #Change direction to up
    print("You pressed the up key!")

turtle.onkeypress(up, "Up") # Create listener for up key
turtle.listen()

turtle.onkeypress(left, "Left")  
turtle.listen()                  
turtle.onkeypress(right, "Right")
turtle.listen()                  
turtle.onkeypress(down, "Down")
                         
turtle.listen()                  

#ADD THE LINES BELOW

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif")
snake.shape("trash.gif")
#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]


    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE

    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")
    

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved down!")

    elif snake.direction == "Right":
       snake.goto(x_pos + SQUARE_SIZE, y_pos)
       print("you moved right!")
       
    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
                   
    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()
    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()
    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]


    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    elif new_y_pos >= UP_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the left edge! Game over!")
         quit()
          #Add this line to the end of the move_snake function
    turtle.ontimer(move_snake,TIME_STEP) #<--- new line here
    
     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE


#Now, call the move_snake() function.  This starts moving the snake.  Once it starts 
#moving, it keeps moving by itself:
move_snake()

turtle.mainloop()
