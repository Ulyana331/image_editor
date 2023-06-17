import customtkinter as ctk
import modules.app as m_app
import modules.image_operation as m_operation
from PIL import Image
import modules.font as m_font

button_crop = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Виділити область",
    font = m_font.font_buttons,
    command = m_operation.crop_image_2
)
button_crop.place(x = 800, y = 600)

button_resize = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Зміна розміру",
    font = m_font.font_buttons,
    command = m_operation.resize
)
button_resize.place(x = 1030, y = 700)

button_rotate = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Повернути фото",
    font = m_font.font_buttons,
    command = m_operation.rotate
)
button_rotate.place(x = 1030, y = 600)

button_write = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Писати",
    font = m_font.font_buttons,
    command = m_operation.write
)
button_write.place(x = 1230, y = 700)

button_draw = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Малювати",
    font = m_font.font_buttons,
    command = m_operation.draw_on_picture
)
button_draw.place(x = 1230, y = 600)

button_prew = ctk.CTkButton(
    master = m_app.app.FRAME_IMAGE,
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
button_prew.place(x = 328, y = 530)

button_next = ctk.CTkButton(
    master = m_app.app.FRAME_IMAGE,
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
button_next.place(x = 527, y = 530)


button_download = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Завантажити фото",
    font = m_font.font_buttons,
    command = m_operation.download_image
)
button_download.place(x = 800,y = 700)

button_clear_frame = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Очистити фрейм",
    font = m_font.font_buttons,
    command = m_operation.clear_frame
)
button_clear_frame.place(x = 600,y = 600)

button_clear_image = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Очистити фото",
    font = m_font.font_buttons,
    command = m_operation.clear_drawing
)
button_clear_image.place(x = 600,y = 700)

button_download_2 = ctk.CTkButton(
    master = m_app.app,
    width = 180,
    height = 60,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "Завантажити з ПК",
    font = m_font.font_buttons,
    command = m_operation.download
)
button_download_2.place(x = 380,y = 700)