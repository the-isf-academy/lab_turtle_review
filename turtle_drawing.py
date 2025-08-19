from turtle import *


# define function with size parameter
#   - how can you incorporate a for loop? 
#   - how can you incorporate a color parameter? 
def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)

square(100) # calls function

input() # keeps window open