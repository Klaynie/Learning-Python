import turtle
import random

# Constants
WIDTH = 800  # px
HEIGHT = 600  # px
FOOD_SIZE = 10  # px
DELAY = 100  # ms


OFFSETS = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

def set_snake_direction(direction):
    global snake_direction
    match direction:
        case "up":
            if snake_direction != "down":
                snake_direction = "up"
        case "down":
            if snake_direction != "up":
                snake_direction = "down"
        case "left":
            if snake_direction != "right":
                snake_direction = "left"
        case "right":
            if snake_direction != "left":
                snake_direction = "right"


def draw_snake():
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()


def self_collision(new_head):
    return new_head in snake


def wall_collision(new_head):
    return new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2


def game_loop():
    stamper.clearstamps()

    # Calculate posittion of new head
    new_head = snake[-1].copy()
    new_head[0] += OFFSETS[snake_direction][0]
    new_head[1] += OFFSETS[snake_direction][1]

    # Check for collision
    if self_collision(new_head) or wall_collision(new_head):
        reset()
    else:
        # Add new head
        snake.append(new_head)

        # Check food collission
        if not food_collision():
            # Remove old tail
            snake.pop(0)

        # Draw new snake
        draw_snake()

        # Refresh screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        # Repeat
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "right"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


# Initialize score
score = 0

# Create window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("#256906")
screen.tracer(0)  # Turn of automatic animation

# Event handlers
screen.listen()
bind_direction_keys()

# Create a turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("#256906", "#0c1e04")
stamper.penup()

# Create snake as a list of coordinate pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "right"

# Initialize score
score = 0

# Draw snake for the first time
draw_snake()

# Food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

# Start animation
game_loop()

# End program
turtle.done()
