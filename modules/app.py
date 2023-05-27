import customtkinter as ctk
import modules.frame as m_frame
from PIL import ImageTk
class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("Редактор зображень")
        self.wm_iconbitmap('images/icon.ico')
        self.FRAME_INFO_IMAGE = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 175, 
                                                  height = 90,
                                                  border_width = 5,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#E8900C",
                                                  corner_radius = 15)
        self.FRAME_INFO_IMAGE.place(x = 20, y = 480)
        self.FRAME_IMAGE = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 860, 
                                                  height = 580,
                                                  border_width = 0,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#1E1E1E",
                                                  corner_radius = 15)
        self.FRAME_IMAGE.place(x = 570, y = 10)

app = App(1450, 840)
