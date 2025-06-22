import customtkinter as ctk
import random

class LearningModeClass(ctk.CTkToplevel):
    def __init__(self, Passwords):
        super().__init__()
        self.title("Tryb Nauki")
        self.geometry("400x400")

        self.passwords = Passwords
        self.selected_password = ""
        self.selected_difficulty = None
        self.active_passwords = []

        self.start_widgets()

    def start_widgets(self):
        self.select_label = ctk.CTkLabel(self, text="Wybierz poziom trudności:", font=("Arial", 16))
        self.select_label.pack(pady=20)

        self.easy_button = ctk.CTkButton(self, text="Łatwe", command=lambda: self.start_learning("Easy"))
        self.easy_button.pack(pady=5)

        self.medium_button = ctk.CTkButton(self, text="Średnie", command=lambda: self.start_learning("Medium"))
        self.medium_button.pack(pady=5)

        self.hard_button = ctk.CTkButton(self, text="Trudne", command=lambda: self.start_learning("Hard"))
        self.hard_button.pack(pady=5)

        self.mixed_button = ctk.CTkButton(self, text="Mieszane", command=lambda: self.start_learning("Mixed"))
        self.mixed_button.pack(pady=5)

    def start_learning(self, difficulty):
        self.selected_difficulty = difficulty

        # Ukryj przyciski wyboru
        self.select_label.pack_forget()
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.mixed_button.pack_forget()

        # Przygotuj listę haseł
        if difficulty == "Mixed":
            self.active_passwords = self.passwords['Easy'] + self.passwords['Medium'] + self.passwords['Hard']
        else:
            self.active_passwords = self.passwords[difficulty]

        if not self.active_passwords:
            error_label = ctk.CTkLabel(self, text="Brak haseł w tym poziomie!", text_color="red")
            error_label.pack(pady=20)
            return

        self.learning_interface()

    def learning_interface(self):
        self.selected_password = self.get_random_password()

        self.label = ctk.CTkLabel(self, text="Przepisz poniższe hasło:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.password_display = ctk.CTkLabel(self, text=self.selected_password, font=("Arial", 18, "bold"), text_color="white")
        self.password_display.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Wpisz hasło tutaj", width=300)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_password)

        self.feedback_label = ctk.CTkLabel(self, text="")
        self.feedback_label.pack(pady=10)

        self.check_button = ctk.CTkButton(self, text="Sprawdź", command=self.check_password)
        self.check_button.pack(pady=10)

    def get_random_password(self):
        return random.choice(self.active_passwords)

    def check_password(self, event=None):
        user_input = self.entry.get()
        if user_input == self.selected_password:
            self.feedback_label.configure(text="✅ Poprawnie!", text_color="green")
            self.entry.delete(0, 'end')
            self.after(1000, self.load_new_password)
        else:
            self.feedback_label.configure(text="❌ Spróbuj ponownie.", text_color="red")

    def load_new_password(self):
        self.selected_password = self.get_random_password()
        self.password_display.configure(text=self.selected_password)
        self.feedback_label.configure(text="")