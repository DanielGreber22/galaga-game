import pgzrun
import random
#screen dimensions
WIDTH = 1200
HEIGHT = 600
#create a ship
ship = Actor('galaga')
bug = Actor('bug')

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 2

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

#creating enemies 
for x in range(8):
    for y in range(4):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y

score = 0
direction = 1
ship.dead = False 
ship.countdown = 90 

def display_score():
    screen.draw.text(str(score),(50,50))

def game_over()