# conftest.py (Va DENTRO de la carpeta 'tests/')
#Este archivo contiene todas las librerías necesarias para inicializar y gestionar el navegador. No tendrás que repetir estas importaciones en tus archivos de prueba.

import pytest
# Selenium WebDriver: La librería principal para controlar el navegador
from selenium import webdriver
# By: Necesario para definir los localizadores (By.ID, By.NAME, etc.)
from selenium.webdriver.common.by import By 
# ChromeService: Necesario para gestionar el servicio del driver de Chrome
from selenium.webdriver.chrome.service import Service as ChromeService 
# Options: Necesario para configurar el modo headless, seguridad, etc.
from selenium.webdriver.chrome.options import Options 
# WebDriverManager: Necesario para descargar y gestionar automáticamente el driver
from webdriver_manager.chrome import ChromeDriverManager 
# Time (Opcional): Lo dejo por si necesitas pausas manuales para debugging, aunque no es buena práctica.
import time 

# === DEFINICIÓN DE LA FIXTURE DEL DRIVER ===

@pytest.fixture(scope="module") 
def driver_setup():
    """Fixture: Configura, inicializa y cierra el driver de Chrome para las pruebas."""
    
    # --- Configuración del Driver ---
    chrome_options = Options()
    # 1. Modo Headless (Imprescindible en servidores CI)
    chrome_options.add_argument("--headless")
    # 2. Opción de Seguridad (Necesario para versiones recientes de Chrome)
    chrome_options.add_argument("--remote-allow-origins=*") 
    
    # --- Inicialización ---
    # 1. Instala el driver si es necesario y obtiene el servicio
    service = ChromeService(ChromeDriverManager().install())
    # 2. Inicia el navegador con el servicio y las opciones
    driver = webdriver.Chrome(service=service, options=chrome_options) 
    
    # Buena Práctica: Espera Implícita (para manejar cargas rápidas)
    driver.implicitly_wait(5) 
    
    # --- Devolución y Pausa ---
    yield driver  # Pytest devuelve el 'driver' abierto y pausa aquí
    
    # --- Limpieza (Se ejecuta automáticamente al finalizar la prueba) ---
    driver.quit() # Cierra el navegador y la sesión del driver