from manim import *

class Shapes(Scene):
    def construct(self):
        # Creating shapes
        circle = Circle()
        square = Square()
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, -1, 0]))
        rectangle = Rectangle(width=2, height=1)
        
        # Showing and animating the circle
        self.play(Create(circle))  # Create circle
        self.play(Transform(circle, square))  # Transition circle into square
        self.play(Transform(square, triangle))  # Transition square into triangle
        self.play(Transform(triangle, rectangle))  # Transition triangle into rectangle
        
        # Transition from rectangle back to circle
        self.play(Transform(rectangle, circle))  # Rectangle turns back into circle
        self.play(Transform(circle, square))  # Circle turns back into square
        self.play(Transform(square, triangle))  # Square turns back into triangle

        # Animate rectangle to shift and scale
        self.play(rectangle.animate.shift(2 * RIGHT))  # Move rectangle to the right
        self.play(rectangle.animate.scale(1.5))  # Scale the rectangle up

        # Fade out all shapes in sequence, transitioning each shape out
        self.play(FadeOut(rectangle))  # Fade out the rectangle
        self.play(FadeOut(triangle))  # Fade out the triangle
        self.play(FadeOut(square))  # Fade out the square
        self.play(FadeOut(circle))  # Fade out the circle

        # End with a wait
        self.wait(1)
