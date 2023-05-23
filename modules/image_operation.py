import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
import requests
import sys
import modules.app as m_app
import modules.path as m_path
from tkinter import Listbox, END
import modules.font as m_font
from io import BytesIO
import os

# Получаем информацию по изображению (формат)
label_information = ctk.CTkLabel(master = m_app.app, font = m_font.font_label, text = "Інформація фотографіЇ:")
label_information.place(x = 15, y = 440)
label_information = ctk.CTkLabel(master = m_app.app, font = m_font.font_label, text = "Список зображень:")
label_information.place(x = 15, y = 600)
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
    image = Image.open("images/img.jpg")
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0,0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    rotated_image = image.rotate(180)

    rotated_image.save("images/rotated_img.png")
    image_r = Image.open("images/rotated_img.png")
    image = image_r.resize((1500, 900))
    tk_image_r = ImageTk.PhotoImage(image_r)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0,0, anchor = "nw", image = tk_image_r)
    canvas.place(x = 0, y = 0)
    canvas.itemconfig(canvas, image = ImageTk.PhotoImage(rotated_image))

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
entry_write.place(x = 15, y = 230)
label = ctk.CTkLabel(master = m_app.app, text = "Введіть напис:", font = m_font.font_label)
label.place(x = 15, y = 190) 

list_url = []

text = ctk.StringVar()
entry = ctk.CTkEntry(
    master = m_app.app,
    width = 400,
    height = 40,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = text
)
entry.place(x = 15, y = 40)
label_url = ctk.CTkLabel(master = m_app.app, text = "Введіть посилання:", font = m_font.font_label)
label_url.place(x = 20, y = 5)



count = 1
def download_image():
    global canvas
    global url1
    global count
    url1 = text.get()
    try:
        req = requests.get(url1, stream = True).raw
        image = Image.open(req)
        list_url.append(url1)
        print(list_url)
    except:
        print("Unable to load image from URL")

    image.save(f"images/original_image.jpg")
    image = image.resize((1500,900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)
    count += 1
    canvas.data = {}
    def start_drawing(event):
        canvas.data["line_start"] = (event.x, event.y)
    def draw_stick(event):
        if "line_start" in canvas.data:
            start = canvas.data["line_start"]
            end = (event.x, event.y)
            canvas.create_line(start[0], start[1], end[0], end[1], fill = "red", width = 5, tags = "drawing")
            canvas.data["line_start"] = end
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", draw_stick)
    canvas.bind("<ButtonRelease-1>", lambda event: canvas.data.pop("line_start", None))

    image.save(f"images/img{count}.jpg","jpeg")
    count += 1
    list_name_image = []
    list_name_image.append(f"images/img{count}.jpg")
    # print(list_name_image)
    # list_box_images = Listbox(m_app.app, bg = "#1E1E1E", fg = "white")
    # for i in list_name_image:
    #     list_box_images.insert(END,i)
    # list_box_images.place(x = 15, y = 700)
    info_image()

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
listbox = Listbox(m_app.app, font = m_font.font_list, bg = "#1E1E1E", fg = "white", height= 5, width= 10)
for value in values:
    listbox.insert(END, value)
listbox.place(x = 20, y = 570)

entry_width = ctk.IntVar()
entry_w = ctk.CTkEntry(
    master = m_app.app,
    width = 120,
    height = 50,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = entry_width)

entry_w.place(x = 20, y = 135)

entry_height = ctk.IntVar()
entry_H = ctk.CTkEntry(
    master = m_app.app,
    width = 120,
    height = 50,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",  
    textvariable = entry_height)

entry_H.place(x = 155, y = 135)

label = ctk.CTkLabel(master = m_app.app, text = "Введіть розміри:", font = m_font.font_label)
label.place(x = 15, y = 95)

def resize():
    height = entry_height.get()
    width = entry_width.get()
    image = Image.open("images/img.jpg")
    image = image.resize((1500, 900))
    tk_image1 = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0,0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    resized = image.resize((width, height), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized)

    image = Image.open("images/img.jpg")
    image1 = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image1)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0,0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)
    
    

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

label_filters = ctk.CTkLabel(master = m_app.app, text = "Оберіть фільтр:", font = m_font.font_label)
label_filters.place(x=10,y=280)    

def clear_frame():
    buttons = [widget for widget in m_app.app.FRAME_IMAGE.winfo_children() if isinstance(widget,ctk.CTkButton)]
    for widget in m_app.app.FRAME_IMAGE.winfo_children():
        if widget not in buttons:
            widget.destroy()
def clear_drawing():
    canvas.delete("drawing")