import time 
from turtle import *
color('green')
bgcolor('black')
speed(100)
hideturtle()
b=0
while b <200:
    right(b)
    forward(b * 1)
    b = b + 1
time.sleep(5)
