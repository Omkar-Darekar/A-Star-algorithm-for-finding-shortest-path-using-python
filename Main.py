import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

#root = tk.Tk()
T = Tkinter.Text(top, height=2, width=300)
T.pack()
T.insert(Tkinter.END, "FINDING SHORTEST DISTANCE PATH AND OBJECT DETECTION AND AVOIDANCE USING IMAGE PROCESSING AND ARTIFICIAL INTELLIGENCE \n\n\n")

top.title("Final Year Project")
top.geometry('1080x500')

def AStarSample():
   os.system('python "/home/omkar/Documents/KartikBhaiyaaNewCode/omkar/Pratik/AStarSample/AStarSample.py"')
D = Tkinter.Button(top, text ="A Star Sample", command = AStarSample)
D.pack()


def WorkingOfAstar():
   os.system('python "/home/omkar/Documents/KartikBhaiyaaNewCode/omkar/Pratik/Working Of A star/main.py"')
C = Tkinter.Button(top, text ="Working of A Star", command = WorkingOfAstar)



def helloCallBack():
    os.system('python A_star.py')
B=Tkinter.Button(top,text="Main Code",command= helloCallBack)
B.pack()
C.pack()

top.mainloop()
