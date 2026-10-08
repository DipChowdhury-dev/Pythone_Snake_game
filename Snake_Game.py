"""
Snake Game (Object-Oriented Implementation)
===========================================
A modern, dynamic Snake game built using Pygame in Python.
Features real-time collision detection, progressive speed/level scaling,
and clean object-oriented architecture.
"""

import pygame
import random


class SnakeGame:
    """
     Manages the core state, logic, event loops, rendering, and dynamic difficulty 
     for the Snake Game.
    
     Attributes:
        initial_fps (int): Base frame rate at starting level 1 (default: 6 FPS).
        screen (pygame.Surface): Display window surface (400x400).
        clock (pygame.time.Clock): Pygame clock object for frame rate management.
        font (pygame.font.Font): Font used for rendering main score text.
        small_font (pygame.font.Font): Font used for rendering level and FPS HUD text.
        snake (list of tuple): List of (x, y) coordinates representing the snake body segments.
        snake_dir (tuple): Current movement velocity tuple (dx, dy) in pixels per step.
        food (pygame.Rect): Rect representing position and bounds of the food item.
        score (int): Player's current total score.
    """

    def __init__(self, initial_fps=6):
        """
         Initializes Pygame modules, display settings, fonts, and sets the starting game state.

         Args:
            initial_fps (int, optional): The starting speed (frame rate) of the snake. 
                                         Defaults to 6 FPS.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.initial_fps = initial_fps
        self.reset_game()

    def reset_game(self):
        """
         Resets all gameplay variables to their initial starting positions.
         
         This method is invoked at startup and whenever the player crashes into a wall 
         or their own body segment (Game Over state).
        
         Actions performed:
          - Sets snake starting position to center (200, 200).
          - Resets snake movement velocity to stationary (0, 0).
          - Spawns food at a random grid coordinate (aligned to 20px grid).
          - Resets score back to 0.
        """
        self.snake = [(200, 200)]
        self.snake_dir = (0, 0)
        self.food = pygame.Rect(
            random.randrange(0, 380, 20),
            random.randrange(0, 380, 20),
            20, 20
        )
        self.score = 0

    def run(self):
        """
         Executes the main game loop until the player closes the window.
 
         The main game loop performs four primary operations on every frame:
          1. Event Handling: Listens for window QUIT events and arrow key directions.
          2. Movement & Collision Logic: Moves snake head, checks food consumption,
             prevents self-collision, detects grid boundaries, and triggers resets on death.
          3. Dynamic Difficulty Calculation: Dynamically calculates Level and FPS based
             on score (`current_fps = min(initial_fps + score // 2, 25)`).
          4. Rendering & Display: Clears background, draws snake segments, food item,
             and HUD status text, then updates display and ticks clock.
        """
        running = True
        while running:
            # 1. Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Key controls handling (prevents 180-degree immediate reversal)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.snake_dir != (0, 20):
                self.snake_dir = (0, -20)
            elif keys[pygame.K_DOWN] and self.snake_dir != (0, -20):
                self.snake_dir = (0, 20)
            elif keys[pygame.K_LEFT] and self.snake_dir != (20, 0):
                self.snake_dir = (-20, 0)
            elif keys[pygame.K_RIGHT] and self.snake_dir != (-20, 0):
                self.snake_dir = (20, 0)

            # 2. Movement & Collision Logic
            if self.snake_dir != (0, 0):
                head = (self.snake[0][0] + self.snake_dir[0],
                        self.snake[0][1] + self.snake_dir[1])
                self.snake.insert(0, head)
                
                # Check food collision
                if pygame.Rect(head, (20, 20)).colliderect(self.food):
                    self.score += 1
                    place_food = False
                    while not place_food:
                        self.food.topleft = (random.randrange(0, 380, 20),
                                            random.randrange(0, 380, 20))
                        if self.food.topleft not in self.snake:
                            place_food = True
                else:
                    self.snake.pop()

                # Check boundary collisions and self-collisions
                if (head in self.snake[1:] or head[0] < 0 or 
                    head[0] >= 400 or head[1] < 0 or head[1] >= 400):
                    self.reset_game()

            # 3. Dynamic Difficulty & Speed Scaling
            level = (self.score // 5) + 1
            current_fps = min(self.initial_fps + (self.score // 2), 25)

            # 4. Rendering & Display
            self.screen.fill((0, 0, 0))
            for pos in self.snake:
                pygame.draw.rect(self.screen, (0, 255, 0), (pos[0], pos[1], 20, 20))
            pygame.draw.rect(self.screen, (255, 0, 0), self.food)

            # Display Score, Level, and Speed on HUD
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            level_text = self.small_font.render(f"Level {level} | Speed: {current_fps} FPS", True, (200, 200, 200))
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(level_text, (200, 18))

            pygame.display.flip()

            # Control Frame Rate
            self.clock.tick(current_fps)

        pygame.quit()


if __name__ == "__main__":
    game = SnakeGame(initial_fps=6)
    game.run()