import customtkinter as ctk

class PasswordWidget(ctk.CTkFrame):
    def __init__(self, *args, width = 100, height = 32, text = None, PasswordsArray = None, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.password_name = text
        self.PasswordsArray = PasswordsArray

        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.DeleteButton = ctk.CTkButton(self, text="x", width=height-3, height=height-3, command=self.DeletePassword, corner_radius=6, fg_color='white', text_color='black')
        self.DeleteButton.grid(row=0, column=1, padx=(0,3), pady=3)

        self.Password = ctk.CTkLabel(self, text=text, text_color='white', width=width-height, height=height-3, fg_color='black', corner_radius=6)
        self.Password.grid(row=0, column=0, padx=(3,0), pady=3)

    def DeletePassword(self):
        self.PasswordsArray.remove(self.password_name)
        self.destroy()

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, *args, master=None, title=None, values=None, **kwargs):
        super().__init__(*args,master=master, label_text=title, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)

        for index, widget in enumerate(values):
            password_widget = PasswordWidget(master=self,text=widget, PasswordsArray=values)
            password_widget.grid(row=index, column=0, padx=(5,5), pady=(10,0), sticky='w')

class PasswordManagerClass(ctk.CTkToplevel):
        def __init__(self, HardsPasswords, MediumPasswords, EasyPasswords):
            super().__init__()
            self.geometry("600x500")
            self.resizable(True, True)
            
            self.grid_columnconfigure((0,1,2), weight=1)
            self.grid_rowconfigure(0, weight=1)

            self.HardPasswordsFrame = ScrollableFrame(master=self, title='Hasła Trudne', values=HardsPasswords, fg_color='red')
            self.HardPasswordsFrame.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky='nsew')

            self.MediumPasswordsFrame = ScrollableFrame(master=self, title='Hasła Średnie', values=MediumPasswords, fg_color='#efeb00')
            self.MediumPasswordsFrame.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky='nsew')

            self.EasyPasswordsFrame = ScrollableFrame(master=self, title='Hasła Łatwe', values=EasyPasswords, fg_color='#24c707')
            self.EasyPasswordsFrame.grid(row=0, column=2, padx=(10,10), pady=(10,10), sticky='nsew')