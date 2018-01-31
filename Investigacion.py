# -*- coding: utf-8 -*-
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

print ("Ingresando al sistema")
time.sleep(3)
print ("Cargando...")

driver = webdriver.Firefox() #Abre el navegador Firefox
url = "https://app.unicah.edu/registro/servlet/loginstd" #Url de la pagina de inicio
driver.get(url) #Abre la Url

time.sleep(1)
print ("Cargando...")

print ("Ingresando datos de usuario")

username = driver.find_element_by_id("vUSRNOM") #Busca el campo de identificacion
password = driver.find_element_by_id("vUSRPWD") #Busca el campo de la contraseña

time.sleep(1)
print ("Cargando...")

username.send_keys("0502199900116") #Escribe la identificacion *Dentro de los corchetes pone tu id
password.send_keys("lesdyromero789") #Escribe la contraseña *Dentro de los corchetes pone tu pass

time.sleep(1)
print ("Cargando...")

print ("Buscando las notas")

login = driver.find_element_by_class_name("Button") #Busca el boton de ingreso
login.click() #Hace click en el boton de ingreso

time.sleep(5)

print ("Cargando...")

notes = driver.find_element_by_id("BTNBOLETANOTAS") #Busca la boleta de notas
notes.click() #Hace click sobre la boleta de notas

time.sleep(1)
print ("Cargando...")

soup = BeautifulSoup(driver.page_source, 'html.parser') #Se declara BeautifulSoup

table = soup.find_all('table') #Busca todos los elementos dentro de la tabla

time.sleep(1)

for tab in table[0]: #Hace un recorrido por todas las tablas existentes
    elem = tab.find_all('td') #Declaracion de "elem"

for x in elem: #Recorre las tablas
    x = x.get_text(" ") #busca la informacion
    print (x) #Imprime la informacion

time.sleep(1)

definicion = table[3].get_text("        ") #Busca la definicion de la tabla
print (definicion) #Imprime la definicion de la tabla

time.sleep(1)

for x in table[4]: #Notas
    for y in x:
        y = y.get_text(" ")
        print (y)

driver.close()