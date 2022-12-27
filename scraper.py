import subprocess
import os
import wget #libreria externa
import requests #libreria externa
import zipfile
import time
import re
from selenium import webdriver #libreria externa
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import openpyxl #libreria externa
from lectorExcel import cargarArchivo


##########################################################
#verificar version de google chrome instalada
##########################################################
def verificaVersionChrome():
    version = subprocess.check_output(
        r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
        shell=True
    )
    version = version.decode('utf-8').strip()
    version =version[8:18] 

    return version


##########################################################
#verificar version de driver online
##########################################################

def verificarDriverOnline():
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version = response.text

    return version

##########################################################
#descargar drivers 
##########################################################
def descargaDriver(versionOnline,direccionDriver):
    

    remote_url = "https://chromedriver.storage.googleapis.com/" + versionOnline + "/" + "chromedriver_win32.zip"
    
    versionOnline = versionOnline.replace(".","_")
    local_file = direccionDriver + "chromedriver"

    archivo_en_zip = wget.download(remote_url, local_file)

    with zipfile.ZipFile(archivo_en_zip, 'r') as zip_ref:
        zip_ref.extractall(direccionDriver + "chromedriver_win32_" + versionOnline) 
   
    os.remove(archivo_en_zip)



##########################################################
# verificar drivers actualizados
##########################################################
def verificar_drivers_actualizados(chrome, online, direccionDriver):
    versionOnline = online.replace(".","_")

    if not(chrome == online[:10]):
        descargaDriver(online, direccionDriver)

    if not(os.path.exists(direccionDriver + "\\chromedriver_win32_" + versionOnline)):
        descargaDriver(online, direccionDriver)

    return versionOnline

##########################################################
# geocoder
##########################################################

def get_geocoder(url_location): # gets geographical lat/long coordinates
        try:
            coords = re.search(r"!3d-?\d\d?\.\d{4,8}!4d-?\d\d?\.\d{4,8}",
                            url_location).group()
            coord = coords.split('!3d')[1]

            tup = tuple(coord.split('!4d'))
            delim = ','

            return delim.join(tup)

        except (TypeError, AttributeError):
            return  "0,0"



##########################################################
# geocoder
##########################################################
def scrape(ubicacion, driver):
    try:
        WebDriverWait(driver, 15)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'input#searchboxinput')))\
                                                .clear()

        WebDriverWait(driver, 15)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'input#searchboxinput')))\
                                                .send_keys(f'{ubicacion}')

        WebDriverWait(driver, 15)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'button#searchbox-searchbutton')))\
                                                .click()

        time.sleep(3) #TODO: probar si es suficiente tiempo para que cargue url

        return get_geocoder(driver.current_url)

    except:
        WebDriverWait(driver, 15)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'button.YismEf')))\
                                                .click()

        return "0,0"




##########################################################
# main
##########################################################
def scrapear(dirArchivo,libro , filaInicio, filaFinal, colInic, colFin, colCoords):
    directorioActual = os.getcwdb()
    directorioActual = directorioActual.decode('utf-8').strip()
    direccionDriver = directorioActual+"\drivers\\"

    version = verificar_drivers_actualizados(verificaVersionChrome(),verificarDriverOnline(), direccionDriver)

    #leer archivo excel
    ##archivo = cargarArchivo()
    archivo = openpyxl.load_workbook(dirArchivo)
    pagina = archivo[f'{libro}']
    archivo.close

    # Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    #cargando driver
    driver = webdriver.Chrome(
        service=Service(executable_path=direccionDriver+"chromedriver_win32_" + version + ".exe"), 
        options = options)


    #inicializar navegador
    driver.get("https://www.google.com/maps")

    coordenadas = []

    ##filaInicio = 1487
    ##filaFinal = 1616
    ##colInic = 'F'
    ##colFin = 'G'
    ##colCoords = 'H'

    for i in range(filaInicio,filaFinal):
        lugar,ubicacion = pagina[f'{colInic}{i}:{colFin}{i}'][0]
        pagina[f'{colCoords}{i}'] = scrape(lugar.value + ", " + ubicacion.value + " izucar de matamoros, puebla",
                                            driver)
        #time.sleep(1)

    archivo.save(dirArchivo)

    time.sleep(1)
    driver.quit()


