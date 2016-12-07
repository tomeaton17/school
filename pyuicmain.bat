@echo off
IF EXIST C:\Users\TomEaton\PycharmProjects\school\test.py del /F C:\Users\TomEaton\PycharmProjects\school\test.py 

pyuic5 -o C:\Users\TomEaton\PycharmProjects\school\test.py C:\Users\TomEaton\Documents\school\main.ui

