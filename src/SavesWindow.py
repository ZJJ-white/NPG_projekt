import customtkinter as ctk
import src.ChallengeMode
import src.IO 




class SavesManagerClass(ctk.CTkToplevel):
    def __init__(self, Saves, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Saves = Saves
        self.title("Saves Manager")
        self.geometry("600x600")


        self.load_saves()
        self.build_ui()
        self.grid_columnconfigure(0, weight=1)
    
    def OpenSavesWindow(self):
        if self.SavesWindow is None or not self.SavesWindow.winfo_exists():
            self.SavesWindow = SavesManagerClass(self.Saves)
        else:
            self.SavesWindow.focus()
