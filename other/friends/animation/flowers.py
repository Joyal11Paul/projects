from manim import *
import numpy as np

class Flower3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Define the 3D flower using a parametric function
        def flower_func(u):
            r = 2 * np.sin(5 * u)  # Creates a 5-petal flower
            x = r * np.cos(u)
            y = r * np.sin(u)
            z = 0.2 * np.sin(10 * u)  # Add some depth
            return np.array([x, y, z])

        flower = ParametricFunction(
            flower_func,
            t_range=[0, TAU],  # Full circle
            color=RED,
            stroke_width=6
        )

        self.play(Create(flower), run_time=3)

        # Rotate the flower for a 3D effect
        self.play(Rotate(flower, angle=PI, axis=UP), run_time=3)

        self.wait(2)
