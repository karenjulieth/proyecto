from tkinter import *
import time
import random
#crea la ventana inicial del juego
ventana=Tk()
imagen=PhotoImage(file="Fondo.png")
carro1=PhotoImage(file="CarroR.png")
carro2=PhotoImage(file="CarroR2.png")
enemigo1=PhotoImage(file="enemigo1.png")
enemigo2=PhotoImage(file="enemigo2.png")
enemigo3=PhotoImage(file="CarroR.png")
vidas=PhotoImage(file="vidas.png")
mancha1=PhotoImage(file="mancha.png")
can= Canvas(ventana,width=1033,height=662)
fondo=can.create_image(0,0,image=imagen,anchor=NW)
fondo2=can.create_image(0,-662,image=imagen,anchor=NW)

posxv=900#imagen vidas
posyv=100
posxc=390  #Posicion en la que la que estará el carro inicialmente
posyc=575
posxc2=735  #Posicion en la que la que estará el carro 2 inicialmente
posyc2=575

v=can.create_image(posxv,posyv,image=vidas,anchor=NW)
carros=can.create_image(posxc,posyc,image=carro1,anchor=NW)
vida1=3
carros2=can.create_image(posxc2,posyc2,image=carro2,anchor=NW)
vida2=3
contador=700

##parametros de nivel
arc=open("partida.txt","r")
nombre1=arc.readline()
nombre2=arc.readline()
tiempA=int(arc.readline())
movE=int(arc.readline())
arc.close()
##enemigos
carron2=[0,False]
carron=[0,False]
carron1=[0,False]
mancha=[0,False]

can.pack()

#teclas 
estado=3
s=True
s2=True
#guardar partida
def abrir():
    arc=open("guardar.txt","w")
    arc.write(str(vida1)+"\n")
    arc.write(str(vida2)+"\n")
    arc.write(str(posxc)+"\n")
    arc.write(str(posyc)+"\n")
    arc.write(str(posxc2)+"\n")
    arc.write(str(posyc2)+"\n")
    arc.close()
def guardar():
    vida1=arc.readline ()
    vida2=arc.readline ()
    posxc=arc.readline ()
    posyc=arc.readline ()
    posxc2=arc.readline ()
    posyc2=arc.readline ()
    arc.close()
    
 
    

    
def golpe():
    global posxc,posyc,carros,estado,s,posxc2,posyc2,carros2,s2,vida1,vida2
    if(mancha[1]==True):
        ob1=can.coords(mancha[0])
        if(vida1>0):
            ob2=can.coords(carros)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida1-=1
                can.delete(mancha[0])
                mancha[1]=False
        if(vida2>0):
            ob2=can.coords(carros2)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida2-=1
                can.delete(mancha[0])
                mancha[1]=False
    if(carron[1]==True):
        ob1=can.coords(carron[0])
        if(vida1>0):
            ob2=can.coords(carros)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida1-=1
                can.delete(carron[0])
                carron[1]=False
        if(vida2>0):
            ob2=can.coords(carros2)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida2-=1
                can.delete(carron[0])
                carron[1]=False # termina la funcion con el enemigo #1
    if(carron1[1]==True):
        ob1=can.coords(carron1[0])
        if(vida1>0):
            ob2=can.coords(carros)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida1-=1
                can.delete(carron1[0])
                carron1[1]=False
        if(vida2>0):
            ob2=can.coords(carros2)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida2-=1
                can.delete(carron1[0])
                carron1[1]=False #termina enemigo#2
    if(carron2[1]==True):
        ob1=can.coords(carron2[0])
        if(vida1>0):
            ob2=can.coords(carros)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida1-=1
                can.delete(carron2[0])
                carron2[1]=False
        if(vida2>0):
            ob2=can.coords(carros2)
            if(max(ob1[0],ob2[0])-min(ob1[0],ob2[0])<=45 and max(ob1[1],ob2[1])-min(ob1[1],ob2[1])<=45 ):
                vida2-=1
                can.delete(carron2[0])
                carron2[1]=False            
                

        
    if(vida1==0):
        can.delete(carros)
    if(vida2==0):
        can.delete(carros2)
        
    
