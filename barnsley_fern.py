#!/usr/bin/env python3
"""
barnsley_fern.py

Zeichnet den Barnsley-Farn mittels Turtle-Grafik.
Nur Python-Standardbibliothek, kein Internet nötig.
"""

import random
import turtle

def draw_barnsley_fern(iterations: int = 100_000,
                       scale: int = 60,
                       dot_size: int = 2):
    # Fenster und Turtle einrichten
    screen = turtle.Screen()
    screen.title("Barnsley Fern Fractal")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    # Start-Koordinaten
    x, y = 0.0, 0.0
    offset_x, offset_y = 0, -200  # Verschiebung im Fenster

    for i in range(iterations):
        r = random.random()
        # Die vier IFS-Transformationen mit jeweiliger Wahrscheinlichkeit
        if r < 0.01:
            x_new, y_new = 0.0, 0.16 * y
        elif r < 0.86:
            x_new = 0.85 * x + 0.04 * y
            y_new = -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x_new = 0.20 * x - 0.26 * y
            y_new = 0.23 * x + 0.22 * y + 1.6
        else:
            x_new = -0.15 * x + 0.28 * y
            y_new = 0.26 * x + 0.24 * y + 0.44

        x, y = x_new, y_new
        screen_x = x * scale + offset_x
        screen_y = y * scale + offset_y

        t.goto(screen_x, screen_y)
        t.dot(dot_size, "green")

    screen.mainloop()


if __name__ == "__main__":
    draw_barnsley_fern()
