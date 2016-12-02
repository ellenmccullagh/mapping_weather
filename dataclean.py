import weather

list_of_report = weather.get_weather()
f = open("data_raw.csv", 'w')
f.write('City,State,Code,Location,Full,Day,Month,Year,Precipitation,Max Temp,Avg Temp,Min Temp,High Gust,Avg Wind,High Wind,Rain,Fog,Thunderstorm,Snow,Sleet\n')

for observation in list_of_report:
    row = ''
    row += str(observation['Station']['City']).strip()
    row += ','
    row += str(observation['Station']['State']).strip()
    row += ','
    row += str(observation['Station']['Code']).strip()
    row += ','
    row += '"{}"'.format(str(observation['Station']['Location']).strip())
    row += ','
    row += str(observation['Date']['Full'])
    row += ','
    row += str(observation['Date']['Day'])
    row += ','
    row += str(observation['Date']['Month'])
    row += ','
    row += str(observation['Date']['Year'])
    row += ','
    row += str(observation['Data']['Precipitation'])
    row += ','
    row += str(observation['Data']['Temperature']['Max Temp'])
    row += ','
    row += str(observation['Data']['Temperature']['Avg Temp'])
    row += ','
    row += str(observation['Data']['Temperature']['Min Temp'])
    row += ','
    row += str(observation['Data']['Wind']['High Gust'])
    row += ','
    row += str(observation['Data']['Wind']['Avg Wind'])
    row += ','
    row += str(observation['Data']['Wind']['High Wind'])
    row += ','
    rain = False
    fog = False
    thunderstorm = False
    snow = False
    sleet = False
    if "RAIN" in observation['Weather Conditions']:
        rain = True
    if "FOG" in observation['Weather Conditions']:
        fog = True
    if "THUNDERSTORM" in observation['Weather Conditions']:
        thunderstorm = True
    if "SNOW" in observation['Weather Conditions']:
        snow = True
    if "SLEET" in observation['Weather Conditions']:
        sleet = True
    row += str(rain)
    row += ','
    row += str(fog)
    row += ','
    row += str(thunderstorm)
    row += ','
    row += str(snow)
    row += ','
    row += str(sleet)
    row += '\n'
    f.write(row)
f.close()
