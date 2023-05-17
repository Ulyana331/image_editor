import customtkinter as ctk
import modules.frame as m_frame
from PIL import Image, ImageDraw
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
        self.FRAME_LIST_IMAGES = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 173, 
                                                  height = 100,
                                                  border_width = 5,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#E8900C",
                                                  corner_radius = 15)
        self.FRAME_LIST_IMAGES.place(x = 20, y = 215)
        self.FRAME_INFO_IMAGE = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 173, 
                                                  height = 90,
                                                  border_width = 5,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#E8900C",
                                                  corner_radius = 15)
        self.FRAME_INFO_IMAGE.place(x = 20, y = 330)
        self.FRAME_IMAGE = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 619, 
                                                  height = 405,
                                                  border_width = 0,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#1E1E1E",
                                                  corner_radius = 15)
        self.FRAME_IMAGE.place(x = 210, y = 20)

        self.canvas = ctk.CTkCanvas(self, width=200, height=100, bg = "#1E1E1E")
        self.canvas.place(x=375, y=45)

        self.canvas.bind("<ButtonPress-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.start_x = None
        self.start_y = None
        self.drawing = False

    def start_drawing(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.drawing = True

    def draw(self, event):
        if self.drawing:
            current_x = event.x
            current_y = event.y
            self.canvas.create_line(self.start_x, self.start_y, current_x, current_y, fill="white")
            self.start_x = current_x
            self.start_y = current_y

    def stop_drawing(self, event):
        self.drawing = False
        
app = App(850, 500)