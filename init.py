

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Ruta al ejecutable de ChromeDriver
driver = webdriver.Chrome()

# Abre WhatsApp Web en el navegador Brave
driver.get('https://web.whatsapp.com')

# Espera a que el usuario escanee el código QR manualmente

# Encuentra el campo de búsqueda y escribe el nombre del contacto o grupo
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
search_box.send_keys('Sistemas 2023 Deltec')

# Espera un segundo para que aparezcan los resultados
driver.implicitly_wait(4)

# Abre la conversación
search_box.send_keys(Keys.RETURN)

# Espera un segundo para que la conversación se cargue completamente
driver.implicitly_wait(4)

contacto = driver.find_element(By.XPATH, '(//*[@role="listitem"])[1]')
contacto.click()
driver.implicitly_wait(3)
# Encuentra el cuadro de texto para el mensaje y escribe tu mensaje
message_box = wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@contenteditable="true"])[2]')))
message_box.send_keys('HOLA DESDE PYTHON LOKAS')

# Envía el mensaje
message_box.send_keys(Keys.RETURN)
send = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Send" or @aria-label="Enviar"]')))
driver.implicitly_wait(5)
send.click()
driver.implicitly_wait(5)
# Cierra el navegador cuando hayas terminado
driver.quit()
