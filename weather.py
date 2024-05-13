from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image
from datetime import datetime

root = Tk()
root.title("Weather App")
root.configure(bg="royal blue1")
root.geometry("700x450")

def get_weather():
    city = city_input.get()
    api_key = "d30c8b838fe4c5de98341081e376bbfb"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']-273.15
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        epoch_time = data['dt']
        date_time = datetime.fromtimestamp(epoch_time)
        desc = data['weather'][0]['description']
        cloudy = data['clouds']['all']

        timelabel.config(text=str(date_time))
        temp_field.insert(0, '{:.2f}'.format(temp)+ " C")
        pressure_field.insert(0, str(pressure) + " hPa")
        hum_field.insert(0, str(humidity) + "%")
        wind_field.insert(0, str(wind) + "km/h")        
        desc_field.insert(0, str(desc))
        cloud_field.insert(0, str(cloudy) + "%")
    else:
        mb.showerror("Error","City not found. Enter a valid city name.")
        city_input.delete(0, END)

title = Label(root, text="Current Weather", fg="yellow", bg="royal blue1", font=("bold",15) )
label1 = Label(root, text = "Enter the city name: ", font = ("bold", 12), bg="royal blue1")
city_input = Entry(root, width=24, fg="dark blue", font=12, relief="groove")
timelabel = Label(root, text="", bg="royal blue1", font=("bold", 14), fg="yellow")

button_submit = Button(root, text="Get Weather", width=10, font=12, bg="dark blue", fg="#ffffff",command = get_weather)
# button_forecast = Button(root, text = "Weather forecast", width=14, font=12, bg="dark blue",fg="#ffffff" , command= None)
button_reset = Button(root, text = "Reset", font=12, bg="dark blue", fg="#ffffff", command= None )

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

title.grid(row = 0, column = 1)
label1.grid(row = 1, column = 0)
timelabel.grid(row =1, column = 2)
button_submit.grid(row = 2, column = 1)
labelTemp.grid(row = 3, column = 0, padx = 5, pady = 5, sticky="W" )
labelPres.grid(row = 4, column = 0, padx = 5, pady = 5, sticky="W" )
labelHum.grid(row = 5, column = 0, padx = 5, pady = 5, sticky="W" )
labelWind.grid(row = 6, column = 0, padx = 5, pady = 5, sticky="W" )
labelCloud.grid(row = 7, column = 0, padx = 5, pady = 5, sticky="W" )
labelDesc.grid(row = 8, column = 0, padx = 5, pady = 5, sticky="W" )


city_input.grid(row = 1, column =1, padx=5, pady = 5)
temp_field.grid(row = 3, column =1, padx=5, pady = 5)
pressure_field.grid(row = 4, column =1, padx=5, pady = 5)
hum_field.grid(row = 5, column =1, padx=5, pady = 5)
wind_field.grid(row = 6, column =1, padx=5, pady = 5)
cloud_field.grid(row = 7, column =1, padx=5, pady = 5)
desc_field.grid(row = 8, column =1, padx=5, pady = 5)
button_reset.grid(row = 9, column =1, padx=5, pady = 5)

root.mainloop()
