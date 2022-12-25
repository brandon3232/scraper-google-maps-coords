import openpyxl #libreria externa
#from tkinter import *
from tkinter import filedialog
import scraper

##########################################################
#seleccionar archivo a utilizar
##########################################################
filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Selecciona el archivo excel a usar",
                                          filetypes = (("Excel",
                                                        "*.xlsx*"),
                                                       ("all files",
                                                        "*.*")))

libro = openpyxl.load_workbook(filename)

pagina = libro.active

libro.close