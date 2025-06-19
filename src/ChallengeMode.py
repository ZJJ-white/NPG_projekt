import customtkinter as ctk
import tkinter as tk
import random
import os
from datetime import datetime
import src.IO as IO




class ChallengeModeWindow(ctk.CTkToplevel):
    def __init__(self, passwords, score=0, time_left=30, nick="", difficulty="Easy"):
        super().__init__()
        self.geometry("600x400")
        self.title("Tryb Challenge")
        self.passwords = passwords

        self.current_word = ""
        self.score = score
        self.time_left = time_left
        self.timer_running = False
        self.paused = False
        self.used_words = []
        self.username = nick

        self.difficulty = ctk.StringVar(value=difficulty)

        # Nowy frame tła
        self.bg_frame = ctk.CTkFrame(self, corner_radius=0)
        self.bg_frame.pack(fill="both", expand=True)

        self.realtime_clock = ctk.CTkLabel(self.bg_frame, text="", font=("Arial", 14))
        self.realtime_clock.place(relx=0.97, rely=0.03, anchor="ne")

        self.username_window()
        self.update_realtime_clock()

    def username_window(self):
        self.username_popup = ctk.CTkToplevel(self)
        self.username_popup.geometry("300x150")
        self.username_popup.title("Podaj nazwę gracza")

        label = ctk.CTkLabel(self.username_popup, text="Wprowadź swój nick:")
        label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self.username_popup)
        self.username_entry.pack(pady=5)

        confirm_button = ctk.CTkButton(self.username_popup, text="OK", command=self.set_username)
        confirm_button.pack(pady=10)

    def set_username(self):
        name = self.username_entry.get().strip()
        if name:
            self.username = name
            self.username_popup.destroy()
            self.build_ui()

    def build_ui(self):
        self.main_frame = ctk.CTkFrame(self.bg_frame, corner_radius=10, fg_color="#101010")
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.85, relheight=0.75)

        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.difficulty_menu = ctk.CTkOptionMenu(self.main_frame, values=["Easy", "Medium", "Hard"],
                                                 variable=self.difficulty)
        self.difficulty_menu.grid(row=0, column=0, pady=(10, 5))

        self.word_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 24, "bold"))
        self.word_label.grid(row=1, column=0, pady=10)

        self.entry = ctk.CTkEntry(self.main_frame, font=("Arial", 16))
        self.entry.grid(row=2, column=0, pady=10)
        self.entry.bind("<Return>", lambda event: self.check_word())

        self.time_label = ctk.CTkLabel(self.main_frame, text=f"Czas: {self.time_left}", font=("Arial", 16))
        self.time_label.grid(row=3, column=0, pady=10)

        self.score_label = ctk.CTkLabel(self.main_frame, text=f"Wynik: {self.score}", font=("Arial", 16))
        self.score_label.grid(row=4, column=0, pady=10)
        
        
        self.start_button = ctk.CTkButton(self.main_frame, text="Start", command=self.start_game)
        self.start_button.grid(row=5, column=0, pady=5)

        self.pause_button = ctk.CTkButton(self.main_frame, text="Pauza", command=self.toggle_pause)
        self.pause_button.grid(row=6, column=0, pady=(0, 5))

        self.exit_button = ctk.CTkButton(self.main_frame, text="Wyjdź do menu", fg_color="gray", command=self.destroy)
        self.exit_button.grid(row=7, column=0, pady=(0, 10))

        self.apply_difficulty_colors()

    def apply_difficulty_colors(self):
        level = self.difficulty.get()
        if level == "Easy":
            bg_color = "#1a4208"
        elif level == "Medium":
            bg_color = "#595c00"
        else:  # Hard
            bg_color = "#4d0011"

        self.bg_frame.configure(fg_color=bg_color)
        self.main_frame.configure(fg_color="#101010")
        self.word_label.configure(text_color="white")

    def start_game(self):
        self.score = 0
        self.time_left = 30
        self.timer_running = True
        self.paused = False
        self.used_words = []
        self.entry.configure(state="normal")
        self.entry.delete(0, 'end')
        self.entry.focus()
        self.score_label.configure(text="Wynik: 0")
        self.next_word()
        self.update_timer()
        self.apply_difficulty_colors()
        self.protocol("WM_DELETE_WINDOW", self.Clean)

    def Clean(self):
    # Zapisz niedokończoną grę tylko jeśli gra trwa
        if self.timer_running and self.time_left > 0:
            IO.save_saves(
            score=self.score,
            remaining_time=self.time_left,
            nick=self.username,
            difficulty=self.difficulty.get()
            )
        self.destroy()




    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_button.configure(text="Wznów" if self.paused else "Pauza")
        if not self.paused:
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0 and self.timer_running and not self.paused:
            if self.time_left <= 5:
                self.time_label.configure(text=f"Czas: {self.time_left}", text_color="red")
                self.blink_time_label()
            else:
                self.time_label.configure(text=f"Czas: {self.time_left}", text_color="white")

            self.time_left -= 1
            self.after(1000, self.update_timer)
        elif self.time_left <= 0:
            self.end_game()

    def blink_time_label(self):
        current_color = self.time_label.cget("text_color")
        next_color = "red" if current_color == "white" else "white"
        self.time_label.configure(text_color=next_color)
        if 0 < self.time_left <= 5 and self.time_left > 0:
            self.after(500, self.blink_time_label)

    def next_word(self):
        level = self.difficulty.get()
        words = self.passwords.get(level, [])
        available_words = list(set(words) - set(self.used_words))

        if not available_words:
            self.used_words = []
            available_words = words

        self.current_word = random.choice(available_words)
        self.used_words.append(self.current_word)
        self.word_label.configure(text=self.current_word)

    def check_word(self, event=None):
        if not self.timer_running or self.paused:
            return
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
        self.time_label.configure(text="Czas: 0", text_color="red")
        self.save_result()

    def save_result(self):
        result_path = os.path.join(os.path.dirname(__file__), "..", "results.txt")
        with open(result_path, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} | {self.username} | {self.difficulty.get()} | {self.score}\n")

    def update_realtime_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.realtime_clock.configure(text=now)
        self.after(1000, self.update_realtime_clock)