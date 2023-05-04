import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
import requests
import sys
import modules.app as m_app

url = 'https://cameralabs.org/media/camera/noiabr/23/53_faab6d80ccb84bd6529017d21e2ea8d5.jpg'
# открываем изображение по ссылке
try:
    resp = requests.get(url, stream=True).raw
except requests.exceptions.RequestException as e:  
    sys.exit(1)

# сохраняем изображение в формате jpg  
try:
    img = Image.open(resp)
except IOError:
    print("Unable to open image")
    sys.exit(1)
img.save('img.jpg', 'jpeg')

# пересохраняем изображение в формате png
try:
    img_1 = Image.open("img.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)
 
img_1.save('img.png', 'png')

# вывод изображения в окно приложения
image = Image.open('img.png')
image_tk = ImageTk.PhotoImage(image)
label_image = ctk.CTkLabel(m_app.app.FRAME_IMAGE, image=image_tk, text = "")
label_image.place(x=20,y=10)
# image.show()

# Получаем информацию по изображению (формат)
image_format = image.format

label = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, text = "Format: {}".format(image_format))
label.place(x = 10, y = 10)

# Получаем информацию по изображению (висота і ширина)
width, height = image.size

label = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, text = "width:{} height:{}".format(width, height))
label.place(x = 10, y = 35)

def crop_image():
    image = Image.open('img.png')
    cropped = image.crop((0, 80, 200, 400))
    cropped.save('D:\image editor\img.png')
    label_image.destroy()
    tk_image = ImageTk.PhotoImage(cropped)
    lable_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    lable_image.place(x = 20,y = 10)

def rotated():
    try:
        image = Image.open("img.png")
    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    image_rotated = image.rotate(180)
    image_rotated.save('img.png')
    tk_image = ImageTk.PhotoImage(image_rotated)
    lable_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    lable_image.place(x = 20,y = 10)

def draw_pictures():
    # Создаем белый квадрат
    img = Image.new('RGBA', (200, 200), 'white')    
    idraw = ImageDraw.Draw(img)
    
    idraw.rectangle((10, 10, 100, 100), fill='red')
    
    img.save('rectangle.png')
    tk_image = ImageTk.PhotoImage(img)
    lable_image = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
    lable_image.place(x = 20,y = 10)

# функция написания текста на экране
try:
    img = Image.open("img.jpg")
except:
    print("Unable to load image")
    sys.exit(1)
    
idraw = ImageDraw.Draw(img)
text = "Памагити" "-" "Ок"
font = ImageFont.truetype("arial.ttf", size=36)
 
idraw.text((10, 10), text, font=font)
 
img.save('img_watermarked.png')
tk_image = ImageTk.PhotoImage(img)

lable_write = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
lable_write.place(x = 20, y = 10)
# 

image = Image.open('img.jpg')
blurred = image.filter(ImageFilter.BLUR)
blurred.save('img.png')
tk_image = ImageTk.PhotoImage(blurred)
lable_write = ctk.CTkLabel(master = m_app.app.FRAME_IMAGE, text = "", image = tk_image)
lable_write.place(x = 20, y = 10)

