from tkinter import * 
from PIL import ImageTk, Image
from time import sleep

image_object = Image.open("imgs/chocolate_sauce/sjokolate_test.jpg")
basewidht = 500
wpercent = basewidht/float(image_object.size[0])
hsize = int(float(image_object.size[1])*float(wpercent))
img = image_object.resize((basewidht, hsize), Image.Resampling.LANCZOS)


root = Tk()
root.geometry(f"{basewidht}x{hsize}")

points = []

def callback(e):
   x= e.x
   y= e.y
   
   print("Pointer is currently at %d, %d" %(x,y))
   points.append((x,y))
   print(points)
   sleep(0.5)
   
root.bind('<Button-1>',callback)
canvas = Canvas(root, width=basewidht, height=hsize)
canvas.pack()

img = ImageTk.PhotoImage(img)
canvas.create_image(0,0, anchor=NW, image=img)
root.mainloop()