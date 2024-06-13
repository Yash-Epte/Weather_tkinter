import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

def get_weather(city):
    API_KEY = open("/Users/yashepte/Desktop/Weather/API_KEY","r").read()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error","City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temprature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(icon_url, temprature, description, city, country)

def search():
    city = city_name.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temprature, description, city, country = result
    location_lable.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_lable.configure(image=icon)
    icon_lable.image = icon

    temperature_lable.configure(text=f"Temperature :{temprature:.2f}°C")
    description_lable.configure(text=f"Description: {description}")

root = tk.Tk()
root.title("Weather Application")
root.geometry("500x500")

# creating input for the user
city_name = tk.Entry(root, font=("arial", 12))
city_name.pack(pady=10)

search_button = tk.Button(root, text="Search", command=search)
search_button.pack(pady=10)

location_lable = tk.Label(root, font=("arial", 25))
location_lable.pack(pady=20)

icon_lable = tk.Label(root)
icon_lable.pack()

temperature_lable = tk.Label(root, font=("arial", 20))
temperature_lable.pack()

description_lable = tk.Label(root, font=("arial", 20))
description_lable.pack()

root.mainloop()