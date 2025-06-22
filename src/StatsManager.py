import customtkinter as ctk
import src.IO as IO

class StatisticsWidget(ctk.CTkFrame):
    def __init__(self, text, Statistics, *args, width = 100, height = 32, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.statistics_name = text
        self.Statistics = Statistics

        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

    
        self.label = ctk.CTkLabel(self, text=text, text_color='white', width=width-height, height=height-3, fg_color='black', corner_radius=6)
        self.label.grid(row=0, column=0, padx=(3,0), pady=3)

    def delete_self(self):
        if self.statistics_name in self.Statistics:
            self.Statistics.remove(self.statistics_name)
        self.destroy()      

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, title, values, *args, **kwargs):
        super().__init__(*args, label_text=title, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        # self.index = len(values)
        self.values = values
        self.widgets = []

        # for index, widget_text in enumerate(values):
        #     statistics_widget = StatisticsWidget(text=widget_text, Statistics=self.values, master=self)
        #     statistics_widget.grid(row=index, column=0, padx=(5, 5), pady=(10, 0), sticky='w')
        #     self.widgets.append(statistics_widget)
        # zmiany:
        def extract_score(text):
            try:
                return int(text.split("|")[-1].strip())
            except ValueError:
                return -1

        self.values.sort(key=extract_score, reverse=True)

        for index, widget_text in enumerate(values):
            statistics_widget = StatisticsWidget(text=widget_text, Statistics=self.values, master=self)
            statistics_widget.grid(row=index, column=0, padx=(5, 5), pady=(10, 0), sticky='w')
            self.widgets.append(statistics_widget)


        self.delete_button = ctk.CTkButton(self, text="Resetuj Statystyki", command=self.delete_statistics_all,
                                           fg_color='white', text_color='black', hover_color='red')
        self.delete_button.grid(row=len(values), column=0, padx=5, pady=10, sticky='ew')

    def delete_statistics_all(self):
        for widget in self.widgets:
            widget.delete_self()
        self.widgets.clear()
        

class StatisticsManagerClass(ctk.CTkToplevel):
        def __init__(self, Statistics_data):
            super().__init__()
            self.Statistics_data = Statistics_data
            self.geometry("600x500")
            self.resizable(True, True)
            
            self.grid_columnconfigure((0,1,2), weight=1)
            self.grid_rowconfigure(0, weight=1)

            #wyświetlanie statystyki
            self.Stat1Frame = ScrollableFrame(title='Łatwe', values=Statistics_data['Easy'],master=self, fg_color='red')
            self.Stat1Frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
            
            self.Stat2Frame = ScrollableFrame(title='Średnie', values=Statistics_data['Medium'],master=self, fg_color='blue')
            self.Stat2Frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

            self.Stat3Frame = ScrollableFrame(title='Trudne', values=Statistics_data['Hard'],master=self, fg_color='green')
            self.Stat3Frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
            
            
            #przyciski do zapisywania i usuwania statystyk

            self.ButtonFrame = ctk.CTkFrame(self, fg_color='transparent')
            self.ButtonFrame.grid(row=1, column=0, columnspan=3, pady=10)
            self.ButtonFrame.grid_columnconfigure((0, 1), weight=1)

            self.SaveButton = ctk.CTkButton(self.ButtonFrame, text="Zapisz zmiany", command=self.save_all_statistics,
                                        fg_color='green', text_color='white', hover_color='darkgreen')
            self.SaveButton.grid(row=0, column=0, padx=20, pady=10, sticky='e')

            self.DeleteAllButton = ctk.CTkButton(self.ButtonFrame, text="Usuń wszystkie statystyki",
                                             command=self.delete_all_statistics,
                                             fg_color='red', text_color='white', hover_color='darkred')
            self.DeleteAllButton.grid(row=0, column=1, padx=20, pady=10, sticky='w') 

        def save_all_statistics(self):
            IO.save_stats(self.Statistics_data)

        def delete_all_statistics(self):
            self.Stat1Frame.delete_statistics_all()
            self.Stat2Frame.delete_statistics_all()
            self.Stat3Frame.delete_statistics_all()