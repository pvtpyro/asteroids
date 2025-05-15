activate virtual environment with `source venv/bin/activate` in WSL

run program with `python3 main.py`

## Delta Time

In math, the Greek letter delta (Δ) is often used to represent a change in a value. In game development, we use "delta time" to represent the amount of time that has passed since the last frame was drawn. This value is useful to decouple the game's speed from the speed it's being drawn to the screen.

If your computer speeds up, the asteroids shouldn't also speed up. Conversely, if your computer slows down, the asteroids shouldn't also slow down: they would just move less smoothly.