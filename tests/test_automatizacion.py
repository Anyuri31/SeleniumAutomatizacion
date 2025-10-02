from selenium import webdriver #sirve para controlar el navegador
from selenium.webdriver.common.by import By     #sirve para localizar elementos en la página
# OBLIGATORIO para tu versión 4.35.0:
from selenium.webdriver.chrome.service import Service as ChromeService  #sirve para iniciar el servicio del driver
from webdriver_manager.chrome import ChromeDriverManager   #sirve para gestionar la instalación del driver
# IMPORTANTE: Instalar la librería webdriver-manager con pip install webdriver-manager
import time #sirve para hacer pausas



print("--- INICIANDO PRUEBA ---")

# 1. INICIALIZACIÓN: Arrancar el navegador
# La línea que usa webdriver-manager para encontrar el driver:
print("Paso 1: Configurando el Driver y abriendo Chrome...")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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