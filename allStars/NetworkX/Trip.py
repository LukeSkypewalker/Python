from scipy.spatial import distance

class Trip:

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.dist = distance.euclidean(src, dst)

    def display(self):
        print ("Src: ", self.src,  ", Dst: ", self.dst,  ", Dist: ", self.dist)



if __name__ == "__main__":


    from tkinter import *
    root = Tk()

    t1 = Trip((30,30), (1000,700))
    t2 = Trip((500,300), (3,4))
    t1.display()

    canv = Canvas(root, width=1200, height=800, bg="lightblue", cursor="pencil")
    canv.create_line(500, 200, 700, 600,width=1, arrow=LAST)
    canv.create_line(*t1.src, t1.dst, width=1, arrow=LAST)
    canv.create_line(*t2.src, t2.dst, width=1, arrow=LAST)

    canv.pack()
    root.mainloop()




