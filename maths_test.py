from manim import *

class Shapes(Scene):
    def construct(self):
        # Making shapes
        circle = Circle()
        square = Square()
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, -1, 0]))
        rectangle = Rectangle(width=2, height=1)
        
        # Showing and animating the circle
        self.play(Create(circle))  # Create circle
        self.play(FadeOut(circle))  # Fade out circle
        
        # Showing and animating the square
        self.play(GrowFromCenter(square))  # Grow square from center
        self.play(Transform(square, triangle))  # Transform square to triangle
        self.play(FadeOut(square))  # Fade out transformed triangle
        
        # Showing and animating the rectangle
        self.play(Create(rectangle))  # Create rectangle
        self.play(rectangle.animate.shift(2 * RIGHT))  # Move rectangle to the right
        self.play(rectangle.animate.scale(1.5))  # Scale the rectangle up
        
        # Adding another transformation: Circle -> Square
        new_circle = Circle(color=BLUE)
        self.play(Create(new_circle))  # Create new blue circle
        self.play(Transform(new_circle, square))  # Transform circle to square
        self.play(FadeOut(new_circle))  # Fade out the square
        
        # More transformations: Circle -> Triangle
        new_triangle = Polygon(np.array([0, 0, 0]), np.array([2, 2, 0]), np.array([2, -2, 0]))
        self.play(Create(new_triangle))  # Create new triangle
        self.play(Transform(new_triangle, rectangle))  # Transform triangle to rectangle
        self.play(FadeOut(new_triangle))  # Fade out the rectangle
        
        # End with a wait
        self.wait(1)