def aparecemancha():
    global mancha
    x=random.randint(0,2)
    if(mancha[1]==False):
        if(x==0):
            mancha[0]=can.create_image(320,-40,image=mancha1,anchor=NW)
        elif(x==1):
            mancha[0]=can.create_image(430,-40,image=mancha1,anchor=NW)
        elif(x==2):
            mancha[0]=can.create_image(645,-40,image=mancha1,anchor=NW)
        else:
            mancha[0]=can.create_image(750,-40,image=mancha1,anchor=NW)
        mancha[1]=True
    can.after(tiempA,aparecemancha)
    
def apareceCarroE():#funcion para aparecer enemigos(carros y manchas)
    global carron, carron1,carron2,enemigo2,enemigo1,enemigo3
    x=random.randint(0,8)
    if(carron[1]==False):
        if(x==0):
            carron[0]=can.create_image(320,820,image=enemigo1,anchor=NW)
        elif(x==1):
            carron[0]=can.create_image(430,820,image=enemigo1,anchor=NW)
        elif(x==2):
            carron[0]=can.create_image(645,820,image=enemigo1,anchor=NW)
        else:
            carron[0]=can.create_image(750,820,image=enemigo1,anchor=NW)
        carron[1]=True #termina carron
    if(carron1[1]==False):#inicia enemigo#1
        if(x==3):
            carron1[0]=can.create_image(320,820,image=enemigo2,anchor=NW)
        elif(x==4):
            carron1[0]=can.create_image(430,820,image=enemigo2,anchor=NW)
        elif(x==5):
            carron1[0]=can.create_image(645,820,image=enemigo2,anchor=NW)
        else:
            carron1[0]=can.create_image(750,820,image=enemigo2,anchor=NW)
        carron1[1]=True #temina carron1   
    if(carron2[1]==False):#inicia carro2
        if(x==6):
            carron2[0]=can.create_image(320,820,image=enemigo3,anchor=NW)
        elif(x==7):
            carron2[0]=can.create_image(430,820,image=enemigo3,anchor=NW)
        elif(x==8):
            carron2[0]=can.create_image(645,820,image=enemigo3,anchor=NW)
        else:
            carron2[0]=can.create_image(750,820,image=enemigo3,anchor=NW)
        carron2[1]=True #temina carron1   
            
    can.after(tiempA,apareceCarroE)
    
def movimiento():
    global posxc,posyc,carros,estado,s,posxc2,posyc2,carros2,s2
    if(vida1>0):
        if("'a'" in K and posxc > 270):# corre el carro para la izquierda
           if(s == True):
                posxc-=8
                can.delete(carros)# elimina la imagen de la posición inicial del carro
                carros=can.create_image(posxc,posyc,image=carro1,anchor=NW)
                #estado=2
                #s=False
           elif(s==False):
                posxc=-8
                can.move(carros,-8,0)
        if("'d'" in K and posxc < 445):#corre el carro hacia la derecha
           if(s == True):
                posxc+=8
                can.delete(carros)
                carros=can.create_image(posxc,posyc,image=carro1,anchor=NW)
                #estado=1
                #s=True
           elif(s==False):
                posxc+=8
                can.move(carros,8,0)
        if("'w'" in K and posyc >100):# corre el carro para delante
            posyc-=3
            can.move(carros,0,-3)
        if("'s'" in K and posyc < 575):# corre el carro para atras
            posyc+=2
            can.move(carros,0,2)
    ## Player 2
    if(vida2>0):
        if("'4'" in K and posxc2 > 605):# corre el carro para la izquierda
           if(s2 == True):
                posxc2-=8
                can.delete(carros2)# elimina la imagen de la posición inicial del carro
                carros2=can.create_image(posxc2,posyc2,image=carro2,anchor=NW)
                #estado=2
                #s=False
           elif(s2==False):
                posxc2=-8
                can.move(carros2,-8,0)
        if("'6'" in K and posxc2 < 775):#corre el carro hacia la derecha
           if(s2 == True):
                posxc2+=8
                can.delete(carros2)
                carros2=can.create_image(posxc2,posyc2,image=carro2,anchor=NW)
                #estado=1
                #s=True
           elif(s2==False):
                posxc2+=8
                can.move(carros2,8,0)
        if("'8'" in K and posyc2 >100):# corre el carro para delante
            posyc2-=3
            can.move(carros2,0,-3)
        if("'5'" in K and posyc2 < 575):# corre el carro para delante
            posyc2+=2
            can.move(carros2,0,2)
    golpe()
        
    can.after(60,movimiento)
            
