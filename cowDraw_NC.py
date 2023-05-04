'''
Author:      Nate Crouch
Description: This application accesses a text file, reads it, and draws a regular and smaller cute cow
from the directions in said text file.
 GNU General Public License v3.0
''' 
import turtle as t
import pandas as pd
import os
import drawMod

while True:
    requestHelp = input("Would you like help with how the program works (Y/N): ")
    if not (requestHelp == "Y" or requestHelp == "y" or requestHelp == "N" or requestHelp == "n"):
        print("Invalid response, try again.")
        continue
    if (requestHelp == "N" or requestHelp == "n"):
        print("Okay, continuing...")
        break
    if (requestHelp == "Y" or requestHelp == "y"):
        print ('''This program will request you to enter a .txt file name, you can
               enter the name if it is in the folder or the file path if outside
               and the file will be used as instructions to draw something using
               turtle and the instruction's specifications must be seperated by
               !s to set up the turtle you must write turtle!(value for turtle speed)!
               (value for pensize)!(color name or hexdecimal code for said color)!
               (height value), (width value) for the turtle screen seperated by the ,
               , then for setpostion you must use go!(x value), (y value) also
               seperated by the , for begin_fill() and end_fill() will just be
               begin and end in that mannder for the commands, no !s needed for
               no value parameter containing commands, after that the other turtle
               commands will be called the same and the !s seperating the command
               and values needed.''')
        break

while True:
    file = input("Please enter file pathway or just filename in .txt format: ")
    if not (os.path.isfile(file)):
        print("Invalid input, try again.")
        continue
    else:
        break

data = pd.read_csv(file, sep="!", header=None)
cowDraw = drawMod.Draw()
for index, row in data.iterrows():
    cowDraw.fileDraw(row)
t.done()
