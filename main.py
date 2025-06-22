import customtkinter as ctk
import src.PasswordsManager as PM
import src.IO as IO
import src.StatsManager as SM
import src.ChallengeMode as CM
import src.LearningMode as LM
import tkinter.messagebox as mbox

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
        
        self.Statistics = IO.load_stats()    
        self.StatisticsManagerWindow = None
        self.StatisticsManagerButton = ctk.CTkButton(self, text='Statystyki', command=self.OpenStatisticsManager)
        self.StatisticsManagerButton.pack(side='top', padx=20, pady=20)
    
        self.Saves = IO.load_saves()
        self.SavesWindow = None
        self.SavesWindowButton = ctk.CTkButton(self, text='Wczytaj ostatnią grę', command=self.OpenSavesWindow)
        self.SavesWindowButton.pack(side='top', padx=20, pady=20)
        
        self.LearningModeWindow = None
        self.LearningModeButton = ctk.CTkButton(self, text='Tryb Nauki', command=self.OpenLearningMode)
        self.LearningModeButton.pack(side='top', padx=20, pady=20)

        self.ChallengeModeWindow = None
        self.ChallengeModeButton = ctk.CTkButton(self, text='Tryb Wyzwań', command=self.OpenChallengeMode)
        self.ChallengeModeButton.pack(side='top', padx=20, pady=20)

    def OpenPasswordManager(self):                                                                                               
        if self.PasswordManagerWindow is None or not self.PasswordManagerWindow.winfo_exists():                                  
            self.iconify()
            self.PasswordManagerWindow = PM.PasswordManagerClass(self.Passwords)
            self.PasswordManagerWindow.protocol("WM_DELETE_WINDOW", lambda: (self.PasswordManagerWindow.destroy(), self.deiconify()))                                                 
        else:                                                                                                                    
            self.PasswordManagerWindow.focus()  
        
    def OpenStatisticsManager(self):                                                                                               
        if self.StatisticsManagerWindow is None or not self.StatisticsManagerWindow.winfo_exists():                                 
            self.iconify()
            self.StatisticsManagerWindow = SM.StatisticsManagerClass(self.Statistics)
            self.StatisticsManagerWindow.protocol("WM_DELETE_WINDOW", lambda: (self.StatisticsManagerWindow.destroy(), self.deiconify()))                                                 
        else:                                                                                                                    
            self.StatisticsManagerWindow.focus()    
    
    def OpenChallengeMode(self):
        if self.ChallengeModeWindow is None or not self.ChallengeModeWindow.winfo_exists():
            self.iconify()
            self.ChallengeModeWindow = CM.ChallengeModeWindow(self.Passwords)
            self.ChallengeModeWindow.protocol("WM_DELETE_WINDOW", lambda: (self.ChallengeModeWindow.destroy(), self.deiconify()))
        else:
            self.ChallengeModeWindow.focus()

    def OpenLearningMode(self):
        if self.LearningModeWindow is None or not self.LearningModeWindow.winfo_exists():
            self.iconify()
            self.LearningModeWindow = LM.LearningModeClass(self.Passwords)
            self.LearningModeWindow.protocol("WM_DELETE_WINDOW", lambda: (self.LearningModeWindow.destroy(), self.deiconify()))
        else:
            self.LearningModeWindow.focus()

    def OpenSavesWindow(self):
        if not self.Saves:
            mbox.showinfo("Brak zapisów", "Nie znaleziono żadnych zapisów gry.")
        else:
            last_save = self.Saves[0]
            self.iconify() # minimalizacja menu
            window=CM.ChallengeModeWindow(self.Passwords, last_save['score'], last_save['remaining_time'], last_save['nick'], last_save['difficulty'], master=self)
            IO.remove_saves(0)
            window.protocol("WM_DELETE_WINDOW", lambda: (window.destroy(), self.deiconify())) # przywraca menu 
    
    def Cleanup(self):
        IO.save_passwords(self.Passwords)   
        IO.save_stats(self.Statistics)
        self.destroy()                      

if __name__ == '__main__':
    app = App()
    app.mainloop()