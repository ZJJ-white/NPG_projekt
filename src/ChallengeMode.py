import customtkinter as ctk
import tkinter as tk
import random
import os
from datetime import datetime


class ChallengeModeWindow(ctk.CTkToplevel):
    def __init__(self, passwords):
        super().__init__()
        self.geometry("600x350")
        self.title("Tryb Challenge")
        self.passwords = passwords

        self.original_word_pool = {}  # kopie słowników słów
        self.word_pool = {}
        for level in passwords:
            self.original_word_pool[level] = passwords[level][:]
            self.word_pool[level] = passwords[level][:]

        self.current_word = ""
        self.score = 0
        self.time_left = 30
        self.timer_running = False
        self.paused = False

        self.difficulty = ctk.StringVar(value="Easy")
        self.build_ui()

    def build_ui(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#101010")
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.85, relheight=0.75)

        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.difficulty_menu = ctk.CTkOptionMenu(self.main_frame, values=["Easy", "Medium", "Hard"],
                                                 variable=self.difficulty)
        self.difficulty_menu.grid(row=0, column=0, pady=(10, 0))

        self.word_label_bg = ctk.CTkFrame(self.main_frame, fg_color="black", corner_radius=10)
        self.word_label_bg.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.word_label = ctk.CTkLabel(self.word_label_bg, text="", font=("Arial", 24, "bold"))
        self.word_label.pack(padx=10, pady=10)

        self.entry = ctk.CTkEntry(self.main_frame, font=("Arial", 16))
        self.entry.grid(row=2, column=0, pady=5)
        self.entry.bind("<Return>", lambda event: self.check_word())

        self.time_label = ctk.CTkLabel(self.main_frame, text="Czas: 30", font=("Arial", 16))
        self.time_label.grid(row=3, column=0, pady=2)

        self.score_label = ctk.CTkLabel(self.main_frame, text="Wynik: 0", font=("Arial", 16))
        self.score_label.grid(row=4, column=0, pady=2)

        self.pause_button = ctk.CTkButton(self.main_frame, text="⏸ Pauza", command=self.toggle_pause)
        self.pause_button.grid(row=5, column=0, pady=5)

        self.start_button = ctk.CTkButton(self.main_frame, text="▶ Start", command=self.start_game)
        self.start_button.grid(row=6, column=0, pady=5)

        self.exit_button = ctk.CTkButton(self.main_frame, text="Wyjdź do menu", fg_color="gray", command=self.destroy)
        self.exit_button.grid(row=7, column=0, pady=(0, 10))

    def start_game(self):
        self.score = 0
        self.time_left = 30
        self.timer_running = True
        self.paused = False
        self.entry.configure(state="normal")
        self.entry.delete(0, 'end')
        self.entry.focus()
        self.score_label.configure(text="Wynik: 0")
        self.time_label.configure(text="Czas: 30")
        self.reset_word_pool()
        self.next_word()
        self.update_timer()
        self.apply_difficulty_colors()

    def update_timer(self):
        if self.time_left > 0 and self.timer_running and not self.paused:
            self.time_label.configure(text=f"Czas: {self.time_left}")
            self.time_left -= 1
            self.after(1000, self.update_timer)
        elif self.time_left <= 0:
            self.end_game()

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.configure(text="▶ Wznów")
        else:
            self.pause_button.configure(text="⏸ Pauza")
            self.update_timer()

    def reset_word_pool(self):
        level = self.difficulty.get()
        self.word_pool[level] = self.original_word_pool[level][:]

    def next_word(self):
        level = self.difficulty.get()
        if not self.word_pool[level]:
            self.reset_word_pool()
        self.current_word = random.choice(self.word_pool[level])
        self.word_pool[level].remove(self.current_word)
        self.word_label.configure(text=self.current_word)

    def check_word(self, event=None):
        typed = self.entry.get().strip()
        if typed == self.current_word:
            self.score += 1
            self.score_label.configure(text=f"Wynik: {self.score}")
        self.entry.delete(0, 'end')
        self.next_word()

    def end_game(self):
        self.timer_running = False
        self.word_label.configure(text="Koniec!")
        self.entry.configure(state="disabled")
        self.time_label.configure(text="Czas: 0")
        self.save_result()

    def save_result(self):
        result_path = os.path.join(os.path.dirname(__file__), "..", "results.txt")
        with open(result_path, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} | {self.difficulty.get()} | {self.score} punktów\n")

    def apply_difficulty_colors(self):
        level = self.difficulty.get()
        if level == "Easy":
            bg_color = "#24c707"
            text_color = "white"
        elif level == "Medium":
            bg_color = "#efeb00"
            text_color = "white"
        else:  # Hard
            bg_color = "#c70039"
            text_color = "white"

        self.configure(fg_color=bg_color)
        self.word_label.configure(text_color=text_color)
        self.word_label_bg.configure(fg_color="black")
        self.entry.configure(fg_color="white", text_color="black")