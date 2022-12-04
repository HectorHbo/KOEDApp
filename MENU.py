from tkinter import*
import tkinter as tk
from tkinter import filedialog
import os
import sys

#DIMENSIONES DEL MENU, (POR CAMBIAR)
raiz=Tk()
raiz.title("Aplicacion KOED")
raiz.resizable(False, False)
raiz.geometry("1299x705")
raiz.config(bg="white")

miframe=Frame()
miframe.pack()

#(IMAGEN DE FONDO EN EL MENU O CANVAS)
miImagen=PhotoImage(file=r"D:\Universidad\Segundo Semestre\Fundamentos de Programación\Laboratorio\Scripts\fondo.gif")
my_canvas = Canvas(raiz, width=1299, height=705)
my_canvas.pack(fil="both", expand=True)
my_canvas.create_image(0,0, image=miImagen, anchor="nw")

#APARTADO DE FUNCIONES Y DEFINICIONES

def onOpen():
    print(filedialog.askopenfilename(initialdir="/", title="open file", filetypes=(("Python files","*.py;*.pyw"),("All files","*.*"))))
#DA LA OPCION DE ABRIR ARCHIVOS .PY Y DE TODO TIPO

def onSave():
    print(filedialog.asksaveasfilename(initialdir="/", title="open file", filetypes=(("Python files","*.py;*.pyw"),("All files","*.*"))))
#DA LA OPCION DE ABRIR ARCHIVOS .PY Y DE TODO TIPO

def resetProgram():
    python= sys.executable
    os.execl(python, python, * sys.argv)
#FUNCION RESETEAR MENU

def OpenWord():
    os.startfile("Documento.docx")
#FUNCION ABRIR DOCUMENTO WORD

def OpenPdf():
    os.startfile("archivo.pdf")
#FUNCION ABRIR ARCHIVO PDF

#

#FUNCION ABRIR ENLACES EXTERNOS:
def OpenDiscord():
    os.startfile("https://discord.gg/GVZnPmE8vV")
#SERVIDOR DISCORD

def OpenDrive():
    os.startfile("https://drive.google.com/drive/folders/1J1ZL69j467ZDmcYZrXG0iLoU6Z1uwSpy?usp=share_link")
#MATERIAL DRIVE

def OpenRick():
    os.startfile("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
#HIMNO KOED

#AGREGAR MENU
barraMenu=Menu(raiz)

#AGREGAR OPCIONES DE MENU
mnuArchivo=Menu(barraMenu)
mnuTipoDocum=Menu(barraMenu)
mnuEnlaces=Menu(barraMenu)
mnuAyuda=Menu(barraMenu)

#VENTANA ARCHIVOS CON 4 FUNCIONES
mnuArchivo.add_command(label="Abrir", command=onOpen)
mnuArchivo.add_command(label="Guardar", command=onSave)
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Reset", command=resetProgram)
mnuArchivo.add_command(label="Salir", command=raiz.destroy)

#VENTANA DOCUMENTOS 2 FUNCIONES ABRIR ARCHIVOS
mnuTipoDocum.add_command(label="PDF", command=OpenPdf)
mnuTipoDocum.add_command(label="Word", command=OpenWord)

#VENTANA ENLACES EXTERNOS
mnuEnlaces.add_command(label="Drive", command=OpenDrive)
mnuEnlaces.add_command(label="Discord", command=OpenDiscord)
mnuEnlaces.add_command(label="RickRoll", command=OpenRick)

#VENTANA AYUDA (FALTA AGREGAR FUNCIONES)
#AYUDA=ABRIR PDF CON INFORMACION SOBRE EL MENU
#ABOUT= EXPLICAR EL PROPOSITO DE KOED
mnuAyuda.add_command(label="Ayuda")
mnuAyuda.add_separator()
mnuAyuda.add_command(label="About")

#AGREGAR MENU COMO CASCADA
barraMenu.add_cascade(label="Archivo", menu=mnuArchivo)
barraMenu.add_cascade(label="Documentacion", menu=mnuTipoDocum)
barraMenu.add_cascade(label="Enlace", menu=mnuEnlaces)
barraMenu.add_cascade(label="Ayuda", menu=mnuAyuda)

#AGREGAR MENU
raiz.config(menu=barraMenu)

#ABRIR MENU
raiz.mainloop()
