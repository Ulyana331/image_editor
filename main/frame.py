import customtkinter as ctk
import modules.app as app

class My_Frame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, fg_color, 
                 border_color, corner_radius, **kwargs):
        super().__init__(master = master,width= width, height= height, border_width = border_width, 
                fg_color = fg_color, border_color = border_color, corner_radius = corner_radius, **kwargs)