from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageGrab

class main:
    def __init__(self,master):
        self.master = master
        #create variables for the colors
        self.pen_color = 'black'
        self.background_color = 'white'
        self.eraser_color = self.background_color

        #setting the cordinates of x and y to none until a function is called
        self.old_x = None
        self.old_y = None
        #setting the width of the eraser and the pen
        self.eraserwidth = 1
        self.penwidth = 1
        #calling the two functions for the menu and pen/eraser sliders
        self.draw_sliders()
        self.create_menu()
        #setting a bind to call the paint function
        self.c.bind('<B1-Motion>',self.paint)
        #setting a bind to call the reset function
        self.c.bind('<ButtonRelease-1>',self.reset)
        #setting a bind to call the eraser function
        self.c.bind('<B3-Motion>', self.erase)
        #setting a bind to call the reset function
        self.c.bind('<ButtonRelease-3>',self.reset)

    #function to set the width of the pen
    def change_pen_width(self, current_scale):
        #sets the width to the matching one from the scale (scales from 5 to 100)
        self.penwidth = current_scale

    #function to draw 
    def paint(self, current):
        if self.old_x and self.old_y:
            #using "create_line" function to draw from x,y to x1,y2, giving the penwidth, color
            self.c.create_line(self.old_x, self.old_y, current.x, current.y, width=self.penwidth, fill=self.pen_color, capstyle=ROUND, smooth=True)
        
        #replacing every cordinate of the line
        #every time it changes it starts "from the begging (current.x, current.y)"
        self.old_x = current.x
        self.old_y = current.y

    #function to set the width of the eraser
    def change_eraser_width(self, current_scale):
        #sets the width to the matching one from the scale (scales from 5 to 100)
        self.eraserwidth = current_scale

    #function to erase
    def erase(self, current):
        if self.old_x and self.old_y:
            #using "create_line" function to erase from x,y to x1,y2, giving the penwidth and the background color so that we can "delete" it
            self.c.create_line(self.old_x, self.old_y, current.x, current.y, width=self.eraserwidth, fill=self.eraser_color, capstyle=ROUND, smooth = TRUE)

        #replacing every cordinate of the line
        #every time it changes it starts "from the begging (current.x, current.y)"
        self.old_x = current.x
        self.old_y = current.y

    #function to reset the cordinates of the last line we drew
    #and set to none 
    def reset(self, last_cordinates):
        self.old_x = None
        self.old_y = None  

    #function to save the image
    def save(self):
        #using filedialog function - gives us an option to choose
        #where to save the image and the name of it
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png')])
        if file:
            #
            x = self.master.winfo_rootx() + self.c.winfo_x()
            y = self.master.winfo_rooty() + self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png')

    #function to clear da canvas
    def clear_canvas(self):
        self.c.delete(ALL)

    #function to change colors
    def change_pen_color(self):
        #set the pen color to the color we chose from the colorchooser menu
        self.pen_color=colorchooser.askcolor(color=self.pen_color)[1]
    #function to change background color
    def change_bg_color(self):
        self.background_color = colorchooser.askcolor(color = self.background_color)[1]
        self.c['bg'] = self.background_color
        self.eraser_color = self.background_color
    #function to draw our widgets
    def draw_sliders(self):
        #we make a frame around the canvas
        self.controls = Frame(self.master,padx = 5,pady = 5)
        #adding text to the frame and decide on what row/column it would be
        Label(self.controls, text='Pen Width: ',font=('',15)).grid(row=0,column=0)
        #create a slider using Scale function from ttk module
        #giving it a range from 5 to 100 px, call the change_pen_width function
        #set the slider to be horizontal/vertical
        self.slider = ttk.Scale(self.controls,from_ = 1, to = 100, command=self.change_pen_width,orient=HORIZONTAL)
        #set the penwidth depending on the slider
        self.slider.set(self.penwidth)
        #placing it in the frame
        self.slider.grid(row=1,column=0,ipady=10)

        #same as above but with the eraser
        Label(self.controls, text='Eraser Width: ',font=('',15)).grid(row=0,column=50)
        self.slider = ttk.Scale(self.controls,from_= 1, to = 100, command=self.change_eraser_width,orient=HORIZONTAL)
        self.slider.set(self.eraserwidth)
        self.slider.grid(row=1,column=50,ipady=10)
        self.controls.pack()

    def create_menu(self):
        #creating the canvas
        self.c = Canvas(self.master,width=1280,height=720,bg=self.background_color)
        self.c.pack(expand=False)

        #create menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        filemenu = Menu(menu, tearoff=0)
        #adding cascade
        menu.add_cascade(label='File',menu=filemenu)
        #adding "Save as" label and calling the save function
        filemenu.add_command(label='Save as',command=self.save)

        #same as above
        colormenu = Menu(menu, tearoff=0)  
        menu.add_cascade(label='Colors',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=self.change_pen_color)
        colormenu.add_command(label = 'Background color', command = self. change_bg_color)

        #same as above
        optionmenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=self.clear_canvas)
        optionmenu.add_command(label='Exit',command=self.master.destroy) 
        
#main
if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Photopaint')
    root.mainloop()