import requests
#import os
from datetime import datetime

api_key="a4537e89117ee35a14a2919a60982265"
location=input("Enter the City Name: ")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data= api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

stats="Weather Stats for - {}  || {}".format(location.upper(), date_time)
temp="Current temperature is: {:.2f} deg C".format(temp_city)
weather="Current weather desc  :",weather_desc
humidity="Current Humidity      :",hmdt, '%'
wind="Current wind speed    :",wind_spd ,'kmph'

print ("-------------------------------------------------------------")
print (stats)
print ("-------------------------------------------------------------")

print (temp)
print (weather)
print (humidity)
print (wind)

file=open("project.txt","w")
file.write("-------------------------------------------------------------")
file.write('\n')
file.write(stats)
file.write('\n')
file.write("-------------------------------------------------------------")
file.write('\n')
file.write(temp)
file.write('\n')
file.write(str(weather) )
file.write('\n')
file.write(str(humidity))
file.write('\n')
file.write(str(wind))
file.close()


