import customtkinter as ctk
import modules.app as m_app

button1 = ctk.CTkButton(
    master = m_app.app,
    width = 173,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
    # command = m_sounds.play,
    # image = ctk.CTkImage
    # (light_image=Image.open(m_path.search_path("images/button_play.png")),
    # size = (82, 43)))
)
button1.place(x = 20, y = 438)

button2 = ctk.CTkButton(
    master = m_app.app,
    width = 130,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
)
button2.place(x = 213, y = 438)

button3 = ctk.CTkButton(
    master = m_app.app,
    width = 130,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
)
button3.place(x = 375, y = 438)

button4 = ctk.CTkButton(
    master = m_app.app,
    width = 130,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
)
button4.place(x = 537, y = 438)

button5 = ctk.CTkButton(
    master = m_app.app,
    width = 130,
    height = 41,
    border_width = 5,
    border_color = "#E8900C",
    corner_radius = 15,
    fg_color = "#1E1E1E",
    text = "",
)
button5.place(x = 699, y = 438)