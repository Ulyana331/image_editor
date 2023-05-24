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

def info_image(canvas, image_id):
    image_format = image.format
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = "Format: {}".format(image_format))
    label_info.place(x = 10, y = 28)

    # Получаем информацию по изображению (высота и ширина)
    width, height = image.size
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = "width:{} height:{}".format(width, height))
    label_info.place(x = 8, y = 55)


def crop_image():
    image = Image.open("images/original_image.jpg")
    image = image.resize((1500,900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_c = image.crop((100, 100, 400, 300))

    tk_image_c = ImageTk.PhotoImage(image_c)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_c)
    canvas.place(x = 0, y = 0)
    image_c.save("iamges/cropped_image.jpg")


def write():
    image = Image.open("images/original_image.jpg")
    image = image.resize((1500,900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    write = text2.get()
    
    image_c = canvas.create_text(100, 100, text=write, font=("Arial", 36), fill="white", tags = "written")
    tk_image_c = ImageTk.PhotoImage(image_c)
    tk_image_c.save("images/written_image.jpg")

    image_w = Image.open("images/written_image.jpg")
    tk_image_w = ImageTk.PhotoImage(image_w)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_w)
    canvas.place(x = 0, y = 0)
    image_w = Image.open("images/written_image_2.jpg")



def rotated():
    image = Image.open("images/original_image.jpg")
    image = image.resize((1500,900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_r = image.rotate(180)

    tk_image_r = ImageTk.PhotoImage(image_r)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_r)
    canvas.place(x = 0, y = 0)
    image_r.save("images/rotated_image.jpg")

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

    info_image()

def get_selected_value():
    global get_value
    global image
    global label_image
    get_value = listbox.get(listbox.curselection())
    if get_value == values[0]:
        image = Image.open('images/original_image.jpg')
        image = image.resize((1500,900))
        tk_image = ImageTk.PhotoImage(image)
        canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
        canvas.create_image(0, 0, anchor = "nw", image = tk_image)
        canvas.place(x = 0, y = 0)

        image_g = image.convert('L')

        tk_image_g = ImageTk.PhotoImage(image_g)
        canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
        canvas.create_image(0, 0, anchor = "nw", image = tk_image_g)
        canvas.place(x = 0, y = 0)
        image_g.save("images/gray_image.jpg")

    if get_value == values[1]:
        image = Image.open('images/original_image.jpg')
        image = image.resize((1500,900))
        tk_image = ImageTk.PhotoImage(image)
        canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
        canvas.create_image(0, 0, anchor = "nw", image = tk_image)
        canvas.place(x = 0, y = 0)

        image_b = image.filter(ImageFilter.BLUR)

        tk_image_b = ImageTk.PhotoImage(image_b)
        canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
        canvas.create_image(0, 0, anchor = "nw", image = tk_image_b)
        canvas.place(x = 0, y = 0)
        image_b.save("images/blurred_image.jpg")
        

    if get_value == values[2]:
        image = Image.open('images/original_image.jpg')
        image = image.resize((1500,900))
        tk_image = ImageTk.PhotoImage(image)
        canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
        canvas.create_image(0, 0, anchor = "nw", image = tk_image)
        canvas.place(x = 0, y = 0)

        image_d = image.filter(ImageFilter.DETAIL)

        tk_image_d = ImageTk.PhotoImage(image_d)
        canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
        canvas.create_image(0, 0, anchor = "nw", image = tk_image_d)
        canvas.place(x = 0, y = 0)
        image_d.save("images/blurred_image.jpg")
        
       

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

    image = Image.open("images/original_image.jpg")
    image = image.resize((1500,900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_r = image.resize((width, height), Image.ANTIALIAS)

    tk_image_r = ImageTk.PhotoImage(image_r)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_r)
    canvas.place(x = 0, y = 0)
    image_r.save("images/resized_image.jpg")


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
    canvas.delete("written")

current_index_d = 0
list_name_image = []
def download():
    global current_index_d
    file_path = ctk.filedialog.askopenfilename(initialdir = "images/", filetypes = (("JPEG files", "*.jpeg;*.jpg"),))
    file_path1 = os.path.splitext(os.path.basename(file_path))[0]
    list_name_image.append(file_path1)
    if current_index_d < len(list_name_image):
        value = list_name_image[current_index_d]
        listbox_images.insert("end", value)
        current_index_d += 1
listbox_images = Listbox(m_app.app, width = 20, height = 7, font = m_font.font_list,bg = "#1E1E1E", fg = "white")  
listbox_images.place(x = 50,y = 1150)