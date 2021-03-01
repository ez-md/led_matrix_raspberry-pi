# YouTube Live Subsciber Counter 
This uses a raspberry pi and an LED Matrix to display subscriber count of YouTube account. 

It can also be used to view any messages.

In my example, it shows a one time welcome message, current time, YouTube Channel name and the subscriber count.Then it loops back to the time. 


![picture of LED Matrix](pix/pix.gif)
## Required 
+ Python3
+ pip
+ any Raspberry pi with Raspbian installed
+ LED matrix [Like this one](https://www.amazon.com/HiLetgo-MAX7219-Arduino-Microcontroller-Display/dp/B07FFV537V?ref_=ast_sto_dp)

## Pi Wiring
 
| Board Pin	| Name	| Remarks	|RPi Pin |	RPi Function
|-----|------|------| -----|-----|
|1	|VCC	|+5V Power	|2	|5V0
|2	|GND	|Ground	|6	|GND
|3	|DIN	|Data In	|19	|GPIO 10 (MOSI)
|4	|CS	|Chip Select	|24	|GPIO 8 (SPI CE0)
|5	|CLK	|Clock	|23	|GPIO 11 (SPI CLK)

## Pre-requisites

### Enable the SPI driver for the LED Matrix module to work.
	sudo raspi-config

	Scroll down to `Advanced Options` (`Interfacing Options` on the Pi Zero) and press enter.
	Scroll down to `SPI`, press enter, and select `yes`.
	
	sudo reboot


### Install Dependencies

```
sudo usermod -a -G spi,gpio pi
sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5
sudo -H pip install --upgrade luma.led_matrix
```
## Running the Program
```
python3 led_matrix_youtube.py
```
Make sure to set the name (channel ID) and key variable.
Google API key is free and easy to obtain [Guide Here](https://www.slickremix.com/docs/get-api-key-for-youtube/)

##  Running on Startup
to sun the scripy on startup modify corontab

```
sudo crontob -e
```
at the bottom of the file add (change path)
```
@reboot python <path to the python file> &

sudo reboot
```


Have Fun!!

credits: 
https://luma-led-matrix.readthedocs.io/en/latest/index.html

