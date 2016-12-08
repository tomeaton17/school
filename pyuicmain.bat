@echo off
IF EXIST C:\Users\TomEaton\PycharmProjects\school\mainui.py del /F C:\Users\TomEaton\PycharmProjects\school\mainui.py 

pyuic5 -o C:\Users\TomEaton\PycharmProjects\school\mainui.py C:\Users\TomEaton\Documents\school\main.ui

