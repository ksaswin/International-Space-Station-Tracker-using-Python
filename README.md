#### Track the International Space Station using Python

This project tracks the International Space Station using API provided by [*Open-Notify*](http://open-notify.org/).<br />
It shows you the location of ISS in a map.
You can also see your location and the next closest time at which the ISS is going to be passing over you in the same map.
For that to work, you will have to hard-code your location.
By default, the location is set to the GPS co-ordinates of NASA.

To change it to your co-ordinates, first find your co-ordinates and paste them in lines **48** and **49** of the code.<br />
Paste your latitude in **__my_lat = float(__** *your latitude goes here* **__)__**    Line 48 in the code<br />
Paste your longitude in **__my_lon = float(__** *your longitude goes here* **__)__**    Line 49 in the code<br />

Clone the repository using:
```
git clone https://github.com/ksaswin/International-Space-Station-Tracker-using-Python.git
```
You may need to install a few additional Python libraries for the project.<br/>
Run the following commands in your terminal to install the additional libraries.
```
sudo apt install python3-tk
```
```
pip3 install urllib3
```
