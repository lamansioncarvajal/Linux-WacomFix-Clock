from tkinter import *
from tkinter import *
from tkinter import ttk
import subprocess
import sys
from datetime import date
import time
root = Tk()
root.title('Clock&Fix')
root.wait_visibility(root)
root.attributes("-alpha", 0.66)
root.geometry('460x290')
root.configure(background="#282c34")

foreground="#abb2bf"
background="#282c34"
style = ttk.Style()

style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [0, 0, 0, 0],
                    "background" : background,
                    "foreground" : foreground },
        },
        "TFrame": {"configure": {"tabmargins": [0, 0, 0, 0],"background" : background,},
        },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1],"foreground": foreground, "background": background },
            "map":       {"background": [("selected", background)],
                          "expand": [("selected", foreground)] } } } )

style.theme_use("yummy")
parent_tab = ttk.Notebook(root)
tab1 = ttk.Frame(parent_tab)
tab2 = ttk.Frame(parent_tab)

nomdia = {
0: "Lunes ",
1: "Martes ",
2: "Miércoles ",
3: "Jueves ",
4: "Viernes ",
5: "Sábado ",
6: "Domingo "}
nommes = {
1: "Enero ",
2: "Febrero ",
3: "Marzo ",
4: "Abril ",
5: "Mayo ",
6: "Junio ",
7: "Julio ",
8: "Agosto ",
9: "Septiembre ",
10: "Octubre ",
11: "Noviembre ",
12: "Diciembre "
}
stylusid = 0
#slider0 = Scale(root, from_=1, to=2, length=50,resolution=1,showvalue=2, orient=HORIZONTAL, bg="#282c34", fg="#abb2bf", font = ("gothic"))
#slider0.set(1)
#slider0.pack(pady=2)
slider = Scale(tab2, from_=-10000, to=-1000, length=300,resolution=500,showvalue=-2000, orient=HORIZONTAL, bg="#282c34", fg="#abb2bf", font = ("gothic"))
slider.set(-3000)
def setAreaWacom():
	area1 = -10 * slider.get()
	area2 = -7 * slider.get()
	# * slider0.get()
	setstring = "0 0 "+str(area1)+" "+str(area2)
	subprocess.getoutput("xsetwacom set "+stylusid+" area "+setstring)
	subprocess.getoutput("xsetwacom set "+stylusid+" Rotate none")
	#if(slider0.get()==2):
		#subprocess.getoutput("xsetwacom set "+stylusid+" Rotate ccw")
	#else:
		#subprocess.getoutput("xsetwacom set "+stylusid+" Rotate none")
arrdevices = subprocess.getoutput("xsetwacom --list devices").split("\n")
for devstring in arrdevices:
	if "stylus" in devstring:
		stylusid = devstring.split()[8]
		thisarea = subprocess.getoutput("xsetwacom get "+stylusid+" area")
		currentval = thisarea.split()[3]
		check1 = int(currentval)%7
		if(check1 != 0):
			setAreaWacom()
button = Button(tab2, text="Set Sensibility", command=setAreaWacom, bg="#282c34", fg="#abb2bf", font = ("gothic"))
def tick():
	timestring = time.strftime("%H:%M:%S")
	clock.config(text=timestring)
	clock.after(200,tick)
def getdatime():
	dateobj = date.today()
	lbldate.config(text= nomdia[dateobj.weekday()] + str(dateobj.day) + "\n" + nommes[dateobj.month] + str(dateobj.year))
	lbldate.after(60000,getdatime)
def big():
    toggleSize(False)
def small():
    toggleSize(True)
def toggleSize(size):
    if(size):
        clock.config(font=("gothic",40))
        lbldate.config(font=("gothic",18))
        print("smallaf")
    else:
        clock.config(font=("gothic",77))
        lbldate.config(font=("gothic", 24))
        print("bigaf")
    clock.pack()
    lbldate.pack()
clock = Label(tab1, font = ("gothic",77, "bold"), bg="#282c34", fg="#abb2bf" )
clock.pack()
lbldate = Label(tab1, font = ("gothic",24, "bold"), bg="#282c34", fg="#abb2bf" )
lbldate.pack()
slider.pack(pady=10)
button.pack(pady=1)
sndbutton = Button(tab1, text="Small", command=small, bg="#282c34", fg="#abb2bf", font = ("gothic"))
trdbutton = Button(tab1, text="Big", command=big, bg="#282c34", fg="#abb2bf", font = ("gothic"))

tick()
getdatime()

button.pack()
sndbutton.pack()
trdbutton.pack()
parent_tab.add(tab1, text="Clock")
parent_tab.add(tab2, text="TabletSensibility")
parent_tab.pack(expand=1, fill='both')
root.mainloop()

Skip to content
Pull requests
Issues
Marketplace
Explore
@lamansioncarvajal
Learn Git and GitHub without any code!

Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
lamansioncarvajal /
Linux-WacomFix-Clock

1
0

    0

Code
Issues 0
Pull requests 0
Actions
Projects 0
Wiki
Security
Insights
Settings
Linux-WacomFix-Clock/

1

from tkinter import *

2

from tkinter import *

3

from tkinter import ttk

4

import subprocess

5

import sys

6

from datetime import date

7

import time

8

root = Tk()

9

root.title('Clock&Fix')

10

root.wait_visibility(root)

11

root.attributes("-alpha", 0.66)

12

root.geometry('460x290')

13

root.configure(background="#282c34")

14

​

15

foreground="#abb2bf"

16

background="#282c34"

17

style = ttk.Style()

18

​

19

style.theme_create( "yummy", parent="alt", settings={

20

        "TNotebook": {"configure": {"tabmargins": [0, 0, 0, 0],

21

                    "background" : background,

22

                    "foreground" : foreground },

23

        },

24

        "TFrame": {"configure": {"tabmargins": [0, 0, 0, 0],"background" : background,},

25

        },

26

        "TNotebook.Tab": {

27

            "configure": {"padding": [5, 1],"foreground": foreground, "background": background },

28

            "map":       {"background": [("selected", background)],

29

                          "expand": [("selected", foreground)] } } } )

30

​

31

style.theme_use("yummy")

32

parent_tab = ttk.Notebook(root)

33

tab1 = ttk.Frame(parent_tab)

34

tab2 = ttk.Frame(parent_tab)

35

​

36

nomdia = {

37

0: "Lunes ",

38

1: "Martes ",

39

2: "Miércoles ",

40

3: "Jueves ",

41

4: "Viernes ",

42

5: "Sábado ",

43

6: "Domingo "}

44

nommes = {

45

1: "Enero ",

46

2: "Febrero ",

47

3: "Marzo ",

48

4: "Abril ",

49

5: "Mayo ",

50

6: "Junio ",

@lamansioncarvajal
Commit changes
Commit summary
Optional extended description
Commit directly to the master branch.
Create a new branch for this commit and start a pull request. Learn more about pull requests.

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

