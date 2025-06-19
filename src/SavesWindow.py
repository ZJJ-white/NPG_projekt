import customtkinter as ctk



class SavesWidget(ctk.CTkFrame):
    def __init__(self, text, Saves, *args, width=100, height=32, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.save_name = text
        self.Saves = Saves

        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.DeleteButton = ctk.CTkButton(self, text="x", width=height-3, height=height-3, command=self.DeleteSave, corner_radius=6, fg_color='white', text_color='black', hover_color='red')
        self.DeleteButton.grid(row=0, column=1, padx=(0,3), pady=3)

        self.Save = ctk.CTkLabel(self, text=text, text_color='white', width=width-height, height=height-3, fg_color='black', corner_radius=6)
        self.Save.grid(row=0, column=0, padx=(3,0), pady=3)

    def DeleteSave(self):
        self.Saves.remove(self.save_name)
        self.destroy()

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, title, values, *args, **kwargs):
        super().__init__(*args, label_text=title, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        self.index = len(values)

        for index, widget_text in enumerate(values):
            saves_widget = SavesWidget(text=widget_text, Saves=self.values, master=self)
            saves_widget.grid(row=index, column=0, padx=(5, 5), pady=(10, 0), sticky='w')
            

        


# class AddSaveFrame(ctk.CTkFrame):
    def __init__(self, Saves, ParentFrame, *args, width = 100, height = 32, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.grid_columnconfigure(1,weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.Saves = Saves
        self.ParentFrame = ParentFrame

        self.AddButton = ctk.CTkButton(self, text="+", width=height-3, height=height-3,
                                       command=self.AddSaveCallback, corner_radius=6,
                                       fg_color='white', text_color='black', hover_color='green')
        self.AddButton.grid(row=0, column=1, padx=(0,3), pady=3)

        self.SaveEntry = ctk.CTkEntry(self, text_color='white', height=height-3,
                                      fg_color='black', corner_radius=6, placeholder_text='Wpisz nazwę zapisu')
        self.SaveEntry.grid(row=0, column=0, padx=(3,0), pady=3, sticky='ew')
        self.SaveEntry.bind('<Return>', self.AddSaveCallback)

    def AddSaveCallback(self, event=None):
        text = self.SaveEntry.get()
        self.SaveEntry.delete(0, 'end')
        if (save := text.strip()) == "" or save in self.Saves:
            return None
        
        self.Saves.append(save)
        new_widget = SavesWidget(text=save, Saves=self.Saves, master=self.ParentFrame)
        new_widget.grid(row=len(self.ParentFrame.widgets), column=0, padx=(5, 5), pady=(10, 0), sticky='w')
        self.ParentFrame.widgets.append(new_widget)


class SavesManagerClass(ctk.CTkToplevel):
    def __init__(self, Saves, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Saves = Saves
        self.title("Saves Manager")
        self.geometry("600x600")

        button_width = 200
        button_height = 60

        self.Save0Button = ctk.CTkButton(self, text="Ostatnia gra", width=button_width, height=button_height)
        self.Save0Button.grid(row=0, column=0, padx=20, pady=(40, 10), sticky='ew')
        self.Save1Button = ctk.CTkButton(self, text="Zapis 1", width=button_width, height=button_height)
        self.Save1Button.grid(row=1, column=0, padx=20, pady=10, sticky='ew')
        self.Save2Button = ctk.CTkButton(self, text="Zapis 2", width=button_width, height=button_height)
        self.Save2Button.grid(row=2, column=0, padx=20, pady=10, sticky='ew')
        self.Save3Button = ctk.CTkButton(self, text="Zapis 3", width=button_width, height=button_height)
        self.Save3Button.grid(row=3, column=0, padx=20, pady=10, sticky='ew')

        self.grid_columnconfigure(0, weight=1)
