import customtkinter as ctk
import src.PasswordsManager as PM
import src.IO as IO
import src.ChallengeMode as CM
import tkinter.messagebox as mbox


class App(ctk.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.resizable(True, True)

        self.protocol("WM_DELETE_WINDOW", self.Cleanup)       #|  
        ctk.set_appearance_mode('dark')                       #| Przygotowanie aplikacji, tj. wczytanie danych i zapisanie do atrybutów   
        self.Passwords = IO.load_passwords()                  #| Ten protocol sprawia, że przy zamykaniu wywołam cleanup, czyli zapis do plików haseł i statystyk                  
                                     
        self.PasswordManagerWindow = None
        self.PasswordManagerButton = ctk.CTkButton(self, text='Zarządzaj hasłami', command=self.OpenPasswordManager)
        self.PasswordManagerButton.pack(side='top', padx=20, pady=20)

        self.Saves = IO.load_saves()

        
        self.SavesWindow = ctk.CTkButton(self, text='Wczytaj ostatnią grę', command=self.OpenSavesWindow)
        self.SavesWindow.pack(side='top', padx=20, pady=20)
        self.SavesWindow = None

        self.ChallengeModeButton = ctk.CTkButton(self, text='Tryb Challenge', command=self.OpenChallengeMode)
        self.ChallengeModeButton.pack(side='top', padx=20, pady=10)


    def OpenPasswordManager(self):                                                                                               #\
        if self.PasswordManagerWindow is None or not self.PasswordManagerWindow.winfo_exists():                                  #| Tworzy okno Zarządzania Hasłami
            self.PasswordManagerWindow = PM.PasswordManagerClass(self.Passwords)                                                 #| Jak już istnieje to je tylko zoomuje (.focus())
        else:                                                                                                                    #|
            self.PasswordManagerWindow.focus()                                                                                   #/

    def Cleanup(self):
        IO.save_passwords(self.Passwords)   
        self.destroy()                      


    def OpenSavesWindow(self):
        saves = IO.load_saves()
        if not saves:
            mbox.showinfo("Brak zapisów", "Nie znaleziono żadnych zapisów gry.")
        else:
            last_save = saves[0]
            self.iconify() # minimalizacja menu
            window=CM.ChallengeModeWindow(self.Passwords, last_save['score'], last_save['remaining_time'], last_save['nick'], last_save['difficulty'], master=self)
            window.loaded_from_save = True # t
            IO.remove_saves(0)
            window.protocol("WM_DELETE_WINDOW", lambda: (window.destroy(), self.deiconify())) # przywraca menu 

    def OpenChallengeMode(self):
        self.iconify()
        window = CM.ChallengeModeWindow(self.Passwords,master=self)
        window.protocol("WM_DELETE_WINDOW", lambda: (window.destroy(), self.deiconify()))
    
        

if __name__ == '__main__':
    app = App()
    app.mainloop()