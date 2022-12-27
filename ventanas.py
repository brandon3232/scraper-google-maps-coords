import tkinter
from tkinter import filedialog
from tkinter import ttk
from scraper import scrapear

##########################################################
#seleccionar archivo a utilizar
##########################################################
def cargarArchivo():
    filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Selecciona el archivo excel a usar",
                                            filetypes = (("Excel",
                                                            "*.xlsx*"),
                                                        ("all files",
                                                            "*.*")))
    labelTextFile['text'] = filename
    

##########################################################
#escrapear
##########################################################
def llamarScraper():
    archivo = labelTextFile["text"]
    filaInicio = int(textInitRow.get())
    filaFinal = int(textEndRow.get())
    colInic = textInitColum.get()
    colFin = textEndColum.get()
    colCoords = textColumWrite.get()
    libro = textNameBook.get()

    scrapear(archivo,libro , filaInicio, filaFinal, colInic, colFin, colCoords)

##########################################################
#crear ventana
##########################################################

filaInicio = 0
filaFinal = 1
colInic = ''
colFin = ''
colCoords = ''
libro=""

#creacion de ventana
root = tkinter.Tk()
root.title("scraper google maps")
root.geometry("+350+150")#600x550
root.resizable(width=False, height=False)

ventana = ttk.Frame(root)
ventana.grid(column=0, row=0)

#seleccion de archivo excel
labelSelecFile = ttk.Label(ventana, text = "selecciona un archivo de excel")
buttonFile = ttk.Button(ventana, text = "selecciona un archivo", command= cargarArchivo)
labelTextFile = ttk.Label(ventana, text = "")

#indicar nombre de libro
labelNameBook = ttk.Label(ventana, text = "nombre de libro")
textNameBook = ttk.Entry(ventana)

#indicar fila de inicio
labelInitRow = ttk.Label(ventana, text = "fila de inicio")
textInitRow = ttk.Entry(ventana)

#indicar fila final
labelEndRow = ttk.Label(ventana, text = "ultima fila")
textEndRow = ttk.Entry(ventana)

#indicar columna inicio
labelInitColum = ttk.Label(ventana, text = "columna de inicio")
textInitColum = ttk.Entry(ventana)

#indicar fila final
labelEndColum = ttk.Label(ventana, text = "columna final")
textEndColum = ttk.Entry(ventana)

#indicar fila final
labelColumWrite = ttk.Label(ventana, text = "columna de escritura")
textColumWrite = ttk.Entry(ventana)

buttonScrapear = ttk.Button(ventana, text = "scrapear", command=llamarScraper)



labelSelecFile.grid(column=1,row=0)
buttonFile.grid(column=1,row=1)
labelTextFile.grid(column=1,row=2)
labelNameBook.grid(column=0,row=3)
textNameBook.grid(column=0,row=4)
labelInitRow.grid(column=1,row=3)
textInitRow.grid(column=1,row=4)
labelEndRow.grid(column=2,row=3)
textEndRow.grid(column=2,row=4)
labelInitColum.grid(column=0,row=5)
textInitColum.grid(column=0,row=6)
labelEndColum.grid(column=1,row=5)
textEndColum.grid(column=1,row=6)
labelColumWrite.grid(column=2,row=5)
textColumWrite.grid(column=2,row=6)
buttonScrapear.grid(column=1,row=7)





#colInic = f'{textInitColum.get()}'
#colFin = f'{textEndColum.get()}'
#colCoords = f'{textColumWrite.get()}'
#archivo = f'{labelTextFile.get()}'
#libro = f'{textNameBook.get()}'

ventana.mainloop()

