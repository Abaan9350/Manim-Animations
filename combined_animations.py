from manim import *

class LinesAnimation(Scene):
    def construct(self):
        # Create several lines
        lines = VGroup(
            Line(LEFT, RIGHT),
            Line(UP, DOWN),
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT)
        )
        
        # Position lines
        lines.arrange_in_grid(rows=2, cols=2, buff=0.5)

        # Display lines
        self.play(LaggedStartMap(Create, lines))

        # Animate the lines moving in different directions
        self.play(
            lines[0].animate.shift(UP),
            lines[1].animate.shift(DOWN),
            lines[2].animate.shift(RIGHT),
            lines[3].animate.shift(LEFT),
            run_time=2
        )
        
        # Rotate all lines together
        self.play(Rotate(lines, angle=PI / 4, about_point=ORIGIN))

        # Wait before ending the scene
        self.wait(1)


class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()


class RotatingSphereScene(ThreeDScene):
    def construct(self):
        # Create a 3D sphere
        sphere = Sphere(radius=2)

        # Set the sphere's color to blue
        sphere.set_fill(BLUE, opacity=0.7)
        
        # Add a glowing effect
        sphere.set_shade_in_3d(True)

        # Display the sphere
        self.play(Create(sphere))

        # Rotate the sphere along both axes
        self.play(
            Rotate(sphere, angle=PI, axis=UP),
            Rotate(sphere, angle=PI / 2, axis=RIGHT),
            run_time=4
        )

        # Wait for a moment before the animation ends
        self.wait(1)


class AllAnimations(Scene):
    def construct(self):
        # Play the first animation (LinesAnimation)
        self.play(LinesAnimation().construct())

        # Wait for a brief moment
        self.wait(1)

        # Play the second animation (PointMovingOnShapes)
        self.play(PointMovingOnShapes().construct())

        # Wait for a brief moment
        self.wait(1)

        # Play the third animation (RotatingSphereScene)
        self.play(RotatingSphereScene().construct())
