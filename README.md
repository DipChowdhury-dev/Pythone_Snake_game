# 🐍 Python Snake Game with Dynamic Difficulty Scaling

A classic, feature-rich **Snake Game** built in Python using **Pygame**. This project demonstrates both procedural and clean Object-Oriented Programming (OOP) paradigms with real-time HUD rendering, collision physics, and dynamic difficulty scaling.

---

## 📋 Table of Contents
- [✨ Key Features](#-key-features)
- [📁 Project Structure](#-project-structure)
- [🎮 Controls](#-controls)
- [⚙️ Dynamic Difficulty Mechanics](#-dynamic-difficulty-mechanics)
- [📖 Class & Method Documentation](#-class--method-documentation)
- [🚀 Quick Start & Installation](#-quick-start--installation)

---

## ✨ Key Features
- **Object-Oriented Architecture**: Modular design encapsulated inside the `SnakeGame` class.
- **Dynamic Speed Progression**: Frame rate starts at a relaxed **6 FPS** and increases progressively as your score climbs.
- **Level Scaling**: Increases your level for every 5 points scored (`Level 1`, `Level 2`, etc.).
- **Smart Food Spawning**: Ensures food never spawns directly inside the snake's body.
- **Directional Lock Prevention**: Prevents the snake from accidentally reversing directly into itself (e.g., pressing `DOWN` while moving `UP`).
- **Real-Time HUD**: On-screen overlay displaying **Score**, **Level**, and **Current FPS**.

---

## 📁 Project Structure

| File | Type | Description |
| :--- | :--- | :--- |
| **[SnakeGame copy.py](file:///d:/Dip-2026%20All%20files/1%29%20Dip%20Programing/Pythone/Snake%20game/SnakeGame%20copy.py)** | **OOP (Recommended)** | Class-based implementation (`SnakeGame`). Highly clean, modular, and extensible. |
| **[SnakeGame.py](file:///d:/Dip-2026%20All%20files/1%29%20Dip%20Programing/Pythone/Snake%20game/SnakeGame.py)** | **Procedural** | Script-level procedural implementation for simple quick runs. |

---

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| <kbd>↑</kbd> Arrow Up | Move Up |
| <kbd>↓</kbd> Arrow Down | Move Down |
| <kbd>←</kbd> Arrow Left | Move Left |
| <kbd>→</kbd> Arrow Right | Move Right |
| `Close Window (X)` | Exit Game |

---

## ⚙️ Dynamic Difficulty Mechanics

The game dynamically adjusts its pace based on your score using mathematical formulas:

1. **Level Formula**:
   $$\text{Level} = \left\lfloor \frac{\text{Score}}{5} \right\rfloor + 1$$
   *Increases level after every 5 points.*

2. **FPS (Speed) Scaling Formula**:
   $$\text{Current FPS} = \min\left(\text{Initial FPS} + \left\lfloor \frac{\text{Score}}{2} \right\rfloor, 25\right)$$
   *Adds +1 FPS for every 2 points, starting at **6 FPS** and capped at **25 FPS** for playability.*

---

## 📖 Class & Method Documentation

### Class: `SnakeGame`
Defined in **[SnakeGame copy.py](file:///d:/Dip-2026%20All%20files/1%29%20Dip%20Programing/Pythone/Snake%20game/SnakeGame%20copy.py)**. Handles window creation, game states, loop management, collision physics, and graphics rendering.

#### Attributes:
- `initial_fps` *(int)*: Starting speed at level 1 (default: `6`).
- `screen` *(pygame.Surface)*: 400x400 display window surface.
- `clock` *(pygame.time.Clock)*: Controls frame rate timing.
- `font` & `small_font` *(pygame.font.Font)*: System fonts for rendering HUD text.
- `snake` *(list of tuple)*: Ordered list of coordinates `[(x, y), ...]` representing the body.
- `snake_dir` *(tuple)*: Active velocity vector `(dx, dy)` in 20px grid steps.
- `food` *(pygame.Rect)*: Rectangle object storing food position.
- `score` *(int)*: Total points earned.

---

### Method Breakdown

#### 1. `__init__(self, initial_fps=6)`
- **What it does**: Initializes the Pygame environment, configures the 400x400 window display, sets window captions, loads fonts, and triggers `reset_game()`.
- **How it works**:
  ```python
  pygame.init()
  self.screen = pygame.display.set_mode((400, 400))
  self.clock = pygame.time.Clock()
  ```

#### 2. `reset_game(self)`
- **What it does**: Resets game state variables back to default positions when starting or upon game over.
- **How it works**:
  - Sets snake head at screen center `(200, 200)`.
  - Sets velocity to stationary `(0, 0)`.
  - Generates food coordinates on a 20px grid using `random.randrange(0, 380, 20)`.
  - Resets `score` to `0`.

#### 3. `run(self)`
- **What it does**: Contains the main `while running:` game loop. Executes input polling, movement updating, collision detection, HUD rendering, and frame timing.
- **How it works**:
  - **Input Handling**: Checks keyboard keys and prevents instantaneous 180-degree turn reversals.
  - **Movement**: Inserts new head segment at index `0`. If food is eaten, score increases and new food spawns; otherwise, `snake.pop()` removes tail segment.
  - **Collision Checks**: Detects wall boundary limits (`< 0` or `>= 400`) and self-touching (`head in snake[1:]`).
  - **Rendering**: Redraws background, green snake blocks, red food block, and white HUD text on each frame.
  - **Clock Tick**: Calls `self.clock.tick(current_fps)` to maintain dynamic game speed.

---

## 🚀 Quick Start & Installation

### Prerequisites
Make sure you have Python 3 installed along with `pygame` or `pygame-ce`:

```bash
pip install pygame
```

### Running the Game

To run the **OOP version** (recommended):
```bash
python "SnakeGame .py"
```

To run the **Procedural version**:
```bash
python "SnakeGame.py"
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
