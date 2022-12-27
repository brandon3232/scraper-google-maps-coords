import tkinter
from tkinter import ttk
from tkinter import filedialog

##########################################################
#seleccionar archivo a utilizar
##########################################################
def cargarArchivo(labelTextFile):
    filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Selecciona el archivo excel a usar",
                                            filetypes = (("Excel",
                                                            "*.xlsx*"),
                                                        ("all files",
                                                            "*.*")))
    labelTextFile['text'] = filename


##########################################################
#crear ventana
##########################################################
def crearVentana():

    #creacion de ventana
    ventana = tkinter.Tk()

    ventana.title("scraper google maps")
    ventana.geometry("600x550+350+150")
    ventana.resizable(width=False, height=False)

    #seleccion de archivo excel
    labelSelecFile = tkinter.Label(ventana, text = "selecciona un archivo de excel")
    labelSelecFile.pack(pady=5)

    buttonFile = tkinter.Button(ventana, text = "selecciona un archivo", command= cargarArchivo(labelTextFile))
    buttonFile.pack(pady=5)

    labelTextFile = tkinter.Label(ventana, text = "")
    labelTextFile.pack(pady=5)

    #indicar nombre de libro
    labelNameBook = tkinter.Label(ventana, text = "nombre de libro")
    labelNameBook.pack(pady=10)

    textNameBook = tkinter.Entry(ventana)
    textNameBook.pack(pady=5)

    #indicar fila de inicio
    labelInitRow = tkinter.Label(ventana, text = "fila de inicio")
    labelInitRow.pack(pady=10)

    textInitRow = tkinter.Entry(ventana)
    textInitRow.pack(pady=5)

    #indicar fila final
    labelEndRow = tkinter.Label(ventana, text = "ultima fila")
    labelEndRow.pack(pady=10)

    textEndRow = tkinter.Entry(ventana)
    textEndRow.pack(pady=5)

    #indicar columna inicio
    labelInitColum = tkinter.Label(ventana, text = "columna de inicio")
    labelInitColum.pack(pady=10)

    textInitColum = tkinter.Entry(ventana)
    textInitColum.pack(pady=5)

    #indicar fila final
    labelEndColum = tkinter.Label(ventana, text = "columna final")
    labelEndColum.pack(pady=10)

    textEndColum = tkinter.Entry(ventana)
    textEndColum.pack(pady=5)

    #indicar fila final
    labelColumWrite = tkinter.Label(ventana, text = "columna de escritura")
    labelColumWrite.pack(pady=10)

    textColumWrite = tkinter.Entry(ventana)
    textColumWrite.pack(pady=5)


    ventana.mainloop()

crearVentana()