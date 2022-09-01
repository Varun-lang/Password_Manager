from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

#Function Space

def inputs():
    a=inp1.get()
    b=inp2.get()
    c=inp3.get()
    if(a=="" or c==""):
        messagebox.showwarning(title="Oops!",message="Don't leave any field empty.")
    else:
        okay=messagebox.askokcancel(title=f"{a} says",message=f"These are the details: \nEmail: {b}\nPassword: {c}\nIs it Okay?")
        if okay:
            adds(a)
            sym()
            adds(b)
            sym()
            adds(c)
            br()
            clr(inp1,inp2,inp3)  

def adds(k):
    f=open("data.txt","a")
    f.write(k)
    f.close()

def sym():
    f=open("data.txt","a")
    f.write(" | ")
    f.close()

def br():
    f=open("data.txt","a")
    f.write("\n")
    f.close()

def clr(*args):
    for i in args:
        i.delete(0,END)

#Generate Password
def genp():
    v=inp3
    v.delete(0,END)
    sm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sy = ['#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    dg = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    psm = [choice(sm) for _ in range(randint(3,5))]
    psy = [choice(sy) for _ in range(randint(2,4))]
    pdg = [choice(dg) for _ in range(randint(2,4))]

    fp=psm+psy+pdg
    shuffle(fp)

    pas=""
    for char in fp:
        pas+=char

    inp3.insert(0,pas)
    pyperclip.copy(pas) #auto-copy


window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=250,height=250)
img=PhotoImage(file='31.png')
canvas.create_image(125,125,image=img)
canvas.grid(column=1,row=0)


lab1=Label(text="Website👉",font=("Courier",12,"italic"))
lab1.grid(row=1,column=0)
lab2=Label(text="Email/Username👉",font=("Courier",12,"italic"))
lab2.grid(row=2,column=0)
lab3=Label(text="Password👉",font=("Courier",12,"italic"))
lab3.grid(row=3,column=0)


inp1=Entry(width=35)
inp1.grid(row=1,column=1,columnspan=2)
inp1.focus()  #used to give cursor
inp2=Entry(width=35)
inp2.grid(row=2,column=1,columnspan=2)
inp2.insert(0,"@gmail.com")  #takes(position,string) to insert
inp3=Entry(width=35)
inp3.grid(row=3,column=1,columnspan=2)

but1=Button(text="Generate Password💡",width=15,command=genp)
but1.grid(row=3,column=2)
but2=Button(text="ADD👆",width=30,command=inputs)
but2.grid(row=4,column=1,columnspan=2)


window.mainloop()