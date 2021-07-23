# Weather App
import tkinter as tk
from PIL import Image, ImageTk
from weather_api import weather_information


def open_weather_icon(icon):
    # set current weather icon
    size = int(information_frame.winfo_height()*0.30)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

def get_weather_info(city_name):
    # set weather information
    weather_report = weather_information(city_name)
    results['text'] = weather_report[0]
    if weather_report[1]:
        weather_icon_name = weather_report[1]
        open_weather_icon(weather_icon_name)


# basic settings of app window
app = tk.Tk()
canvas = tk.Canvas(app, height=600, width=700)
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

# input frame
frame = tk.Frame(app, bg='#42c2f4', bd=5)
frame.place(x=100, y=80, relwidth=0.75, relheight=0.1)
# input text-box
textbox = tk.Entry(frame, font=('Courier', 16))
textbox.place(relwidth=0.65, relheight=1)
# submit button
submit_button = tk.Button(frame,
                        text='Search Weather',
                        font=35,
                        command=lambda: get_weather_info(textbox.get()))
submit_button.place(x=360, relheight=1, relwidth=0.3)

# information frame
information_frame = tk.Frame(app, bg='#42c2f4', bd=6)
information_frame.place(x=100, y=200, relwidth=0.75, relheight=0.55)

# label for weather information
results = tk.Label(information_frame, 
                font=('Courier', 14), 
                anchor='nw', 
                justify='left',
                bg='white',
                bd=4)
results.place(relwidth=1, relheight=1)

# canvas for weather icon
weather_icon = tk.Canvas(results, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

app.mainloop()