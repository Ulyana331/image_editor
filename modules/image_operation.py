import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
import requests
import sys
import modules.app as m_app
import modules.path as m_path
from tkinter import Listbox, END
import modules.font as m_font
from io import BytesIO

# Получаем информацию по изображению (формат)
label_info_image = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = "Інформація фотографії:")
label_info_image.place(x = 10, y = 5)
def info_image():
    image_format = image.format
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = "Format: {}".format(image_format))
    label_info.place(x = 10, y = 28)

    # Получаем информацию по изображению (высота и ширина)
    width, height = image.size
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = "width:{} height:{}".format(width, height))
    label_info.place(x = 8, y = 55)

def crop_image():
    global image
    global label_image
    global tk_image
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "")
    label_image.place(x = 20, y = 10)
    image = image.crop((100, 100, 400, 300))
    label_image.destroy()
    tk_image = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 20,y = 10)

def write():
    global image
    global label_image
    global tk_image
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "")
    label_image.place(x = 20, y = 10)
    try:
        image = Image.open("images/img.png")
    except:
        print("Unable to load image")
        sys.exit(1)
    write = text2.get()
    idraw = ImageDraw.Draw(image)
    text = write
    font = ImageFont.truetype("arial.ttf", size=36)
    
    idraw.text((10, 10), text, font=font)
    tk_image = ImageTk.PhotoImage(image)
    label_image.destroy()

    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 5, y = 0)

def rotated():
    global image
    global label_image
    global tk_image
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "")
    label_image.place(x = 20, y = 10)
    try:
        image = Image.open("images/img.png")
    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    image = image.rotate(180, expand = True)
    image.save('images/img.png')
    tk_image = ImageTk.PhotoImage(image)

    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 5, y = 200, anchor = ctk.W)


# функция написания текста на экране
text2 = ctk.StringVar()
entry_write = ctk.CTkEntry(
    master = m_app.app,
    width = 180,
    height = 40,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = text2 
)
entry_write.place(x = 15, y = 165)
label = ctk.CTkLabel(master = m_app.app, text = "Введіть напис:")
label.place(x = 15, y = 135) 

list_url = []

text = ctk.StringVar()
entry = ctk.CTkEntry(
    master = m_app.app,
    width = 180,
    height = 40,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = text
)
entry.place(x = 15, y = 25)
label_url = ctk.CTkLabel(master = m_app.app, text = "Введіть посилання:")
label_url.place(x = 20, y = -5)


count = 1
def download_image():
    global image
    global count
    global label_image
    global url1
    url1 = text.get()
    try:
        req = requests.get(url1, stream = True).raw
        image = Image.open(req)
        list_url.append(url1)
        print(list_url)
    except:
        print("Unable to load image from URL")
    
    try:
        image.save(f"images/img.jpg", "jpeg")
        image_path = ctk.CTkImage(light_image = Image.open(m_path.search_path(f"images/img.jpg")), size = (619,410))        
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = image,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)
        label_image.destroy()
        info_image()
    except:
        image.save(f"images/img.png", "png")
        images_path = ctk.CTkImage(light_image = Image.open(m_path.search_path(f"images/img.png")), size = (619,410))
        
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = images_path,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)
        info_image()

label_filters = ctk.CTkLabel(master = m_app.app.FRAME_LIST_IMAGES, text = "Оберіть фільтр:")
label_filters.place(x=10,y=5)    
def get_selected_value():
    global get_value
    global image
    global label_image
    get_value = listbox.get(listbox.curselection())
    if get_value == values[0]:
        image = Image.open('images/img.png')
        grayscale = image.convert('L')
        image_tk = ImageTk.PhotoImage(grayscale)
        label_image.destroy()
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                                image = image_tk,
                                text = "")
        label_image.place(x = 5, y = 10)
    if get_value == values[1]:
        image = Image.open('images/img.png')
        blurred_img = image.filter(ImageFilter.BLUR)
        tk_image = ImageTk.PhotoImage(blurred_img)
        label_image.destroy()
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = tk_image,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)

    if get_value == values[2]:
        image = Image.open('images/img.png')
        detailed_img = image.filter(ImageFilter.DETAIL)
        tk_image = ImageTk.PhotoImage(detailed_img)
        label_image.destroy()
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = tk_image,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)
    print(get_value)
values = ["Gray", "Blur", "Detail"]
listbox = Listbox(m_app.app.FRAME_LIST_IMAGES, font = m_font.font_list)
for value in values:
    listbox.insert(END, value)
listbox.place(x = 20, y = 15)

entry_width = ctk.IntVar()
entry_w = ctk.CTkEntry(
    master = m_app.app,
    width = 80,
    height = 40,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = entry_width)

entry_w.place(x = 15, y = 95)

