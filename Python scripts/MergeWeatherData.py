#Import pandas library
import pandas as pnd
import os
import sys

#print(os.getcwd()) this will get the location of current directory
data_frm_humidity = pnd.read_csv('ProjectDataSets/humidity.csv')
data_frm_pressure = pnd.read_csv('ProjectDataSets/pressure.csv')
data_frm_temperature = pnd.read_csv('ProjectDataSets/temperature.csv')
data_frm_weather_description = pnd.read_csv('ProjectDataSets/weather_description.csv')
data_frm_wind_direction = pnd.read_csv('ProjectDataSets/wind_direction.csv')
data_frm_wind_speed = pnd.read_csv('ProjectDataSets/wind_speed.csv')
data_frm_City_Attributes = pnd.read_csv('ProjectDataSets/city_attributes.csv')
ls_FullHumidity=[]
ls_FullPressure=[]
ls_Fulltemperature = []
ls_Fullwind_direction = []
ls_Fullwind_speed = []
ls_Fullweather_description = []
ls_FullWeatherData = []
list_of_column_names = list(data_frm_humidity.columns)

print('List of column names : ',
      list_of_column_names)

for i in range(1,len(list_of_column_names)):
    for index_humidity, row_humidity in data_frm_humidity.iterrows():
        ls_FullHumidity.append([row_humidity[0], list_of_column_names[i],row_humidity[i]])                          
data_frm_FullWeatherData = pnd.DataFrame(ls_FullHumidity, columns=['TimeStamp','Locationa','Humidity'])

for i in range(1,len(list_of_column_names)):
    for index_pressure, row_pressure in data_frm_pressure.iterrows():
        ls_FullPressure.append(row_pressure[i])  
data_frm_FullWeatherData["Pressure"] =  ls_FullPressure    

for i in range(1,len(list_of_column_names)):
    for index_temperature, row_temperature in data_frm_temperature.iterrows():
        ls_Fulltemperature.append(row_temperature[i])  
data_frm_FullWeatherData["Temperature"] =  ls_Fulltemperature   

for i in range(1,len(list_of_column_names)):
    for index_wind_direction, row_wind_direction in data_frm_wind_direction.iterrows():
        ls_Fullwind_direction.append(row_wind_direction[i])  
data_frm_FullWeatherData["Wind Direction"] =  ls_Fullwind_direction

for i in range(1,len(list_of_column_names)):
    for index_wind_speed, row_wind_speed in data_frm_wind_speed.iterrows():
        ls_Fullwind_speed.append(row_wind_speed[i])  
data_frm_FullWeatherData["Wind Speed"] =  ls_Fullwind_speed

for i in range(1,len(list_of_column_names)):
    for index_weather_description, row_weather_description in data_frm_weather_description.iterrows():
        ls_Fullweather_description.append(row_weather_description[i])  
data_frm_FullWeatherData["Weather Description"] =  ls_Fullweather_description

data_frm_FullWeatherData.to_csv(os.getcwd()+'Tests/HourlyWeatherData_Merged.csv')  

print('File created successfully')