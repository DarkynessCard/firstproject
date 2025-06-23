import tkinter as tk

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplayer Hangman")
        self.max_attempts = 6
        self.player_turn = 1  # Player 1 starts as word setter
        self.player_word = ""
        self.reset_game()

    def reset_game(self):
        self.word = ""
        self.guessed = []
        self.remaining_attempts = self.max_attempts
        self.get_secret_word()

    def get_secret_word(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Label for player whose turn it is
        tk.Label(self.root, text=f"Player {self.player_turn}: Enter a word", font=("Arial", 14)).pack(pady=10)

        # Input for the secret word (masked)
        self.entry = tk.Entry(self.root, font=("Arial", 14), show="*")
        self.entry.pack(pady=5)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.start_game).pack(pady=10)

    def start_game(self):
        self.word = self.entry.get().lower()
        if not self.word.isalpha() or len(self.word) < 2:
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root, width=200, height=250, bg="orange")
        self.canvas.pack(pady=10)

        self.word_display = tk.StringVar()
        self.message_display = tk.StringVar()
        self.attempts_display = tk.StringVar()
        self.feedback_display = tk.StringVar()

        tk.Label(self.root, text=f"Player {3 - self.player_turn} Guess Now!", font=("Arial", 14)).pack()
        tk.Label(self.root, textvariable=self.word_display, font=("Courier", 24)).pack()
        tk.Label(self.root, textvariable=self.attempts_display, font=("Arial", 12)).pack()
        tk.Label(self.root, textvariable=self.feedback_display, font=("Arial", 12), fg="blue").pack()
        tk.Label(self.root, textvariable=self.message_display, font=("Arial", 12), fg="red").pack()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, command=lambda l=letter: self.guess(l.lower()))
            btn.grid(row=i//9, column=i%9, padx=2, pady=2)

        self.restart_button = tk.Button(self.root, text="Next Round", command=self.next_round, state=tk.DISABLED)
        self.restart_button.pack(pady=10)

        self.update_display()
        self.draw_base()

    def update_display(self):
        displayed = " ".join([ch if ch in self.guessed else "_" for ch in self.word])
        self.word_display.set(displayed)
        self.attempts_display.set(f"Attempts Left: {self.remaining_attempts}")

        if "_" not in displayed:
            self.message_display.set(f"Player {3 - self.player_turn} Wins! 🎉")
            self.end_game()

        elif self.remaining_attempts == 0:
            self.message_display.set(f"Player {3 - self.player_turn} Loses! Word was: {self.word}")
            self.end_game()

    def guess(self, letter):
        if letter in self.guessed:
            return

        self.guessed.append(letter)

        if letter in self.word:
            self.feedback_display.set(f"✔ Correct: '{letter.upper()}' is in the word!")
        else:
            self.feedback_display.set(f"✘ Wrong: '{letter.upper()}' is not in the word.")
            self.remaining_attempts -= 1
            self.draw_next()

        self.update_display()

    def end_game(self):
        for btn in self.buttons_frame.winfo_children():
            btn.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)

    def next_round(self):
        self.player_turn = 3 - self.player_turn  # Switch player: 1 ↔ 2
        self.reset_game()

    # --- Drawing Functions ---

    def draw_base(self):
        self.canvas.create_line(20, 230, 180, 230)  # Base
        self.canvas.create_line(50, 230, 50, 20)    # Pole
        self.canvas.create_line(50, 20, 120, 20)    # Top beam
        self.canvas.create_line(120, 20, 120, 40)   # Rope

    def draw_next(self):
        step = self.max_attempts - self.remaining_attempts
        if step == 1:
            self.canvas.create_oval(100, 40, 140, 80)  # Head
        elif step == 2:
            self.canvas.create_line(120, 80, 120, 140)  # Body
        elif step == 3:
            self.canvas.create_line(120, 100, 90, 120)  # Left arm
        elif step == 4:
            self.canvas.create_line(120, 100, 150, 120)  # Right arm
        elif step == 5:
            self.canvas.create_line(120, 140, 100, 180)  # Left leg
        elif step == 6:
            self.canvas.create_line(120, 140, 140, 180)  # Right leg

# --- Start the Game ---
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()