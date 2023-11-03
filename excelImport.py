
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Captura de mensaje y selección de archivo Excel")
ventana.geometry("300x200")

# Crear una etiqueta para el mensaje
etiqueta = tk.Label(ventana, text="Escribe tu mensaje:")
entrada = tk.Entry(ventana, width=40, height=8)

etiqueta.pack(pady=10)

# Crear un campo de entrada para el mensaje
entrada_mensaje = tk.Entry(ventana)
entrada_mensaje.pack()

# Cambiar el estilo de la entrada de texto
style = ttk.Style()
style.configure('TButton', font=('calibri', 12, 'bold'))  # Cambia la fuente del texto del botón



def abrir_archivo_excel(mensaje):
    archivo_excel = filedialog.askopenfilename(filetypes=[("Archivos de Excel", "*.xlsx")])
    if archivo_excel:
        ventana.destroy()
        driver.get('https://web.whatsapp.com')
        df = pd.read_excel(archivo_excel)
        try:
            for index, row in df.iterrows():
                # import pdb; pdb.set_trace()
                mensaje_persona = mensaje.replace("{nombre}", str(row['NOMBRE']))
                mensaje_persona = mensaje_persona.replace("{telefono}", str(row['TELEFONO']))
                print(str(row['TELEFONO']))
                enviar_mensaje(mensaje_persona,str(row['TELEFONO']))
        except Exception as e:
            print("error {e}")
    # driver.quit()

def obtener_mensaje():
    mensaje = entrada_mensaje.get()
    abrir_archivo_excel(mensaje)

def enviar_mensaje(mensaje,numero):
    wait = WebDriverWait(driver, 30)
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
    search_box.clear()
    search_box.send_keys(numero)
    driver.implicitly_wait(5)
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    contacto = driver.find_element(By.XPATH, '(//*[@role="listitem"])[1]')
    contacto.click()
    driver.implicitly_wait(5)
    message_box = wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@contenteditable="true"])[2]')))
    wait = WebDriverWait(driver, 10)
    message_box.send_keys(mensaje)
    message_box.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 5)
    # send = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Send" or @aria-label="Enviar"]')))
    # driver.implicitly_wait(5)
    # send.click()
    # driver.quit()


# Crear un botón para continuar
boton_continuar = ttk.Button(ventana, text="Continuar", command=obtener_mensaje)
boton_continuar.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()