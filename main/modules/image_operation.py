import customtkinter as ctk
from PIL import Image, ImageTk, ImageFilter
import requests
import modules.app as m_app
from tkinter import Listbox, END
import modules.font as m_font

label_information = ctk.CTkLabel(master = m_app.app, font = m_font.font_label, text = "Інформація фотографіЇ:")
label_information.place(x = 15, y = 440)
label_list_images = ctk.CTkLabel(master = m_app.app, font = m_font.font_label, text = "Список зображень:")
label_list_images.place(x = 15, y = 580)
label_pencil_size = ctk.CTkLabel(master = m_app.app, text = "Оберіть розмір та", font = m_font.font_label)
label_pencil_size.place(x=220,y=280)    
label_pencil_color = ctk.CTkLabel(master = m_app.app, text = "колір олівця:", font = m_font.font_label)
label_pencil_color.place(x=400,y=280)    

pencil_size_data = ctk.IntVar()
entry_pencil_size = ctk.CTkEntry(
    master = m_app.app,
    width = 90,
    height = 40,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = pencil_size_data 
)
entry_pencil_size.place(x = 220, y = 320)

pencil_color_data = ctk.StringVar()
entry_pencil_color = ctk.CTkEntry(
    master = m_app.app,
    width = 110,
    height = 40,
    fg_color = "#1E1E1E",
    text_color = "white",
    border_color = "#E8900C",
    textvariable = pencil_color_data 
)
entry_pencil_color.place(x = 220, y = 370)


def info_image():
    image = Image.open(f"images/image{count}.jpg")

    width = image.width
    height = image.height
    format = f"Format: {image.format}"
    mode = f"Mode: {image.mode}"

    label_info_format = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = format)
    label_info_format.place(x = 10, y = 18)

    label_info_mode = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = mode)
    label_info_mode.place(x = 120, y = 18)

    label_info = ctk.CTkLabel(master = m_app.app.FRAME_INFO_IMAGE, font = m_font.font_info, text = f"Width: {width}    Height: {height}")
    label_info.place(x = 8, y = 50)


def draw_on_picture():
    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    pencil_size = pencil_size_data.get()
    pencil_color = pencil_color_data.get()

    canvas.data = {}
    def start_drawing(event):
        canvas.data["line_start"] = (event.x, event.y)
    def draw_stick(event):
        if "line_start" in canvas.data:
            start = canvas.data["line_start"]
            end = (event.x, event.y)
            canvas.create_line(start[0], start[1], end[0], end[1], fill = pencil_color, width = pencil_size, tags = "drawing")
            canvas.data["line_start"] = end
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", draw_stick)
    canvas.bind("<ButtonRelease-1>", lambda event: canvas.data.pop("line_start", None))

    image = Image.open(f"images/original_image.jpg")

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

def write():
    global count
    count += 1
    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    write = text2.get()
    
    image_c = canvas.create_text(100, 100, text=write, font=("Arial", 36), fill="white", tags = "written")
    image_c.save(f"images/image.jpg")

    tk_image_w = ImageTk.PhotoImage(image_w)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_w)
    canvas.place(x = 0, y = 0)
    image_w = Image.open("images/written_image_2.jpg")


def rotate():
    global count
    count += 1
    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_r = image.rotate(180)
    image_r.save(f"images/image{count}.jpg")
    
    list_name_image.append(f"images/image{count}.jpg")

    tk_image_r = ImageTk.PhotoImage(image_r)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_r)
    canvas.place(x = 0, y = 0)
    image_r = Image.open("images/rotated_image_2.jpg")

current_index_d = 0
list_name_image = []
def download():
    global current_index_d
    global count 
    count += 1
    file_path = ctk.filedialog.askopenfilename(initialdir = "images/", filetypes = (("JPEG files", "*.jpeg;*.jpg"),))
    list_name_image.append(file_path)
    if current_index_d < len(list_name_image):
        value = list_name_image[current_index_d]
        listbox_images.insert("end", value)
        current_index_d += 1
    info_image()
listbox_images = Listbox(m_app.app, width = 37, height = 10, font = m_font.font_list,bg = "#1E1E1E", fg = "white")  
listbox_images.place(x = 30,y = 1080)

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

count = 0
def download_image():
    global url1
    global count
    global current_index_d
    count += 1
    url1 = text.get()
    try:
        req = requests.get(url1, stream = True).raw
        image = Image.open(req)

        image.save(f"images/image{count}.jpg")
        list_name_image.append(f"images/image{count}.jpg")

        list_url.append(url1)
    except:
        print("Unable to load image from URL")

    if current_index_d < len(list_name_image):
        value = list_name_image[current_index_d]
        listbox_images.insert("end", value)
        current_index_d += 1

    info_image()

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
    global count
    count += 1

    height = entry_height.get()
    width = entry_width.get()

    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_r = image.resize((width, height), Image.ANTIALIAS)
    image_r.save(f"images/image{count}.jpg")
    list_name_image.append(f"images/image{count}.jpg")

    canvas.delete("all")
    tk_image_r = ImageTk.PhotoImage(image_r)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = width, height = height, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_r)
    canvas.place(x = 0, y = 0)
    image_r = Image.open("images/resized_image.jpg")