entry_height = ctk.IntVar()
entry_H = ctk.CTkEntry(
    master = m_app.app,
    width = 80,
    height = 40,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = entry_height)

entry_H.place(x = 110, y = 95)

label = ctk.CTkLabel(master = m_app.app, text = "Введіть розміри:")
label.place(x = 15, y = 65)

def resize():
    global label_image
    height = entry_height.get()
    width = entry_width.get()
    label_image.destroy()
    image = Image.open("images/img.png")
    resized = image.resize((width, height), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized)
    
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 20, y = 10)
    

# label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "")
# label_image.place(x = 20, y = 10)

current_index = 0
def next_image():
    global current_index
    global label_image
    current_index = (current_index + 1) % len(list_url)
    url = list_url[current_index]
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    tk_image = ImageTk.PhotoImage(image)
    label_image.destroy()
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 0, y = 0)
    
def prev_image():
    global current_index
    global label_image
    current_index = (current_index - 1) % len(list_url)
    url = list_url[current_index]
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    tk_image = ImageTk.PhotoImage(image)
    label_image.destroy()
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 0, y = 0)

label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "")
label_image.place(x = 20, y = 10)

image_height = 619
image_width = 410
class Draw_image(ctk.CTk):
    def __init__(self):
        self.crop_active = False
        self.draw_active = False
        self.max_height = 619
        self.max_width = 410
        self.pencil_size = 2
        self.pencil_color = "red"
        self.current_image_size = (image_height, image_width)
        self.current_resized_image_size = (image.size[0], image.size[1])
        self.lines_drawn = []
        self.image_x_co, self.image_y_co = (self.winfo_screenwidth() / 2) - image_width / 2, (
            self.max_height / 2) - image_height / 2
        self.image = image
        return image
    def draw_crop(self, event):
        if self.crop_active:
            if not self.rectangles:
                self.rectangles.append(self.rect)

            image_width, image_height = self.current_resized_image_size[0], self.current_resized_image_size[1]
            x_co_1, x_co_2 = int((self.winfo_screenwidth() / 2) - image_width/ 2), int(
                (self.winfo_screenwidth() / 2) + image_width / 2)
            y_co_1, y_co_2 = int(self.max_height / 2 - image_height / 2), int((self.max_height / 2) + image_height / 2)

            if x_co_2 > event.x > x_co_1 and y_co_1 + 2 < event.y < y_co_2:
                self.image_canvas.coords(self.rect, self.point_x, self.point_y, event.x, event.y)

                self.event_x, self.event_y = event.x, event.y

            elif self.draw_active:
                image_width, image_height = self.current_resized_image_size[0], self.current_resized_image_size[1]
                x_co_1, x_co_2 = int((self.winfo_screenwidth() / 2) - image_width / 2), int(
                    (self.winfo_screenwidth() / 2) + image_width / 2)
                y_co_1, y_co_2 = int(self.max_height / 2 - image_height / 2), int((self.max_height / 2) + image_height / 2)

                if x_co_2 > self.point_x > x_co_1 and y_co_1 < self.point_y < y_co_2:
                    if x_co_2 > event.x > x_co_1 and y_co_1 < event.y < y_co_2:
                        lines = self.image_canvas.create_line(self.point_x, self.point_y, event.x, event.y,
                                                              fill=self.pencil_color, width = self.pencil_size)
                        
                        x_co_1, y_co_1, x_co_2, y_co2 = ((self.point_x - self.image_x_co) * self.current_image_size[0])/self.current_resized_image_size[0], ((self.point_y - self.image_y_co)*self.current_image_size[1])/self.current_resized_image_size[1], ((event.x - self.image_x_co)*self.current_image_size[0])/self.current_resized_image_size[0], ((event.y - self.image_y_co)*self.current_image_size[1])/self.current_resized_image_size[1]
                        img = ImageDraw.Draw(self.image)
                        img.line([(x_co_1), (x_co_2)], fill = self.pencil_color, width = self.pencil_size + 1)

                        self.lines_drawn.append(lines)
                        self.point_x, self.point_y = event.x, event.y
    def get_mouse_pos(self, event):
        if not self.draw_active and self.crop_active:
            if self.rect:
                self.rectangles = []
                self.image_canvas.delete(self.rect)

            self.rect = self.image_canvas.create_rectangle(0,0,0,0, outline="black", width=3)

        self.point_x, self.point_y = event.x, event.y

        self.image_canvas = ctk.CTkCanvas(self, bd=0, highlightbackground = "black", background = "black")       
        self.image_canvas.bind('<B1-Motion>', self.draw_crop)
        self.image_canvas.bind("<ButtonPress-1>", self.get_mouse_pos)
        self.image_canvas.pack(fill="both", expand=True)
drawing = Draw_image()