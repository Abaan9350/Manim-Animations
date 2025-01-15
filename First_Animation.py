from manim import *

class SquidGameIntro(Scene):
    def construct(self):
        # Create the text "Squid Game"
        title = Text("Squid Game", font="Arial", color=WHITE).scale(2)

        # Position the title at the center
        title.move_to(ORIGIN)

        # Show the title with a "pop" effect
        self.play(Write(title))
        
        # Create a subtle shake animation for the text
        self.play(title.animate.shift(0.5 * RIGHT), run_time=0.5)
        self.play(title.animate.shift(-1 * RIGHT), run_time=0.5)
        
        # Add a fade-out effect for the title
        self.play(FadeOut(title))

        # Wait before finishing
        self.wait(1)
