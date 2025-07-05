# 🎮 Project Module Description

## 🔹 `import pygame`
This imports the **Pygame** library so you can use its built-in functions and features, such as:
- Creating a game window  
- Handling user events  
- Drawing shapes, images, and more

---

## 🔹 `class Main:`
Defines a **class** named `Main`.  
A class is like a blueprint for creating objects — in this case, the game controller.  
It will hold all the necessary code and settings to run your game.

---

## 🔹 `def __init__(self):`
This is the **constructor method** of the `Main` class.  
It is automatically called when an object of the class is created.  
Used to initialize game settings like the screen window.

---

## 🔹 `pygame.init()`
Initializes all imported Pygame modules.  
⚠️ This **must be called** before using any Pygame features like graphics, sound, etc.

---

## 🔹 `self.screen = pygame.display.set_mode((1200, 800))`
- Creates the main **game window** of size **1200x800 pixels**
- Stores the window surface in `self.screen` so you can draw on it later

---

## 🔹 `def run_game(self):`
Defines the method `run_game()` inside the `Main` class.  
This is your **main game loop**, responsible for keeping the game running and checking for input.

---

## 🔹 `while True:`
Creates an **infinite loop** that continuously runs as long as the game is active.

---

## 🔹 `for event in pygame.event.get():`
- Retrieves all user-generated events like key presses, mouse clicks, or window close
- Loops through each event to handle them individually

---

## 🔹 `if event.type == pygame.QUIT:`
Checks if the user has clicked the window **close (X)** button.  
If so, the program will exit cleanly.

---

## 🔹 `pygame.quit()`
- Properly shuts down all Pygame modules
- Closes the game window

---

## 🔹 `return`
- Exits the `run_game()` function  
- Stops the game loop and ends the program gracefully

---

## 🔹 `pygame.display.flip()`
Updates the entire game window.  
Even though there's nothing drawn yet, this line refreshes the screen every loop cycle.

---

## 🔹 `main = Main()`
Creates an object of the `Main` class.  
This calls the constructor method and **sets up the game window**.

---

## 🔹 `main.run_game()`
Starts the main game loop by calling the `run_game()` method.  
Keeps the window open and responsive until the user closes it.
