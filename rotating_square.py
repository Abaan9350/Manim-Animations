from manim import *

class RotatingSquare(Scene):
    def construct(self):
        # Create a square
        square = Square()

        # Display the square on screen
        self.play(Create(square))

        # Rotate the square 45 degrees
        self.play(Rotate(square, PI / 4))

        # Wait before ending the scene
        self.wait(1)
