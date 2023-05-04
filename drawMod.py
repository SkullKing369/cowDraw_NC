'''
Author: Nate Crouch
Description: Python class module that uses data from a text file to draw objects.
GNU General Public License v3.0
'''
import turtle as t

class Draw:
    def fileDraw(self, row):
        global turtleLines
        if row[0]=="turtle":
            t.speed(int(row[1]))
            turtleLines = t.Screen()
            t.pensize(row[2])
            turtleLines.bgcolor(row[3])
            setting = row[4].split(",")
            turtleLines.setup(int(setting[0]), int(setting[1]))
        if row[0]=="go":
            newpos = row[1].split(",")
            t.up()
            t.setpos(float(newpos[0]),float(newpos[1]))
            t.down()
        if row[0]=="seth":
            t.seth(float(row[1]))
        if row[0]=="forward":
            t.forward(float(row[1]))
        if row[0]=="fillcolor":
            t.fillcolor(row[1])
        if row[0]=="pencolor":
            t.pencolor(row[1])
        if row[0]=="begin":
            t.begin_fill()
        if row[0]=="end":
            t.end_fill()
        if row[0]=="circle":
            t.circle(float(row[1]), float(row[2]))
        if row[0]=="reset":
            turtleLines.reset()
        if row[0]=="hide":
            t.hideturtle()
        return
