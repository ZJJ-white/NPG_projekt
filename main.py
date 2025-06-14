import customtkinter as ctk
import src.PasswordsManager as PM
import src.IO as IO
import src.StatsManager as SM
import src.LearningMode as LM
import src.ChallengeMode as CM

class App(ctk.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.resizable(True, True)

        self.protocol("WM_DELETE_WINDOW", self.Cleanup)
        ctk.set_appearance_mode('dark')
        self.Passwords = IO.load_passwords()
       

        # Zarządzanie hasłami
        self.PasswordManagerWindow = None
        self.PasswordManagerButton = ctk.CTkButton(self, text='Zarządzaj hasłami', command=self.OpenPasswordManager)
        self.PasswordManagerButton.pack(side='top', padx=20, pady=20)

        # Tryb Nauki
        self.LearningModeWindow = None
        self.LearningModeButton = ctk.CTkButton(self, text='Tryb Nauki', command=self.OpenLearningMode)
        self.LearningModeButton.pack(side='top', padx=40, pady=20)

        # Tryb Wyzwań
        self.ChallengeModeWindow = None
        self.ChallengeModeButton = ctk.CTkButton(self, text='Tryb Wyzwań', command=self.OpenChallengeMode)
        self.ChallengeModeButton.pack(side='top', padx=40, pady=20)

    def OpenPasswordManager(self):
        if self.PasswordManagerWindow is None or not self.PasswordManagerWindow.winfo_exists():
            self.PasswordManagerWindow = PM.PasswordManagerClass(self.Passwords)
        else:
            self.PasswordManagerWindow.focus()

    def OpenLearningMode(self):
        if self.LearningModeWindow is None or not self.LearningModeWindow.winfo_exists():
            self.LearningModeWindow = LM.LearningModeClass(self.Passwords)
        else:
            self.LearningModeWindow.focus()

    def OpenChallengeMode(self):
        if self.ChallengeModeWindow is None or not self.ChallengeModeWindow.winfo_exists():
            self.ChallengeModeWindow = CM.ChallengeModeClass(self.Passwords)
        else:
            self.ChallengeModeWindow.focus()

    def Cleanup(self):
        IO.save_passwords(self.Passwords)
        self.destroy()

if __name__ == '__main__':
    app = App()
    app.mainloop()