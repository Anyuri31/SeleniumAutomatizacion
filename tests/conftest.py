#sirve para tener las configuraciones globales de pytest y no usarlas en cada test de prueba
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ... (Importaciones necesarias para el driver, como webdriver_manager) ...

# === A. DEFINICIÓN DE LA FIXTURE DEL DRIVER ===

@pytest.fixture(scope="module") # <--- @FIXTURE: Marca esta función como un recurso. 'module' significa ejecutar una vez por archivo.
def driver_setup():
    """Fixture: Prepara el driver de Chrome antes de la prueba y lo cierra después."""
    
    # --- Configuración (Tu código de opciones Headless) ---
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-allow-origins=*")
    
    # --- Inicialización ---
    # AQUÍ VA: Tu código para inicializar el driver (webdriver.Chrome(...))
    driver = webdriver.Chrome(options=chrome_options) 
    
    # Buena práctica: Sincronización implícita para cargas rápidas
    driver.implicitly_wait(5) 
    
    # --- Pausa / Devolución ---
    yield driver  # <--- YIELD: Pausa la función, envía el 'driver' abierto a la prueba.
    
    # --- Limpieza (Se ejecuta después de la prueba) ---
    driver.quit() # <--- AQUÍ VA: El cierre limpio del navegador.