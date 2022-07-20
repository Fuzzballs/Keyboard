from tkinter import *
#Bro the "tk(className=)" thing is to literally JUST name the window.  
#It doest do anything!
root = Tk(className="Literlly this is just to name it")
root.geometry("350x150")
#10 number buttons
numButton1 = Button(root, text="1", padx=5)
numButton2 = Button(root, text="2", padx=5)
numButton3 = Button(root, text="3", padx=5)
numButton4 = Button(root, text="4", padx=5)
numButton5 = Button(root, text="5", padx=5)
numButton6 = Button(root, text="6", padx=5)
numButton7 = Button(root, text="7", padx=5)
numButton8 = Button(root, text="8", padx=5)
numButton9 = Button(root, text="9", padx=5)
numButton10 = Button(root, text="0", padx=5)
#10 first letter row
fLetterButton1 = Button(root, text="Q")
fLetterButton2 = Button(root, text="W")
fLetterButton3 = Button(root, text="E")
fLetterButton4 = Button(root, text="R")
fLetterButton5 = Button(root, text="T")
fLetterButton6 = Button(root, text="Y")
fLetterButton7 = Button(root, text="U")
fLetterButton8 = Button(root, text="I")
fLetterButton9 = Button(root, text="O")
fLetterButton10 = Button(root, text="P")
#9 second letter row
mLetterButton1 = Button(root, text="A")
mLetterButton2 = Button(root, text="S")
mLetterButton3 = Button(root, text="D")
mLetterButton4 = Button(root, text="F")
mLetterButton5 = Button(root, text="G")
mLetterButton6 = Button(root, text="H")
mLetterButton7 = Button(root, text="J")
mLetterButton8 = Button(root, text="K")
mLetterButton9 = Button(root, text="L")
#7 third button row
lastButtonRow1 = Button(root, text="Z")
lastButtonRow2 = Button(root, text="X")
lastButtonRow3 = Button(root, text="C")
lastButtonRow4 = Button(root, text="V")
lastButtonRow5 = Button(root, text="B")
lastButtonRow6 = Button(root, text="N")
lastButtonRow7 = Button(root, text="M")
#Space bar
spaceBar = Button(root, text=" ", padx=50)

#Placing the keys on the screen

#Placing the numbers row
numButton1.grid(row=0, column=0)
numButton2.grid(row=0, column=1)
numButton3.grid(row=0, column=2)
numButton4.grid(row=0, column=3)
numButton5.grid(row=0, column=4)
numButton6.grid(row=0, column=5)
numButton7.grid(row=0, column=6)
numButton8.grid(row=0, column=7)
numButton9.grid(row=0, column=8)
numButton10.grid(row=0, column=9)

#Placing the first row 
fLetterButton1.grid(row=1, column=0)
fLetterButton2.grid(row=1, column=1)
fLetterButton3.grid(row=1, column=2)
fLetterButton4.grid(row=1, column=3)
fLetterButton5.grid(row=1, column=4)
fLetterButton6.grid(row=1, column=5)
fLetterButton7.grid(row=1, column=6)
fLetterButton8.grid(row=1, column=7)
fLetterButton9.grid(row=1, column=8)
fLetterButton10.grid(row=1, column=9)

#Placing the second row
mLetterButton1.grid(row=2, column=0)
mLetterButton1.grid(row=2, column=1)
mLetterButton1.grid(row=2, column=2)
mLetterButton1.grid(row=2, column=3)
mLetterButton1.grid(row=2, column=4)
mLetterButton1.grid(row=2, column=5)
mLetterButton1.grid(row=2, column=6)
mLetterButton1.grid(row=2, column=7)
mLetterButton1.grid(row=2, column=8)

#Placing the third row
lastButtonRow1.grid(row=3, column=0)
lastButtonRow1.grid(row=3, column=1)
lastButtonRow1.grid(row=3, column=2)
lastButtonRow1.grid(row=3, column=3)
lastButtonRow1.grid(row=3, column=4)
lastButtonRow1.grid(row=3, column=5)
lastButtonRow1.grid(row=3, column=6)

#Placing space bar
spaceBar.grid(row=4, column=4)

root.mainloop() 