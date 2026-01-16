import requests
from datetime import datetime ,timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os
from geopy.geocoders import Nominatim

#-----------------------------------------------------

if not os.path.exists('data'):
    os.makedirs('data')
    

#-----------------------------------------------------
cityname = input("enter the city name: ")
geolocator = Nominatim(user_agent="city_locator")
location = geolocator.geocode(cityname)
latitude = location.latitude
longitude = location.longitude

#-----------------------------------------------------

today = datetime.now()
weekAgo = today - timedelta(days=7)

startingDate = weekAgo.strftime("%Y-%m-%d")
endingDate = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={startingDate}&end_date={endingDate}&daily=temperature_2m_max,temperature_2m_min"

data = requests.get(url).json()
# print(data['daily']['time'])
# for i in range(7):
#   print(f"date: {data['daily']['time'][i]}")
#   print(f"max temp: {data['daily']['temperature_2m_max'][i]}")
#   print(f"min temp: {data['daily']['temperature_2m_min'][i]}")



#-----------------------------------------------------


dailyData = data['daily']

df = pd.DataFrame({
  'date': dailyData['time'],
  'maxTem': dailyData['temperature_2m_max'],
  'minTem': dailyData['temperature_2m_min']
})

df["date"] = pd.to_datetime(df["date"])
print(df)


#-----------------------------------------------------


plt.figure(figsize=(10,5))
plt.plot(df["date"], df["maxTem"], marker='o', label='Max Temperature')
plt.plot(df["date"], df["minTem"], marker='o', label='Min Temperature')

plt.title(f'{cityname} -Temperature Over the Past Week')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig(f'data/{cityname}_temperature_last_week.png')
plt.show()


#-----------------------------------------------------


df.to_csv(f'data/{cityname}_temperature_last_week.csv', index=False)
print("data save succesfully")


