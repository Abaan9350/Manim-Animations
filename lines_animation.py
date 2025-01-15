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
