import pgzrun
import random
import os

#hi! If you're reading this, welcome. I started making this game based on a tutorial, and then added in some of my own style. I used claude to help make some of it, but the majority of it i made on my own. hope you enjoy! 

#if you're interested in the tutorial, here's the link: https://www.youtube.com/watch?v=AY9Mn

#ok bye fren

# SCREEN
WIDTH = 800
HEIGHT = 600

# SETUP SCORE
score = 0
high_score = 0

# SETUP SUBJECT
subject = Actor("subject")
subject.x = 90
subject.y = 250

# SETUP WALLS
walls = []

def create_wall_pair():
    gap = random.randint(200, 300)
    top_height = random.randint(50, HEIGHT - gap - 50)

    wall_top = Actor("wall-top")
    wall_top.x = WIDTH
    wall_top.y = top_height - wall_top.height

    wall_bottom = Actor("wall-bottom")
    wall_bottom.x = WIDTH
    wall_bottom.y = top_height + gap

    return (wall_top, wall_bottom)

# BUTTON PRESSES
def on_mouse_down():
    print("The mouse has been clicked!")
    subject.y = subject.y - 50

# DRAW STUFF TO SCREEN
def draw():
    screen.fill("light blue")
    subject.draw()
    for wall_pair in walls:
        wall_pair[0].draw()
        wall_pair[1].draw()
    screen.draw.text(f"Score: {score}", (50, 30), color="orange")
    screen.draw.text(f"High Score: {high_score}", (50, 50), color="blue")

# EACH CYCLE THROUGH THE LOOP
def update():
    global score, high_score

    subject.y = subject.y + 1

    # Move existing walls
    for wall_pair in walls:
        wall_pair[0].x -= 2
        wall_pair[1].x -= 2

        # Check if a wall has passed the left side of the screen
        if wall_pair[0].right < 0:
            score += 1
            if score > high_score:
                high_score = score
                save_high_score()

    # Remove walls that are off-screen
    walls[:] = [wall for wall in walls if wall[0].right > 0]

    # Generate new walls
    if len(walls) == 0 or walls[-1][0].x < WIDTH - 300:
        walls.append(create_wall_pair())

    # Check collisions
    if subject.y > HEIGHT:
        reset()
    for wall_pair in walls:
        if subject.colliderect(wall_pair[0]) or subject.colliderect(wall_pair[1]):
            reset()

# RESET
def reset():
    global score, walls
    print("The game is resetting!")
    subject.y = 250
    walls.clear()
    score = 0

# HIGH SCORE FUNCTIONS
def load_high_score():
    global high_score
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    else:
        high_score = 0

def save_high_score():
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))

# INITIALIZE HIGH SCORE
load_high_score()

# RUN PYGAME ZERO
pgzrun.go()