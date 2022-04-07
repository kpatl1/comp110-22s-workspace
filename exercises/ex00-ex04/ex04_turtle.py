"""A Turtle demonstration and exercise that creates a scene."""

__author__ = "730477803"


from turtle import Turtle, done, colormode
from random import randint
"""" Variables below are used to generate random RGB values to fill in the frame of the image."""
randlightnessred: float = randint(230, 255)
randlightnessgreen: float = randint(230, 255)


def main() -> None:
    """Executes all functions in order to paint the landscape."""
    t: Turtle = Turtle()
    colormode(255)
    t.speed(0)
    drawRect(t, -400, -200, 500, 955, 0, 0, 0, 5)

    """Creates a fill for the frame using randomly generated numbers for Red and Green to make a different (light) shade of blue/purple)."""
    t.begin_fill()
    drawRect(t, -398, -198, 495, 950, randlightnessred, randlightnessgreen, 255, 0)
    t.end_fill()

    drawMount(t, -400, 0, 150, "blue3", 2)
    drawMount(t, -295, -35, 150, "CornflowerBlue", 3)
    drawSun(t, 500, 140, 55, "yellow")
    drawRays(t, 462, 180, 45, 25, "yellow")
    done()
    return None


def drawSun(turt: Turtle, x: float, y: float, radius: int, color: str) -> None:
    """Draws the sun in the corner of the frame and fills it in."""
    turt.up()
    turt.goto(x, y)
    turt.down()
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()
    turt.up()
    return None 


def drawRays(turt: Turtle, x: float, y: float, radius: int, distance: int, color: str) -> None:
    """Draws the rays on the sun."""
    degrees: int = 0 
    turt.up()
    turt.goto(x, y)
    turt.setheading(90)
    turt.color(color)
    while degrees < 360:
        turt.forward(radius)
        turt.down()
        turt.forward(distance)
        turt.up()
        turt.backward(distance + radius)
        turt.right(45)
        degrees += 45

    return None


def drawRect(turt: Turtle, x: float, y: float, length: float, width: float, r: float, g: float, b: float, thickness: int) -> None:
    """Used to construct rectangles. In this program it is used to make the frame and fill a frame background color."""
    turt.up()
    turt.goto(x, y)
    turt.down()
    turt.color(r, g, b)
    turt.width(thickness)
    turt.setheading(90)
    turt.forward(length)
    turt.right(90)
    turt.forward(width)
    turt.right(90)
    turt.forward(length)
    turt.right(90)
    turt.forward(width)
    turt.width(2)
    return None


def drawMount(turt: Turtle, x: float, y: float, length: float, color: str, thickness: int) -> None: 
    """Draws the mountains on the landscape using triangle tips."""
    turt.up()
    turt.goto(x, y)
    turt.color(color)
    turt.down()
    turt.width(thickness)
    i = 0
    turt.setheading(45)
    while i < 4:
        turt.forward(length)
        turt.right(90)
        turt.forward(length)
        turt.left(90)
        i += 1
    turt.up()
    return None


if __name__ == "__main__":
    main()