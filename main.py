import customtkinter as ctk
import src.PasswordsManager as PM
import src.IO as IO
import src.ChallengeMode as CM

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.resizable(True, True)

        self.protocol("WM_DELETE_WINDOW", self.Cleanup)
        ctk.set_appearance_mode('dark')

        self.Passwords = IO.load_passwords()

        self.PasswordManagerWindow = None
        self.PasswordManagerButton = ctk.CTkButton(self, text='Zarządzaj hasłami', command=self.OpenPasswordManager)
        self.PasswordManagerButton.pack(side='top', padx=20, pady=20)

        self.ChallengeModeButton = ctk.CTkButton(self, text='Tryb Challenge', command=self.OpenChallengeMode)
        self.ChallengeModeButton.pack(side='top', padx=20, pady=10)

        self.ScoreboardButton = ctk.CTkButton(self, text='Tablica Rekordów', command=self.OpenScoreboard)
        self.ScoreboardButton.pack(side='top', padx=20, pady=10)

    def OpenPasswordManager(self):
        if self.PasswordManagerWindow is None or not self.PasswordManagerWindow.winfo_exists():
            self.PasswordManagerWindow = PM.PasswordManagerClass(self.Passwords)
        else:
            self.PasswordManagerWindow.focus()

    def OpenChallengeMode(self):
        CM.ChallengeModeWindow(self.Passwords)

    def OpenScoreboard(self):
        CM.ScoreboardWindow()

    def Cleanup(self):
        IO.save_passwords(self.Passwords)
        self.destroy()

if __name__ == '__main__':
    app = App()
    app.mainloop()