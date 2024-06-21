# -*- coding: utf-8 -*-
"""
Tema: Diccionarios y Entorno Gráfico con Tkinter

Referencia: Charatan, Programming in Two Semesters
            pag 220    
            https://python-forum.io/thread-30362.html   
            
@author: Roberto Méndez Méndez
modificado: Wed Jun 21 2024
"""

from tkinter import Tk, Label, Entry


# Diccionario
calificaciones = {'Saul' : 8.3 , 'Greta' : 9.5 , 
                  'Alex' : 7.8, 'Oscar' : 6.9, 'José' : 9.2}


# Creo la ventana
ventana = Tk()
ventana.title("Calificación")
ventana.eval('tk::PlaceWindow . center')

#Creo los elementos a poner en la ventana 
texto = Label(ventana,  font=('Helvetica 15 bold'), text = '¿Cuál es tu nombre?')
entrada = Entry(ventana, font=('Helvetica 15 bold'),background='#ffa533', width=30)
score = Label(ventana,font=('Helvetica 15 bold'),text='')


# Pongo los elementos en la ventana
texto.pack(side = 'left', padx=(20,5), pady=10)
entrada.pack(side='left', padx=(2,20), pady=10)
score.pack(side='bottom', padx= (0,10),pady=(100,5))

# Toma el dato de la entrada después de dar enter
# e imprime el nombre en consola
def mi_entrada(event):
    nombre = entrada.get()
    resultado = calificaciones[nombre]
    score.configure(text = 'Tu calificación es: '+ str(resultado))

# Enlaza el recuadro de entrada con dar Return    
entrada.bind('<Return>', mi_entrada)

ventana.mainloop()