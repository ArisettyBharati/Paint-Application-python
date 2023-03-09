from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from turtle import bgcolor

window= Tk()
window.geometry("1276x651")
window.title("Paint Application")
window.resizable(False,False)
window.config(bg="#1C1C1C")

#Variable
pen_color="black"
eraser_color="white"

#Canvas
canvas = Canvas (window, bg="white", bd=5, relief=GROOVE, height=525, width=1225)
canvas.place(x=15,y=90)

# Functions
def canvas_color():
    global eraser_color
    color=colorchooser.askcolor()
    canvas.configure(bg=color[1])
    eraser_color=color[1]

def eraser():
    global pen_color
    pen_color = eraser_color

def clear():
    canvas.delete("all")

DEFAULT_COLOR = 'black'
def choose_color():
        color = colorchooser.askcolor()
        colour=color[1]
        select_color(colour)

def paint (event):
    x1,y1=(event.x-2), (event.y-2)
    x2,y2 =(event.x+2), (event.y+2)
    canvas.create_oval (x1,y1,x2,y2, fill=pen_color, outline=pen_color,width=size_label.get())

current_x, current_y = 0,0
color = 'black'
def locate_xy(event):
    global current_x, current_y
    current_x, current_y= event.x, event.y
def addLine(event):
    global current_x, current_y
    canvas.create_line((current_x,current_y,event.x,event.y), fill= pen_color,width=size_label.get())
    current_x, current_y= event.x, event.y
canvas.bind("<Button-1>", locate_xy)
canvas.bind('<B1-Motion>',addLine)

def select_color(col):
    global pen_color
    pen_color=col

# Frame
color_frame=LabelFrame (window, text="Color",labelanchor="s",bd=0, relief=RIDGE, bg="#262626", font=("Courier New",12),fg="white")
color_frame.place(x=20,y=15, width=480,height=53)

tool_frame =LabelFrame (window, text="Tool",labelanchor="s",bd=0, relief=RIDGE, bg="#262626", font=("Courier New",12),fg="white") 
tool_frame.place(x=520,y=15, width=300,height=53)

size_label = LabelFrame (window, text="Size",labelanchor="s",bd=0, relief=RIDGE, bg="#262626", font =("Courier New",12),fg="white")
size_label.place (x=840,y=15, width=170,height=53)

colors= ["#FF0000", "#008000","#FFCOCB", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#A52A2A", "#FFFFFF","#000000", "#808080", "#87CEEB"]

#Button
i=j=0
for color in colors:
    Button(color_frame,bd=3, bg=color, relief=RIDGE, width=3,borderwidth=0, command=lambda col=color:select_color(col)).grid(row=j,column=i,padx=2,pady=8)
    i= i+1

#Tool_Button
multi_photo= PhotoImage(file="multicolor.png")
multi_col=Button(color_frame,image=multi_photo,bd=0,command=lambda col=color[1]:choose_color())
multi_col.grid(row=0, column=13, padx=2)

canvas_color_b1 =Button(tool_frame, text="fill", bg="white", command=canvas_color)
canvas_color_b1.grid(row=0, column=8, padx=2)

eraser_b2 =Button (tool_frame, text="Eraser", bg="white", command=eraser)
eraser_b2.grid(row=0, column=2, padx=2)

clear_b3=Button(tool_frame, text="Clear", bg="white", command=clear)
clear_b3.grid(row=0, column=12, padx=2)

#scale from tkk
current_value = DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
# label for slider
slider_label = ttk.Label(size_label,text='Slider:', font =("Courier New",8))
slider_label.config(background="#262626",foreground="white")
slider_label.grid(column=0,row=0,sticky='nw')
#  slider
size_label = ttk.Scale(size_label,from_=0,to=10,orient='horizontal', variable=current_value)

size_label.grid(column=1,row=0,sticky='ew')

window.mainloop()