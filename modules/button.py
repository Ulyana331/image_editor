import customtkinter as ctk
import modules.app as m_app
import modules.image_operation as m_operation

button1 = ctk.CTkButton(
    master = m_app.app,
    width = 120,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Обрезка фото",
    command = m_operation.crop_image
)
button1.place(x = 150, y = 438)

button2 = ctk.CTkButton(
    master = m_app.app,
    width = 120,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Поворот фото",
    command = m_operation.rotated
)
button2.place(x = 280, y = 438)

button3 = ctk.CTkButton(
    master = m_app.app,
    width = 120,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Рисовать",
    command = m_operation.draw_pictures
)
button3.place(x = 420, y = 438)

button4 = ctk.CTkButton(
    master = m_app.app,
    width = 120,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
)
button4.place(x = 570, y = 438)

button5 = ctk.CTkButton(
    master = m_app.app,
    width = 120,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
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
    width = 120,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Загрузка фото",
    command = m_operation.download_image
)
button8.place(x = 20,y = 438)