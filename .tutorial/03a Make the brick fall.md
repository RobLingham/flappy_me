# Make the brick fall down
We want to have the bird move down all the time and jump up a bit when we click the mouse. We'll do this in two steps... Move up when the mouse is slicked and then move down all the time.
## Move down always
There is another special function that Pygame Zero uses it's called the `update()` function. It will run every frame of the game. We use this function for any calculations or adjustments to the position of game players that happen every time through the game loop.

### 1. Create the update function 
Find the section labelled `#EACH CYCLE THROUGH THE LOOP` and add the function definition for the update function:
```python
def update()
```
Remember that moving down is going to be making the y value bigger. Indented inside the update function you need to add to the brick's y value. I will add 1 but you can try adding bigger numbers to make the brick fall faster.
```python
  brick.y = brick.y + 1
```
### 2. Run your code

If not you can see what the code should look like here (don't peek unless you need to)

<details>
<summary> 👀 Answer</summary>

  ``` python
#SETUP PYGAME ZERO
import pgzrun
#SCREEN
WIDTH = 600
HEIGHT = 400

#SETUP SCORE
#SETUP BRICK
brick = Actor("brick")
brick.x = 90
brick.y = 250
#SETUP WALLS
#BUTTON PRESSES
def on_mouse_down():
    brick.y = brick.y - 50
#DRAW STUFF TO SCREEN
def draw():
  screen.fill("black")
  brick.draw()
#EACH CYCLE THROUGH THE LOOP
def update():
    brick.y = brick.y + 1
    #COLLISIONS
#RESET
#RUN PYGAME ZERO
pgzrun.go()
```
</details>