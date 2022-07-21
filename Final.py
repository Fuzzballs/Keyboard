from sqlite3 import Row
from tkinter import *
#Bro the "tk(className=)" thing is to literally JUST name the window.  
#It doest do anything!
root = Tk(className="Literlly this is just to name it")
#Lines 7, 8 and 9 make it so the space bars dont seperate the columns.
#Now I cant change the pad=x of the spacebar
root.rowconfigure(4, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(5, weight=1)
root.geometry("250x150")
#What each button will print out, it will all print in the same location,
#it will print and delete the last thing typed
def myClick1():
    myLabel1 = Label(root, text="1")
    myLabel1.grid(row=5, column=4)
def myClick2():
    myLabel2 = Label(root, text='2')
    myLabel2.grid(row=5, column=4)
def myClick3():
    myLabel3 = Label(root, text='3')
    myLabel3.grid(row=5, column=4)
def myClick4():
    myClick4 = Label(root, text='4')
    myClick4.grid(row=5, column=4)
def myClick5():
    myClick5 = Label(root, text='5')
    myClick5.grid(row=5, column=4)
def myClick6():
    myClick6 = Label(root, text='6')
    myClick6.grid(row=5, column=4)
def myClick7():
    myClick7 = Label(root, text='7')
    myClick7.grid(row=5, column=4)
def myClick8():
    myClick8 = Label(root, text='8')
    myClick8.grid(row=5, column=4)
def myClick9():
    myClick9 = Label(root, text='9')
    myClick9.grid(row=5, column=4)
def myClick0():
    myClick0 = Label(root, text='0')
    myClick0.grid(row=5, column=4)
def myClickQ():
    myClickQ = Label(root, text='Q')
    myClickQ.grid(row=5, column=4)
def myClickW():
    myClickW = Label(root, text='W')
    myClickW.grid(row=5, column=4)
def myClickE():
    myClickE = Label(root, text='E')
    myClickE.grid(row=5, column=4)
def myClickR():
    myClickR = Label(root, text='R')
    myClickR.grid(row=5, column=4)
def myClickT():
    myClickT = Label(root, text='T')
    myClickT.grid(row=5, column=4)
def myClickY():
    myClickY = Label(root, text='Y')
    myClickY.grid(row=5, column=4)
def myClickU():
    myClickU = Label(root, text='U')
    myClickU.grid(row=5, column=4)
def myClickI():
    myClickI = Label(root, text='I')
    myClickI.grid(row=5, column=4)
def myClickO():
    myClickO = Label(root, text='O')
    myClickO.grid(row=5, column=4)
def myClickP():
    myClickP = Label(root, text='P')
    myClickP.grid(row=5, column=4)
def twoClickA():
    twoClickA = Label(root, text='A')
    twoClickA.grid(row=5, column=4)
def twoClickS():
    twoClickS = Label(root, text='S')
    twoClickS.grid(row=5, column=4)
def twoClickD():
    twoClickD = Label(root, text='D')
    twoClickD.grid(row=5, column=4)
def twoClickF():
    twoClickF = Label(root, text='F')
    twoClickF.grid(row=5, column=4)
def twoClickG():
    twoClickG = Label(root, text='G')
    twoClickG.grid(row=5, column=4)
def twoClickH():
    twoClickH = Label(root, text='H')
    twoClickH.grid(row=5, column=4)
def twoClickJ():
    twoClickJ = Label(root, text='J')
    twoClickJ.grid(row=5, column=4)
def twoClickK():
    twoClickK = Label(root, text='K')
    twoClickK.grid(row=5, column=4)
def twoClickL():
    twoClickL = Label(root, text='L')
    twoClickL.grid(row=5, column=4)
def threeClickZ():
    threeClickZ = Label(root, text='Z')
    threeClickZ.grid(row=5, column=4)
def threeClickX():
    threeClickX = Label(root, text='X')
    threeClickX.grid(row=5, column=4)
def threeClickC():
    threeClickC = Label(root, text='C')
    threeClickC.grid(row=5, column=4)
def threeClickV():
    threeClickV = Label(root, text='V')
    threeClickV.grid(row=5, column=4)
def threeClickB():
    threeClickB = Label(root, text='B')
    threeClickB.grid(row=5, column=4)
def threeClickN():
    threeClickN = Label(root, text='N')
    threeClickN.grid(row=5, column=4)
def threeClickM():
    threeClickM = Label(root, text="M")
    threeClickM.grid(row=5, column=4)


    #10 number buttons
numButton1 = Button(root, text="1", padx=5, command=myClick1)
numButton2 = Button(root, text="2", padx=5, command=myClick2)
numButton3 = Button(root, text="3", padx=5, command=myClick3)
numButton4 = Button(root, text="4", padx=5, command=myClick4)
numButton5 = Button(root, text="5", padx=5, command=myClick5)
numButton6 = Button(root, text="6", padx=5, command=myClick6)
numButton7 = Button(root, text="7", padx=5, command=myClick7)
numButton8 = Button(root, text="8", padx=5, command=myClick8)
numButton9 = Button(root, text="9", padx=5, command=myClick9)
numButton10 = Button(root, text="0", padx=5, command=myClick0)
#10 first letter row
fLetterButton1 = Button(root, text="Q", command=myClickQ)
fLetterButton2 = Button(root, text="W", command=myClickW)
fLetterButton3 = Button(root, text="E", command=myClickE)
fLetterButton4 = Button(root, text="R", command=myClickR)
fLetterButton5 = Button(root, text="T", command=myClickT)
fLetterButton6 = Button(root, text="Y", command=myClickY)
fLetterButton7 = Button(root, text="U", command=myClickU)
fLetterButton8 = Button(root, text="I", command=myClickI)
fLetterButton9 = Button(root, text="O", command=myClickO)
fLetterButton10 = Button(root, text="P", command=myClickP)
#9 second letter row
mLetterButton1 = Button(root, text="A", command=twoClickA)
mLetterButton2 = Button(root, text="S", command=twoClickS)
mLetterButton3 = Button(root, text="D", command=twoClickD)
mLetterButton4 = Button(root, text="F", command=twoClickF)
mLetterButton5 = Button(root, text="G", command=twoClickG)
mLetterButton6 = Button(root, text="H", command=twoClickH)
mLetterButton7 = Button(root, text="J", command=twoClickJ)
mLetterButton8 = Button(root, text="K", command=twoClickK)
mLetterButton9 = Button(root, text="L", command=twoClickL)
#7 third button row
lastButtonRow1 = Button(root, text="Z", command=threeClickZ)
lastButtonRow2 = Button(root, text="X", command=threeClickX)
lastButtonRow3 = Button(root, text="C", command=threeClickC)
lastButtonRow4 = Button(root, text="V", command=threeClickV)
lastButtonRow5 = Button(root, text="B", command=threeClickB)
lastButtonRow6 = Button(root, text="N", command=threeClickN)
lastButtonRow7 = Button(root, text="M", command=threeClickM)
#Space bar
spaceBar = Button(root, text=" ", padx=50)
spaceBar2 = Button(root, text=" ", padx=50)
spaceBar3 = Button(root, text=" ", padx=50)

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
mLetterButton2.grid(row=2, column=1)
mLetterButton3.grid(row=2, column=2)
mLetterButton4.grid(row=2, column=3)
mLetterButton5.grid(row=2, column=4)
mLetterButton6.grid(row=2, column=5)
mLetterButton7.grid(row=2, column=6)
mLetterButton8.grid(row=2, column=7)
mLetterButton9.grid(row=2, column=8)

#Placing the third row
lastButtonRow1.grid(row=3, column=1)
lastButtonRow2.grid(row=3, column=2)
lastButtonRow3.grid(row=3, column=3)
lastButtonRow4.grid(row=3, column=4)
lastButtonRow5.grid(row=3, column=5)
lastButtonRow6.grid(row=3, column=6)
lastButtonRow7.grid(row=3, column=7)

#Placing space bar
spaceBar.grid(row=4, column=4)
spaceBar2.grid(row=4, column=3)
spaceBar3.grid(row=4, column=5)

root.mainloop() 
