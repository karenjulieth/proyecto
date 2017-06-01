from tkinter import *
#MENÚ
ventana1=Tk()
ventana1.title("Road_figther")
imagenm=PhotoImage(file="menu2.png")
imagen=PhotoImage(file="Fondo.png")

can = Canvas(ventana1,width=700,height=662)
menú=can.create_image(0,0,image=imagenm,anchor=NW)
#ventana de juego
def v():
    global campo1,campo2
    arc=open("partida.txt","w")
    arc.write(campo1.get()+"\n")
    arc.write(campo2.get()+"\n")
    arc.write(str(5000)+"\n")
    arc.write(str(15)+"\n")
    arc.close()
    ventana1.destroy()
    import nivel1
def v1():
    global campo1,campo2
    arc=open("partida.txt","w")
    arc.write(campo1.get()+"\n")
    arc.write(campo2.get()+"\n")
    arc.write(str(5000)+"\n")
    arc.write(str(30)+"\n")
    arc.close()
    ventana1.destroy()
    import nivel1
def v2():
    global campo1,campo2
    arc=open("partida.txt","w")
    arc.write(campo1.get()+"\n")
    arc.write(campo2.get()+"\n")
    arc.write(str(5000)+"\n")
    arc.write(str(10)+"\n")
    arc.close()
    ventana1.destroy()
    import nivel1
def v3():
    global campo1,campo2
    arc=open("partida.txt","w")
    arc.write(campo1.get()+"\n")
    arc.write(campo2.get()+"\n")
    arc.write(str(5000)+"\n")
    arc.write(str(5)+"\n")
    arc.close()
    ventana1.destroy()
    import nivel1
def v4():
    global campo1,campo2
    arc=open("partida.txt","w")
    arc.write(campo1.get()+"\n")
    arc.write(campo2.get()+"\n")
    arc.write(str(5000)+"\n")
    arc.write(str(6)+"\n")
    arc.close()
    ventana1.destroy()
    import nivel1    
        
    
#BOTONES
s=StringVar()
d=StringVar()     
boton1=Button(ventana1,text="Nivel 1",command=v,font=("verdana",15),background="blue").place(x=100,y=300)
boton2=Button(ventana1,text="Nivel 2",command=v1,font=("verdana",15),background="blue").place(x=100,y=360)
boton3=Button(ventana1,text="Nivel 3",command=v2,font=("verdana",15),background="blue").place(x=100,y=410)
boton4=Button(ventana1,text="Nivel 4",command=v3,font=("verdana",15),background="blue").place(x=100,y=460)
boton5=Button(ventana1,text="Nivel 5",command=v4,font=("verdana",15),background="blue").place(x=100,y=510)
cargar=Button(ventana1,text="cargar",font=("verdana",15),background="blue").place(x=100,y=660)

jugador1=Label(text="Jugador 1:",font=("verdana",19),background="green").place(x=100,y=200)
jugador1=Label(text="Jugador 2:",font=("verdana",19),background="green").place(x=100,y=250)
campo1=Entry(ventana1,textvariable=s,font=("verdana",19))
campo1.place(x=250,y=200)
campo2=Entry(ventana1,textvariable=d,font=("verdana",19))
campo2.place(x=250,y=250)

can.pack()


