# Processing for Dynamo 
The focus of this repository is to leverage [Processing.Py](https://processing.org) to simplify and enhance the visualization of Python usage with the Revit API. This approach aims to streamline and clarify the integration process.

# What is Processing?
Processing is a flexible software sketchbook and a language for learning how to code within the context of the visual arts. It's an open-source graphical library and integrated development environment (IDE) built for the electronic arts, new media art, and visual design communities. It was initially developed to serve as a software sketchbook and to teach fundamentals of computer programming in a visual context.

# How Does Processing Work?
Processing provides a simplified interface to Java and allows users to create visual art easily and efficiently. It emphasizes sketching with code, making it very suitable for rapid prototyping and creative coding. The core concepts include:

# Sketches: 

- These are the programs written in Processing. A sketch typically consists of two functions: setup() and draw(). The setup() function runs once when the program starts, and the draw() function continuously executes the lines of code contained inside its block until the program is stopped.
 - Coordinates System: Processing uses a Cartesian coordinate system where the origin (0, 0) is at the top-left corner of the window. The x-coordinate increases to the right, and the y-coordinate increases downwards.
 - Shapes and Colors: It provides simple functions to draw shapes (like line(), ellipse(), rect()) and control their appearance with colors, strokes, and fills.
 - Interaction: Processing supports mouse and keyboard events, allowing for interactive sketches.

# The Library
Processing comes with a set of built-in functions and libraries that simplify working with graphics, animation, and interaction. Here are some fundamental features of its library:

## Drawing Primitives: Basic functions to draw points, lines, rectangles, ellipses, and other shapes.
```py
ellipse(50, 50, 80, 80)
```

## Color Control: Functions to set colors, including fill and stroke.
```py
fill(255, 0, 0)  # Red color
stroke(0)        # Black outline
```

## Transformations: Functions to move (translate()), rotate (rotate()), and scale (scale()) shapes.
```py
translate(50, 50)
rotate(PI / 4)
rect(0, 0, 100, 50)
```

## Interaction: Event functions like mousePressed(), mouseMoved(), and keyPressed().
```py
def mousePressed():
    fill(0, 255, 0)
```

## Animation: The draw() function is called continuously, making it easy to create animations.

```py
def draw():
    background(255)
    ellipse(mouseX, mouseY, 50, 50)
```

## Data Structures: Support for arrays and lists for managing collections of data.

```py
my_list = []
my_list.append(10)
```

## Example Sketch
Here's a simple example that draws a circle following the mouse cursor and changes color when the mouse is pressed:

```py
def setup():
    size(400, 400)
    noStroke()

def draw():
    background(255)
    if mousePressed:
        fill(255, 0, 0)  # Red when mouse is pressed
    else:
        fill(0, 0, 255)  # Blue otherwise
    ellipse(mouseX, mouseY, 50, 50)
```










