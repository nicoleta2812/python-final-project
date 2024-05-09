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
city_input = Entry(root, width=24, fg="dark blue", font=12, relief="groove")
timelabel = Label(root, text="", bg="royal blue1", font=("bold", 14), fg="yellow")

button_submit = Button(root, text="Get Weather", width=10, font=12, bg="lime green", command= None)
button_forecast = Button(root, text = "Weather forecast", width=14, font=12, bg="dark blue", fg="#ffffff", command= None)
button_reset = Button(root, text = "Reset", font=12, bg="lime green", command= None )

# button_submit.pack(padx=50, pady=50)
labelTemp = Label(root, text = "Temperature", font =("bold", 12), bg="royal blue1")
labelPres = Label(root, text = "Pressure", font =("bold", 12), bg="royal blue1")
labelHum = Label(root, text = "Humidity", font =("bold", 12), bg="royal blue1")
labelWind = Label(root, text = "Wind", font =("bold", 12), bg="royal blue1")
labelCloud = Label(root, text = "Cloudness", font =("bold", 12), bg="royal blue1")
labelDesc = Label(root, text = "Description", font =("bold", 12), bg="royal blue1")

temp_field = Entry(root, width = 24, font = 11)
pressure_field = Entry(root, width = 24, font = 11)
hum_field = Entry(root, width = 24, font = 11 )
wind_field = Entry(root, width = 24, font = 11 )
cloud_field = Entry(root, width = 24, font = 11 )
desc_field = Entry(root, width = 24, font = 11 )


label1.grid(row = 1, column = 0)
button_forecast.grid(row = 2, column = 1, pady = 5)
labelTemp.grid(row = 3, column = 0, padx = 5, pady = 5, sticky="W" )
labelPres.grid(row = 4, column = 0, padx = 5, pady = 5, sticky="W" )
labelHum.grid(row = 5, column = 0, padx = 5, pady = 5, sticky="W" )
labelWind.grid(row = 6, column = 0, padx = 5, pady = 5, sticky="W" )
labelCloud.grid(row = 7, column = 0, padx = 5, pady = 5, sticky="W" )
labelDesc.grid(row = 8, column = 0, padx = 5, pady = 5, sticky="W" )


city_input.grid(row = 1, column =1, padx=5, pady = 5)
temp_field.grid(row = 3, column =1, padx=5, pady = 5)
pressure_field.grid(row = 4, column =1, padx=5, pady = 5)
root.mainloop()
