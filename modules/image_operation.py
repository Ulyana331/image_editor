import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
import requests
import sys
import modules.app as m_app
import modules.path as m_path
from tkinter import Listbox, END
import modules.font as m_font

# Получаем информацию по изображению (формат)
def info_image():
    image_format = image.format
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, text = "Format: {}".format(image_format))
    label_info.place(x = 10, y = 25)

    # Получаем информацию по изображению (высота и ширина)
    width, height = image.size
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, text = "width:{} height:{}".format(width, height))
    label_info.place(x = 8, y = 55)

def crop_image():
    global image
    global label_image
    global tk_image
    # image = Image.open('images/img.png')
    image = image.crop((0,80,120,100))
    label_image.destroy()
    tk_image = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 20,y = 10)

def rotated():
    global image
    global label_image
    global tk_image
    try:
        image = Image.open("images/img.png")
    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    image = image.rotate(180)
    image.save('images/img.png', size = (607, 393))
    tk_image = ImageTk.PhotoImage(image)

    # label_image.destroy()
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    # label_image.place(x = 20,y = 10, anchor = ctk.W) 
    label_image.place(x = 5, y = 200, anchor = ctk.W) 


def draw_pictures():
    global image
    global label_image
    global tk_image
    # Создаем белый квадрат
    image = Image.new('RGBA', (200, 200), 'white')    
    idraw = ImageDraw.Draw(image)
    
    idraw.rectangle((10, 10, 100, 100), fill='red')
    tk_image = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 20,y = 10)

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
write = entry_write.get()

entry_write.place(x = 15, y = 165)
label = ctk.CTkLabel(master = m_app.app, text = "Введите надпись")
label.place(x = 15, y = 135)
def write():
    global image
    global label_image
    global tk_image
    try:
        image = Image.open("images/img.jpg")
    except:
        print("Unable to load image")
        sys.exit(1)
        
    idraw = ImageDraw.Draw(image)
    text = write
    font = ImageFont.truetype("arial.ttf", size=36)
    
    idraw.text((10, 10), text, font=font)
    tk_image = ImageTk.PhotoImage(image)
    label_image.destroy()

    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 5, y = 200, anchor = ctk.W)
# 

# https://w.forfun.com/fetch/70/703e3aefd9500eff0f63294bc383ac2a.jpeg
# https://klike.net/uploads/posts/2019-11/1572612050_1.jpg
# https://cameralabs.org/media/camera/noiabr/23/53_faab6d80ccb84bd6529017d21e2ea8d5.jpg
# (0, 80, 200, 400)
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
label_url = ctk.CTkLabel(master = m_app.app, text = "Введите ссылку")
label_url.place(x = 20, y = -5)


count = 1
def download_image():
    global image
    global count
    global label_image
    url1 = text.get()
    try:
        req = requests.get(url1, stream = True).raw
        image = Image.open(req)
        list_url.append(url1)
        print(list_url)
    except:
        print("Unable to load image from URL")
    
    try:
        image.save(f"images/img.jpg, " "jpeg")
        images_path = ctk.CTkImage(light_image = Image.open(m_path.search_path(f"images/img.jpg")), size = (607,393))
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = images_path,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)
        info_image()
        # count += 1
    except:
        image.save(f"images/img.png", "png")
        images_path = ctk.CTkImage(light_image = Image.open(m_path.search_path(f"images/img.png")), size = (607,393))
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = images_path,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)
        info_image()
        
def get_selected_value():
    global get_value
    global image
    global label_image
    get_value = listbox.get(listbox.curselection())
    if get_value == values[0]:
        try:
            image = Image.open("images/img.png")
        except IOError:
            print("Unable to load image")
            sys.exit(1)
        grayscale = image.convert('L')
        image_tk = ImageTk.PhotoImage(grayscale)
        label_image.destroy()
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                                image = image_tk,
                                text = "")
        label_image.place(x = 5, y = 10)
    if get_value == values[1]:
        # image = Image.open('img.png')
        download_image()
        blurred_img = image.filter(ImageFilter.BLUR)
        tk_image = ImageTk.PhotoImage(blurred_img)
        label_image.destroy()
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = tk_image,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)

    if get_value == values[2]:
        # image = Image.open('img.png')
        download_image()
        detailed_img = image.filter(ImageFilter.DETAIL)
        tk_image = ImageTk.PhotoImage(detailed_img)
        label_image.destroy()
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                             image = tk_image,
                             text = "")
        label_image.place(x = 5, y = 200, anchor = ctk.W)
    print(get_value)
values = ["Серое фото", "Blur", "Detail"]
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

label = ctk.CTkLabel(master = m_app.app, text = "Введите размеры")
label.place(x = 15, y = 65)

def resize():
    global label_image
    height = entry_height.get()
    width = entry_width.get()
    image = Image.open("images/img.png")
    resized = image.resize((width, height), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized)
    label_image.destroy()
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 20, y = 10)
