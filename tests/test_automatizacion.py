from selenium import webdriver #sirve para controlar el navegador
from selenium.webdriver.common.by import By  #sirve para localizar elementos en la página
from selenium.webdriver.chrome.service import Service as ChromeService #sierve para gestionar el servicio del driver de Chrome
from webdriver_manager.chrome import ChromeDriverManager #sirve para gestionar la instalación del driver de Chrome
import time  #sirve para hacer pausas en la ejecución
from selenium.webdriver.chrome.options import Options  #sirve para configurar opciones del navegador Chrome
#ultimo ajuste para ci
# 1. Crear el objeto de Opciones
chrome_options = Options()

# 2. Configurar el modo sin cabeza (headless): 
# Le dice a Chrome que se ejecute sin interfaz gráfica, necesario en CI.
chrome_options.add_argument("--headless")

# 3. Configurar la opción de seguridad:
# NECESARIO para que el driver funcione con versiones recientes de Chrome en CI.
chrome_options.add_argument("--remote-allow-origins=*") 


print("--- INICIANDO PRUEBA ---")
print("Paso 1: Configurando el Driver y abriendo Chrome...")
# 4. Pasar el objeto de opciones al inicializar el driver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options # <--- PARÁMETRO AÑADIDO
)

# 2. NAVEGACIÓN: Ir a la URL
driver.get("https://www.google.com")
print("Paso 2: Navegado a Google.")

# 3. LOCALIZACIÓN: Encontrar el campo de búsqueda (el elemento con name='q')
print("Paso 3: Localizando el campo de búsqueda...")
campo_busqueda = driver.find_element(By.NAME, "q") 

# 4. ACCIÓN: Escribir texto y enviar la búsqueda
campo_busqueda.send_keys("Aprendiendo Automatización Web")
campo_busqueda.submit()
print("Paso 4: Búsqueda realizada.")

# 5. PAUSA: Esperar 3 segundos para visualizar
time.sleep(3) 

# 6. CIERRE: Cerrar el navegador y terminar la sesión
driver.quit()
print("Paso 6: Automatización terminada. ¡Exitoso!")