label_filters = ctk.CTkLabel(master = m_app.app, text = "Оберіть фільтр:", font = m_font.font_label)
label_filters.place(x=10,y=280)    


def clear_frame():
    buttons = [widget for widget in m_app.app.FRAME_IMAGE.winfo_children() if isinstance(widget,ctk.CTkButton)]
    for widget in m_app.app.FRAME_IMAGE.winfo_children():
        if widget not in buttons:
            widget.destroy()

def clear_drawing():
    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
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

    canvas.delete("drawing")
    canvas.delete("written")
    image = Image.open("images/no.jpg")

def next_image():
    global count
    count += 1
    image = Image.open(f"images/image{count}.jpg")
    image = image.resize((1500,900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)
    image = Image.open("images/next1.jpg")

def prev_image():
    global count
    count -= 1
    image = Image.open(f"images/image{count}.jpg")
    image = image.resize((1500,900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)
    image = Image.open("images/prev1.jpg")


start_x = 0
start_y = 0
end_x = 0
end_y = 0

def on_mouse_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
def on_mouse_release(event):
    global end_x, end_y
    end_x = event.x
    end_y = event.y
    crop_image()

def crop_image():
    global current_index_d
    global count
    count += 1

    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_c = image.crop((start_x, start_y, end_x, end_y))
    image_c.save(f"images/image{count}.jpg")

    tk_image_c = ImageTk.PhotoImage(image_c)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_c)
    canvas.place(x = 0, y = 0)
    
    image_c = Image.open("images/cropped_image.jpg")

def crop_image_2():
    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    canvas.bind("<ButtonPress-1>", on_mouse_press)
    canvas.bind("<ButtonRelease-1>", on_mouse_release)

    image = Image.open("images/o.jpg")


def display_image(event):
    selected_index = listbox_images.curselection()
    if selected_index:
        image_path = listbox_images.get(selected_index)
        image = Image.open(image_path)
        image = image.resize((1500, 900))
        tk_image = ImageTk.PhotoImage(image)
        canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
        canvas.create_image(0, 0, anchor = "nw", image = tk_image)
        canvas.place(x = 0, y = 0)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=tk_image)
        canvas.update()
        image = Image.open("images/i.jpg")

listbox_images.bind("<<ListboxSelect>>", display_image)

def gray_filter():
    global current_index_d
    global count
    count += 1

    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_g = image.convert('L')
    image_g.save(f"images/image{count}.jpg")
    list_name_image.append(f"images/image{count}.jpg")
    if current_index_d < len(list_name_image):
        value = list_name_image[current_index_d]
        listbox_images.insert("end", value)
        current_index_d += 1

    tk_image_g = ImageTk.PhotoImage(image_g)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_g)
    canvas.place(x = 0, y = 0)
    image_g = Image.open("images/gray_image.jpg")

def blur_filter():
    global current_index_d
    global count
    count += 1 

    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_b = image.filter(ImageFilter.BLUR)
    image_b.save(f"images/image{count}.jpg")
    list_name_image.append(f"images/image{count}.jpg")
    if current_index_d < len(list_name_image):
        value = list_name_image[current_index_d]
        listbox_images.insert("end", value)
        current_index_d += 1

    tk_image_b = ImageTk.PhotoImage(image_b)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_b)
    canvas.place(x = 0, y = 0)
    image_b = Image.open("images/blurred_image.jpg")

def detail_filter():
    global current_index_d
    global count 
    count += 1

    selected_index = listbox_images.curselection()
    image_path = listbox_images.get(selected_index)
    image = Image.open(image_path)
    image = image.resize((1500, 900))
    tk_image = ImageTk.PhotoImage(image)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image)
    canvas.place(x = 0, y = 0)

    image_d = image.filter(ImageFilter.DETAIL)
    image_d.save(f"images/image{count}.jpg")
    list_name_image.append(f"images/image{count}.jpg")
    if current_index_d < len(list_name_image):
        value = list_name_image[current_index_d]
        listbox_images.insert("end", value)
        current_index_d += 1

    tk_image_d = ImageTk.PhotoImage(image_d)
    canvas = ctk.CTkCanvas(m_app.app.FRAME_IMAGE, width = 1500, height = 900, bg = "#1E1E1E")
    canvas.create_image(0, 0, anchor = "nw", image = tk_image_d)
    canvas.place(x = 0, y = 0)
    image_d = Image.open("images/detailed_image_3.jpg")

radio_var = ctk.StringVar()

radio_btn1 = ctk.CTkRadioButton(m_app.app, width = 10, text="Gray", value="gray", variable=radio_var, command=gray_filter)
radio_btn2 = ctk.CTkRadioButton(m_app.app, width = 10, text="Blur", value="blur", variable=radio_var, command=blur_filter)
radio_btn3 = ctk.CTkRadioButton(m_app.app, width = 10, text="Detail", value="detail", variable=radio_var, command=detail_filter)

radio_btn1.place(x = 20, y = 330)
radio_btn2.place(x = 20, y = 360)
radio_btn3.place(x = 20, y = 390)