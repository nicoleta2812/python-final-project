from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image
from datetime import datetime

root = Tk()
root.title("Weather App")
root.configure(bg="royal blue1")
root.geometry("700x450")

title = Label(root, text="Weather and forecast", fg="yellow", bg="royal blue1", font=("bold",15) )
label1 = Label(root, text = "Enter the city name: ", font = ("bold", 12), bg="royal blue1")
city_input = Entry(root, width=24, fg="red2", font=12, relief="groove")
timelabel = Label(root, text="", bg="royal blue1", font=("bold", 14), fg="yellow")

button_submit = Button(root, text="Get Weather", width=10, font=12, bg="lime green", command= None)
button_forecast = Button(root, text = "Weather forecast", width=14, font=12, bg="lime green", command= None)
button_reset = Button(root, text = "Reset", font=12, bg="lime green", command= None )

# button_submit.pack(padx=50, pady=50)
labelTemp = Label(root, text = "Temperature", font =("bold", 12), bg="red")
labelPres = Label(root, text = "Pressure", font =("bold", 12), bg="royal blue1")
labelHum = Label(root, text = "Humidity", font =("bold", 12), bg="royal blue1")
labelWind = Label(root, text = "Wind", font =("bold", 12), bg="red")
labelCloud = Label(root, text = "Cloudness", font =("bold", 12), bg="red")
labelDesc = Label(root, text = "Description", font =("bold", 12), bg="red")

temp_field = Entry(root, width = 24, font = 11)
pressure_field = Entry(root, width = 24, font = 11)
hum_field = Entry(root, width = 24, font = 11 )
wind_field = Entry(root, width = 24, font = 11 )
cloud_field = Entry(root, width = 24, font = 11 )
desc_field = Entry(root, width = 24, font = 11 )

root.mainloop()
