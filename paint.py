from tkinter import *

#window
root = Tk()
root.title("Photopaint")
root.geometry("1280x720")

#label
mainLabel = Label(root, text="Photopaint")
mainLabel.pack()


#frames
topframe = Frame(root)
topframe.pack()
botframe = Frame(root)
botframe.pack(side = BOTTOM)

#buttons
button1 = Button(topframe, text="brush", fg="grey")
button1.pack(side = LEFT)
button2 = Button(topframe, text="pencil", fg="grey")
button2.pack(side = LEFT)
button3 = Button(topframe, text="eraser", fg="grey")
button3.pack(side = LEFT)
s

root.mainloop()