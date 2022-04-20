import WalkCycle
import tkinter


root = tkinter.Tk()

c = tkinter.Canvas(root, height=300, width=600, bg="white")

arc = c.create_arc(0, 0, WalkCycle.xPos, WalkCycle.yPos, fill="red")

c.pack()
root.mainloop()