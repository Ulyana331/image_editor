import customtkinter as ctk
import modules.app as m_app
import modules.image_operation as m_operation
from PIL import Image

button1 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Обрізка фото",
    command = m_operation.crop_image
)
button1.place(x = 210, y = 438)

button2 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Зміна розміру",
    command = m_operation.resize
)
button2.place(x = 330, y = 438)

button3 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Повернути фото",
    command = m_operation.rotated
)
button3.place(x = 460, y = 438)

button4 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Писати",
    command = m_operation.write
)
button4.place(x = 600, y = 438)

button5 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Фільтри",
    command = m_operation.get_selected_value
)
button5.place(x = 720, y = 438)

button6 = ctk.CTkButton(
    master = m_app.app,
    width = 70,
    height = 31,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#D9D9D9",
    text = "<",
    text_color = "black",
    command = m_operation.prev_image
)
button6.place(x = 400, y = 364)

button7 = ctk.CTkButton(
    master = m_app.app,
    width = 70,
    height = 31,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#D9D9D9",
    bg_color = "transparent",
    text = ">",
    text_color = "black",
    command = m_operation.next_image
)
button7.place(x = 527, y = 364)


button8 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Завантажити фото",
    command = m_operation.download_image
)
button8.place(x = 50,y = 438)

