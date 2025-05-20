import customtkinter as ctk

class PasswordWidget(ctk.CTkFrame):
    def __init__(self, text, Passwords, *args, width = 100, height = 32, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.password_name = text
        self.Passwords = Passwords

        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.DeleteButton = ctk.CTkButton(self, text="x", width=height-3, height=height-3, command=self.DeletePassword, corner_radius=6, fg_color='white', text_color='black', hover_color='red')
        self.DeleteButton.grid(row=0, column=1, padx=(0,3), pady=3)

        self.Password = ctk.CTkLabel(self, text=text, text_color='white', width=width-height, height=height-3, fg_color='black', corner_radius=6)
        self.Password.grid(row=0, column=0, padx=(3,0), pady=3)

    def DeletePassword(self):
        self.Passwords.remove(self.password_name)
        self.destroy()

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, title, values, *args, **kwargs):
        super().__init__(*args, label_text=title, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)

        for index, widget in enumerate(values):
            password_widget = PasswordWidget(text=widget, Passwords=values, master=self)
            password_widget.grid(row=index, column=0, padx=(5,5), pady=(10,0), sticky='w')

class PasswordManagerClass(ctk.CTkToplevel):
        def __init__(self, Passwords):
            super().__init__()
            self.geometry("600x500")
            self.resizable(True, True)
            
            self.grid_columnconfigure((0,1,2), weight=1)
            self.grid_rowconfigure(0, weight=1)

            self.HardPasswordsFrame = ScrollableFrame(title='Hasła Trudne', values=Passwords['Hard'],master=self, fg_color='red')
            self.HardPasswordsFrame.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky='nsew')

            self.MediumPasswordsFrame = ScrollableFrame(title='Hasła Średnie', values=Passwords['Medium'],master=self, fg_color='#efeb00')
            self.MediumPasswordsFrame.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky='nsew')

            self.EasyPasswordsFrame = ScrollableFrame(title='Hasła Łatwe', values=Passwords['Easy'],master=self, fg_color='#24c707')
            self.EasyPasswordsFrame.grid(row=0, column=2, padx=(10,10), pady=(10,10), sticky='nsew')