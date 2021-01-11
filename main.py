import urllib.request
from datetime import datetime
import time
import turtle
import json


def callPassTime(my_lat, my_lon, presenttime):
    # Finding all the pass times over your specified location
    url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(my_lat) + '&lon=' + str(my_lon)
    passtime = json.loads(urllib.request.urlopen(url).read())
    indexMax = len(passtime['response'])
    for i in range(indexMax):
        timestamp = passtime['response'][i]['risetime']
        if(timestamp > presenttime):
            break
    passdict = {"Timestamp": timestamp, "MaxIndex": indexMax}
    return passdict


# Prints the names of all the astronauts currentl in International Space Station
astro_url = 'http://api.open-notify.org/astros.json'
astro_data = json.loads(urllib.request.urlopen(astro_url).read())
num = astro_data["number"]
astrofile = open("astronauts_data.txt", "a")
astrofile.write("Program executed on: " + str(datetime.fromtimestamp(datetime.timestamp(datetime.now()))) + "\n")
astrofile.write("Number of astronauts on board: " + str(num) + "\n")
astrofile.write("Astronauts on board:\n")
for astronaut in range(astro_data["number"]):
    print(astro_data["people"][astronaut]["name"])
    astrofile.write("\t" + astro_data["people"][astronaut]["name"] + "\n")
astrofile.write("\n\n")
astrofile.close()

# Setting up the sreen
screen = turtle.Screen()
screen.setup(1392, 696)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('world-map.png')
screen.register_shape('iss_icon.gif')

iss = turtle.Turtle()
iss.shape("iss_icon.gif")
iss.penup()

# GPS coordinates of NASA, United States. Latitude: 38.8765 Longitude: -77.0098
# To find if the ISS is going to be passing over you or any other specific location of your choice
my_lat = float(38.8765)       # Custom latitude here
my_lon = float(-77.0098)      # Custom longitude here

my_loc = turtle.Turtle()
my_loc.penup()
my_loc.color('yellow')
my_loc.goto(my_lon, my_lat)
my_loc.dot(5)
my_loc.hideturtle()

presenttime = datetime.timestamp(datetime.now())
passtimeDict = callPassTime(my_lat, my_lon, presenttime)
passtime = datetime.fromtimestamp(passtimeDict["Timestamp"])
my_loc.write(passtime)

while True:
    # Real-time location of International Space Station
    astro_url = 'http://api.open-notify.org/iss-now.json'
    location_data = json.loads(urllib.request.urlopen(astro_url).read())
    longitude = location_data['iss_position']['longitude']
    latitude = location_data['iss_position']['latitude']
    print('Longitude = ', longitude, end=' and ')
    print('Latitude = ', latitude)
    iss.goto(float(longitude), float(latitude))
    
    presenttime = datetime.timestamp(datetime.now())
    if presenttime > passtimeDict["Timestamp"]:
        passtimeDict = callPassTime(my_lat, my_lon, presenttime)
        passtime = datetime.fromtimestamp(passtimeDict["Timestamp"])
        my_loc.write(passtime)
    
    time.sleep(10)

