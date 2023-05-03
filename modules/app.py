import customtkinter as ctk
from PIL import Image
import requests
import sys
import modules.frame as m_frame
class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("image editor")
        self.FRAME_LIST_IMAGES = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 173, 
                                                  height = 238,
                                                  border_width = 5,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#E8900C",
                                                  corner_radius = 15)
        self.FRAME_LIST_IMAGES.place(x = 20, y = 20)
        self.FRAME_INFO_IMAGE = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 173, 
                                                  height = 154,
                                                  border_width = 5,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#E8900C",
                                                  corner_radius = 15)
        self.FRAME_INFO_IMAGE.place(x = 20, y = 271)
        self.FRAME_IMAGE = m_frame.My_Frame(text = "", 
                                                  master = self,
                                                  width = 619, 
                                                  height = 405,
                                                  border_width = 5,
                                                  fg_color = "#1E1E1E",
                                                  border_color = "#E8900C",
                                                  corner_radius = 15)
        self.FRAME_IMAGE.place(x = 210, y = 20)

# url = 'https://i.ytimg.com/vi/vEYsdh6uiS4/maxresdefault.jpg'
 
# try:
#     resp = requests.get(url, stream=True).raw
# except requests.exceptions.RequestException as e:  
#     sys.exit(1)
 
# try:
#     img = Image.open(resp)
# except IOError:
#     print("Unable to open image")
#     sys.exit(1)
 
# img.save('sid.jpg', 'jpeg')

app = App(850, 500)