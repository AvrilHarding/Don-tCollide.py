#!/bin/python3

from p5 import *
from random import randint, seed

# Include global variables here
level = 1
score = 0


def setup():
  size(400, 400)
  text_size(40)
  text_align(CENTER, TOP)

def draw():
# Put code to run every frame here
  global level
  if level > 0:
    safe = color(25, 27, 84)
    background(safe)
    drawObstacles()
    drawPlayer()
    text("Score: " + str(score), TOP, LEFT)
  
def drawPlayer():
  safe = color(25, 27, 84)
  player_y = int(height * 0.8)
  global score
  global level
  
  no_fill()
  no_stroke()
  ellipse(mouse_x, player_y, 10, 10)
  ellipse(mouse_x, player_y + 40, 10, 10)
  ellipse(mouse_x - 12, player_y + 20, 10, 10)
  ellipse(mouse_x + 12, player_y + 20, 10, 10)
  
  collide = get(mouse_x, player_y)
  collide2 = get(mouse_x - 12, player_y + 20)
  collide3 = get(mouse_x + 12, player_y + 20)
  collide4 = get(mouse_x, player_y + 40)
  
  if mouse_x < width:
    collide2 = safe
  
  if mouse_x > width:
    collide3 = safe
  
  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    text('💫', mouse_x, player_y)
    score += level
  else:
    text('💥', mouse_x, player_y)
    level = 0

  
def drawObstacles():
  global level
  seed(234645)
  for i in range(level * 2):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * level)
    ob_y %= height
    text('👽', ob_x, ob_y)

  if frame_count % height == height - 1 and level < 5:
    level += 1
    print("you have reached level", level)
  
# Keep this to run your code
run()
