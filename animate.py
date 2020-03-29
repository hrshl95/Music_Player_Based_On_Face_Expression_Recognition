import tkinter
from PIL import Image,ImageTk, ImageSequence



class App:
    def __init__(self,parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=550, height=400)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                            Image.open("music-visualizer.gif")
                            )]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animating = True
        self.animate(0)

    def animate(self, counter):
        self.canvas.itemconfig(self.image,image=self.sequence[counter])
        if not self.animating:
            return
        self.parent.after(100, lambda: self.animate((counter+1)%len(self.sequence)))




root = tkinter.Tk()
app = App(root)
root.mainloop()
