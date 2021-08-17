import tkinter as tk
import requests
import time
from functools import partial 


def subtract_for_celcius(temp):
    return int(temp - 273.150)

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    if units.get()==0:
        api = api+"&units=imperial"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    min_temp = int(json_data['main']['temp_min'])
    max_temp = int(json_data['main']['temp_max'])
    if units.get()==1:
        temp = subtract_for_celcius(temp)
        min_temp = subtract_for_celcius(min_temp)
        max_temp = subtract_for_celcius(max_temp)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 14400))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 14400))
    symbol = "°c"
    if units.get()==0:
        symbol="°f"
    final_info = condition + "\n" + str(temp) + symbol
    final_data = "\n"+ "Min Temp: " + str(min_temp) + symbol + "\n" + "Max Temp: " + str(max_temp) + symbol +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

units=tk.IntVar()
c1=tk.Checkbutton(canvas, text="Metric", variable=units, onvalue=1, offvalue=0)
c1.pack()
textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', lambda event:getWeather(units))

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
