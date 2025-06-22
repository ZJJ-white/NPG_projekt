import customtkinter as ctk
import src.IO as IO
import src.StatsManager as SM
        
class StatisticsChoiceClass(ctk.CTkToplevel):
        def __init__(self,*args, **kwargs):
            super().__init__()
            self.Statistics = IO.load_stats()
            self.geometry("600x500")
            self.resizable(True, True)
            
            self.grid_columnconfigure((0,1,2), weight=1)
            self.grid_rowconfigure(0, weight=1)

            #przyciski do wyboru okna statystyk

            self.ButtonFrame = ctk.CTkFrame(self, fg_color='transparent')
            self.ButtonFrame.grid(row=1, column=0, columnspan=3, pady=10)
            self.ButtonFrame.grid_columnconfigure((0, 1), weight=1)

            self.GeneralStatButton = ctk.CTkButton(self.ButtonFrame, text="Ogólne statystyki", command=self.OpenStatisticsManager,
                                        fg_color='green', text_color='white', hover_color='darkgreen')
            self.GeneralStatButton.grid(row=0, column=0, padx=20, pady=10, sticky='e')

            self.LastGameStatsButton = ctk.CTkButton(self.ButtonFrame, text="Statystyki ostatniej gry",
                                             command=None,
                                             fg_color='Yellow', text_color='white', hover_color='darkorange')
            self.LastGameStatsButton.grid(row=0, column=1, padx=20, pady=10, sticky='w') 

        def OpenStatisticsManager(self):                                                                                               #\
            if  self.StatisticsManagerWindow is None or not self.StatisticsManagerWindow.winfo_exists():                                  #| Tworzy okno Zarządzania Hasłami
                self.StatisticsManagerWindow = SM.StatisticsManagerClass(self.Statistics)                                                 #| Jak już istnieje to je tylko zoomuje (.focus())
            else:                                                                                                                    #|
                self.StatisticsManagerWindow.focus() 