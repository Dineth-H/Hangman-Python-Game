import tkinter as tk
import random

# List of words for the game
word_list = [
    "python", "hangman", "programming", "computer", "software", "developer", "challenge", "keyboard", "algorithm", "debugging",
    "machine", "learning", "data", "science", "intelligence", "visualization", "analysis", "artificial", "neural", "network",
    "deep", "learning", "supervised", "unsupervised", "classification", "regression", "ensemble", "clustering", "overfitting", "underfitting",
    "recursion", "iteration", "efficiency", "optimization", "abstraction", "iteration", "automation", "scripting", "integration", "database",
    "framework", "interface", "encryption", "security", "authentication", "authorization", "middleware", "deployment", "scalability", "agile", 
    "repository", "version", "control", "repository", "commit", "branch", "merge", "conflict", "agile", "sprint", "product", "backlog",
    "retrospective", "continuous", "integration", "deployment", "repository", "software", "architecture", "testing", "unit", "integration", "functional",
    "system", "user", "acceptance", "testing", "bug", "issue", "feature", "requirement", "documentation", "code", "review", "framework", "library",
    "dependency", "front-end", "back-end", "full-stack", "responsive", "design", "framework", "library", "dependency", "front-end", "back-end", "full-stack",
    "responsive", "design", "framework", "library", "dependency", "front-end", "back-end", "full-stack", "responsive", "design", "interface", "user",
    "experience", "usability", "wireframe", "prototype", "iteration", "responsive", "design", "interface", "user", "experience", "usability", "wireframe",
    "prototype", "iteration" 
    ]

# Function to start a new game
def new_game():
    global secret_word, guessed_word, guesses_left, guessed_letters
    secret_word = random.choice(word_list).lower()
    guessed_word = ['_'] * len(secret_word)
    guesses_left = 6
    guessed_letters = []
    guess_entry.config(state=tk.NORMAL)  # Re-enable the entry widget
    update_display()

# Function to make a guess
def make_guess():
    global guesses_left
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    if guess in guessed_letters:
        return  # Skip if the letter was already guessed
    
    guessed_letters.append(guess)
    
    if guess not in secret_word:
        guesses_left -= 1
    
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            guessed_word[i] = guess
    
    update_display()
    
    if ''.join(guessed_word) == secret_word:
        result_label.config(text="Congratulations! You guessed the word.")
        guess_entry.config(state=tk.DISABLED)
    elif guesses_left == 0:
        result_label.config(text=f"Game over. The word was '{secret_word}'.")
        guess_entry.config(state=tk.DISABLED)
    else:
        result_label.config(text=f"Guesses left: {guesses_left}")

# Function to update the display
def update_display():
    word_label.config(text=' '.join(guessed_word))
    hangman_stage_label.config(text=hangman_stages[6 - guesses_left])
    guessed_letters_label.config(text="Guessed Letters: " + ', '.join(guessed_letters))

# Create the main window
window = tk.Tk()
window.title("Hangman Game")
window.configure(bg="black")

# Hangman stages (ASCII art)
hangman_stages = [
    """
    
    """,
    """
    |
    
    """,
    """
    |
    O
    
    """,
    """
    |
    O
    |
    
    """,
    """
    |
    O
   /|
    
    """,
    """
    |
    O
   /|\\
    
    """,
    """
    |
    O
   /|\\
   / \\
    
    """
]

# Create and configure widgets
word_label = tk.Label(window, text='', font=("Helvetica", 20), fg="white", bg="black")
guess_entry = tk.Entry(window, font=("Helvetica", 14))
guess_button = tk.Button(window, text="Guess", command=make_guess, font=("Helvetica", 14))
new_game_button = tk.Button(window, text="New Game", command=new_game, font=("Helvetica", 14))
result_label = tk.Label(window, text='', font=("Helvetica", 16), fg="white", bg="black")
hangman_stage_label = tk.Label(window, text='', font=("Courier", 12), fg="white", bg="black")
guessed_letters_label = tk.Label(window, text='', font=("Helvetica", 14), fg="white", bg="black")

# Place widgets on the grid with alignment
word_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
hangman_stage_label.grid(row=1, column=0, columnspan=3, sticky='n')
guessed_letters_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
guess_entry.grid(row=3, column=0, padx=10, pady=10)
guess_button.grid(row=3, column=1, padx=10, pady=10)
new_game_button.grid(row=3, column=2, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=3)

# Start a new game
new_game()

# Add a label for the creator and Python version
creator_label = tk.Label(window, text="Created by DinethH using Python 3 - 2023", font=("Helvetica", 12), fg="white", bg="black")
creator_label.grid(row=5, column=0, columnspan=3, pady=(20, 0))

# Start the GUI main loop
window.mainloop()
