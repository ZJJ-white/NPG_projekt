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

class AddPassword(ctk.CTkFrame):
    def __init__(self, Passwords, ParentFrame, *args, width = 100, height = 32, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.grid_columnconfigure(1,weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.Passwords = Passwords
        self.ParentFrame = ParentFrame

        self.AddButton = ctk.CTkButton(self, text="+", width=height-3, height=height-3, command=self.AddPasswordCallback, corner_radius=6, fg_color='white', text_color='black', hover_color='green')
        self.AddButton.grid(row=0, column=1, padx=(0,3), pady=3)

        self.PasswordEntry = ctk.CTkEntry(self, text_color='white', height=height-3, fg_color='black', corner_radius=6, placeholder_text='Wpisz hasło')
        self.PasswordEntry.grid(row=0, column=0, padx=(3,0), pady=3, sticky='ew')
        self.PasswordEntry.bind('<Return>', command=self.AddPasswordCallback)

    def AddPasswordCallback(self, event=None):
        text = self.PasswordEntry.get()
        self.PasswordEntry.delete(0, 'end')
        if (password := text.strip()) == "" or password in self.Passwords:
            return None
        
        self.Passwords.append(password)
        NewPasswordWidget = PasswordWidget(password, self.Passwords, master=self.ParentFrame)
        NewPasswordWidget.grid(row=len(self.Passwords) - 1, column=0, padx=(5,5), pady=(10,0), sticky='w')
        
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

            self.HardPasswordAddButton = AddPassword(Passwords['Hard'], self.HardPasswordsFrame, master=self)
            self.HardPasswordAddButton.grid(row=1, column=0, sticky='ew', padx=(5,5), pady=(10,0))
            
            self.MediumPasswordAddButton = AddPassword(Passwords['Medium'], self.MediumPasswordsFrame, master=self)
            self.MediumPasswordAddButton.grid(row=1, column=1, sticky='ew', padx=(5,5), pady=(10,0))

            self.EasyPasswordAddButton = AddPassword(Passwords['Easy'], self.EasyPasswordsFrame, master=self)
            self.EasyPasswordAddButton.grid(row=1, column=2, sticky='ew', padx=(5,5), pady=(10,0))