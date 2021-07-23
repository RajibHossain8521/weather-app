# Calculator App
import tkinter as tk
from PIL import Image, ImageTk

height = 600
width = 700

# SETTINGS OF APP WINDOW
app = tk.Tk()
canvas = tk.Canvas(app, height=height, width=width)
canvas.pack()
app.resizable(False, False)
app.title('Weather App')

# set background image
background_image = tk.PhotoImage(file='background-image.png')
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

# heading of the App
heading = tk.Label(app,
        text='Weather Information',
        font=('Helvetica', 25, 'bold'),
        bg='#ffff99',
        bd=5)
heading.place(y=2, relwidth=1)

# INPUT FRAME
frame = tk.Frame(app, bg='#42c2f4', bd=5)
frame.place(x=100, y=80, relwidth=0.75, relheight=0.1)
# input text-box
textbox = tk.Entry(frame, font=('Courier', 16))
textbox.place(relwidth=0.65, relheight=1)
# submit button
submit_button = tk.Button(frame,
                        text='Search Weather',
                        font=35)
submit_button.place(x=360, relheight=1, relwidth=0.3)

# RESULT FRAME
information_frame = tk.Frame(app, bg='#42c2f4', bd=6)
information_frame.place(x=100, y=200, relwidth=0.75, relheight=0.55)

# weather information
results = tk.Label(information_frame, 
                font=('Courier', 14), 
                anchor='nw', 
                justify='left',
                bg='white',
                bd=4)
results.place(relwidth=1, relheight=1)

# set icon of weather
weather_icon = tk.Canvas(results, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

app.mainloop()