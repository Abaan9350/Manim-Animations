from manim import *

# Set the FPS to 60
config.frame_height = 8.0
config.frame_width = 14.0
config.fps = 60

class SimpleScene(Scene):
    def construct(self):
        # Create a square
        square = Square()

        # Display the square on screen
        self.play(Create(square))

        # Rotate the square 45 degrees
        self.play(Rotate(square, PI / 4))

        # Wait for 1 second before the scene ends
        self.wait(1)
