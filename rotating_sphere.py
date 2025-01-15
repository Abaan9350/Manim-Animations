from manim import *

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
