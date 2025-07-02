import requests 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


API_KEY = "84382eabb146538a4b2fb8346942057e" 
CITY = "Mumbai"           
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(URL)
data = response.json()

if data["cod"] != "200":
    print("❌ Failed to retrieve data:", data)
    exit()


forecast_list = data["list"]

weather_data = {
    "Datetime": [],
    "Temperature (°C)": [],
    "Humidity (%)": [],
    "Weather": [],
}

for entry in forecast_list:
    weather_data["Datetime"].append(entry["dt_txt"])
    weather_data["Temperature (°C)"].append(entry["main"]["temp"])
    weather_data["Humidity (%)"].append(entry["main"]["humidity"])
    weather_data["Weather"].append(entry["weather"][0]["main"])

df = pd.DataFrame(weather_data)
df["Datetime"] = pd.to_datetime(df["Datetime"])


plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x="Datetime", y="Temperature (°C)", label="Temperature", marker="o")
sns.lineplot(data=df, x="Datetime", y="Humidity (%)", label="Humidity", marker="x")
plt.xticks(rotation=45)
plt.title(f"Weather Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Values")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("output.png")
plt.show()