def movimientomapa():#mueve el mapa 
    global fondo,fondo2,carros,mancha,carros2,posxc,posyc,posxc2,posyc2,contador
    contador-=1
    cot1=Label(can,text=contador-1).place(x=1000,y=50)
    cot2=Label(can,text=contador-1).place(x=100,y=50)

    #print (contador)
    can.move(fondo,0,20)
    can.move(fondo2,0,20)
    if(can.coords(fondo)[1]>=660 or can.coords(fondo2)[1]>=660):
        can.delete(fondo)
        can.delete(fondo2)
        fondo=can.create_image(0,-662,image=imagen,anchor=NW)
        fondo2=can.create_image(0,0,image=imagen,anchor=NW)
        if(vida1>0):
            posxc=can.coords(carros)[0]
            posyc=can.coords(carros)[1]
            can.delete(carros)
            carros=can.create_image(posxc,posyc,image=carro1,anchor=NW)
        if(vida2>0):
            posxc2=can.coords(carros2)[0]
            posyc2=can.coords(carros2)[1]
            can.delete(carros2)
            carros2=can.create_image(posxc2,posyc2,image=carro2,anchor=NW)
         
        if(mancha[1]==True):
            tmp=can.coords(mancha[0])
            can.delete(mancha[0])
            mancha[0]=can.create_image(tmp[0],tmp[1],image=mancha1,anchor=NW)
    if(mancha[1]==True):
        can.move(mancha[0],0,10)
        if(can.coords(mancha[0])[1]>670):
            can.delete(mancha[0])
            mancha[1]=False
    can.after(50,movimientomapa)
    
def enemigos():#funcion para el movimiento de los carros enemigos
    global enemigo1,can,ventana,enemigo2
    if(carron[1]==True):
        tmp=can.coords(carron[0])
        can.delete(carron[0])
        carron[0]=can.create_image(tmp[0],tmp[1]-movE,image=enemigo1,anchor=NW)
        if(can.coords(carron[0])[1]<-100):
            can.delete(carron[0])
            carron[1]=False
    if(carron1[1]==True):
        tmp=can.coords(carron1[0])
        can.delete(carron1[0])
        carron1[0]=can.create_image(tmp[0],tmp[1]-movE,image=enemigo2,anchor=NW)
        if(can.coords(carron1[0])[1]<-100):
            can.delete(carron1[0])
            carron1[1]=False
    if(carron2[1]==True):
        tmp=can.coords(carron2[0])
        can.delete(carron2[0])
        carron2[0]=can.create_image(tmp[0],tmp[1]-movE,image=enemigo2,anchor=NW)
        if(can.coords(carron2[0])[1]<-100):
            can.delete(carron1[0])
            carron2[1]=False              
    can.after(60,enemigos)

def key(event):
    """
    objetivo: agrega a una lista de teclas presionadas la tecla que se undio con el fin que la funcion de movimiento se realize
    """
    global K,O
    tecla = repr(event.char)
    if(not(tecla in K)and tecla in O):
        K.append(tecla)
def key2(event):
    """
    objetivo: remueve de una lista de teclas presionadas la tecla que se solto con el fin que la funcion de movimiento pare de realizarce
    """
    global K,O
    tecla = repr(event.char)
    if((tecla in K)and tecla in O):
        K.remove(tecla)

##Teclas presionadas y permitidas
K=[]
O=["'d'","'a'","'w'","'s'","'6'","'8'","'4'","'5'"]

can.focus_set()
#etiquetas para que nombre aparezca
nom1=Label(can,text=nombre1).place(x=20,y=20)
nom2=Label(can,text=nombre2).place(x=1000,y=20)
#cot=Label(can,text=contador-1).place(x=1000,y=50)

aparecemancha()
apareceCarroE()
can.bind("<Key>",key)
can.bind("<KeyRelease>",key2)
movimientomapa()
movimiento()

enemigos()
    
mainloop()
