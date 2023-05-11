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
    text = "Обрезка фото",
    command = m_operation.crop_image
)
button1.place(x = 140, y = 438)

button2 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Изменение размера",
    command = m_operation.resize
)
button2.place(x = 260, y = 438)

button3 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Рисовать",
    command = m_operation.draw_pictures
)
button3.place(x = 425, y = 438)

button4 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Писать",
    command = m_operation.write
)
button4.place(x = 540, y = 438)

button5 = ctk.CTkButton(
    master = m_app.app,
    width = 110,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Фильтр",
    command = m_operation.get_selected_value
)
button5.place(x = 650, y = 438)

button6 = ctk.CTkButton(
    master = m_app.app,
    width = 70,
    height = 31,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#D9D9D9",
    text = ""
)
button6.place(x = 428, y = 364)

button7 = ctk.CTkButton(
    master = m_app.app,
    width = 70,
    height = 31,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#D9D9D9",
    text = ">",
    text_color = "black"
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
    text = "Загрузка фото",
    command = m_operation.download_image
)
button8.place(x = 10,y = 438)

button_rotate = ctk.CTkButton(
    master = m_app.app,
    width = 30,
    height = 30,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
    image = ctk.CTkImage(light_image=Image.open("images/rotate.png"),size = (30, 30)),
    command = m_operation.rotated

)
button_rotate.place(x = 770,y = 438)