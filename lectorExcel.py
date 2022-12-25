#from tkinter import *
from tkinter import filedialog


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
    return filename

##########################################################
# main
##########################################################





