import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
import requests
import sys
import modules.app as m_app
import modules.path as m_path

# Получаем информацию по изображению (формат)
def info_image():
    image_format = image.format
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, text = "Format: {}".format(image_format))
    label_info.place(x = 20, y = 25)

    # Получаем информацию по изображению (высота и ширина)
    width, height = image.size
    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, text = "width:{} height:{}".format(width, height))
    label_info.place(x = 20, y = 55)

    label_info_img = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, text = "info image")
    label_info_img.place(x = 40, y = 15)

def crop_image():
    global image
    global label_image
    global tk_image
    image = Image.open('images/img.png')
    image = image.crop((0, 80, 200, 400))
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
        
    image = image.rotate(90)
    image.save('images/img.png', size = (607, 393))
    tk_image = ImageTk.PhotoImage(image)

    label_image.destroy()
    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 20,y = 10)  


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
    text = "Памагити" "-" "Ок"
    font = ImageFont.truetype("arial.ttf", size=36)
    
    idraw.text((10, 10), text, font=font)
    tk_image = ImageTk.PhotoImage(image)
    label_image.destroy()

    label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_image.place(x = 5, y = 10)
# 
# write()

def filters():
    image = Image.open('images/img.jpg')
    image = image.filter(ImageFilter.BLUR)
    tk_image = ImageTk.PhotoImage(image)
    label_blur = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    label_blur.place(x = 20, y = 10)

# filters()

list_url = []
text = ctk.StringVar()
entry = ctk.CTkEntry(master = m_app.app,
                      width = 180, 
                      height = 40, 
                      fg_color = "#1E1E1E", 
                      text_color = "white", 
                      border_color = "#E8900C",
                      textvariable = text)
entry.place(x = 15, y = 18)

count = 1

# https://cameralabs.org/media/camera/noiabr/23/53_faab6d80ccb84bd6529017d21e2ea8d5.jpg
# https://w.forfun.com/fetch/70/703e3aefd9500eff0f63294bc383ac2a.jpeg
# https://klike.net/uploads/posts/2019-11/1572612050_1.jpg

def download_image():
    global image 
    global count
    url1 = text.get()
    try:
        req = requests.get(url1, stream = True).raw
        image = Image.open(req)
        list_url.append(url1)
    except:
        print("Unable to load image from URL")

    try:
        image.save(f"images/image{count}.jpg," "jpeg")
        images_path = ctk.CTkImage(light_image = Image.open(m_path.search_path(f"images/image{count}.jpg")), size =(607, 393))
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                                    text = "",
                                    image = images_path)
        label_image.place(x = 5, y = 200, anchor = ctk.W)
        info_image()
        count += 1
    except:
        image.save(f"images/image{count}.png")
        images_path = ctk.CTkImage(light_image = Image.open(m_path.search_path(f"images/image{count}.png")), size =(607, 393))
        label_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE,
                                    text = "",
                                    image = images_path)
        label_image.place(x = 5, y = 200, anchor = ctk.W)
        info_image()
        count += 1