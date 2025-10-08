# test_nombre_de_la_prueba.py (Va DENTRO de la carpeta 'tests/')

import pytest
# Importa la clase de página que deseas probar
from pages.ejemplo_page import NombreDeLaPagina 

# === FUNCIÓN DE PRUEBA ===

# IMPORTANTE: Solicitas la fixture con su nombre ('driver_setup')
def test_mi_flujo_de_usuario_es_correcto(driver_setup): 
    """Función de prueba: Verifica la secuencia de acciones y resultados."""
    
    # --- 1. CONFIGURACIÓN (Creación del Objeto) ---
    # 'driver_setup' es el navegador abierto que Pytest inyecta.
    pagina = NombreDeLaPagina(driver_setup) # <--- AQUÍ VA: La creación del objeto (la INSTANCIA).
    
    # --- 2. ACCIONES (El Flujo de Usuario) ---
    pagina.cargar_pagina()
    
    # Lógica de la prueba (llamando a los métodos de la clase)
    pagina.ingresar_credenciales("usuario_valido", "contrasena_secreta") 

    # --- 3. VERIFICACIÓN (Aserción) ---
    # Obtener el resultado final de la acción
    titulo_actual = pagina.obtener_titulo() 
    
    # Verificar el resultado con una aserción
    assert "Bienvenido" in titulo_actual # <--- AQUÍ VA: El assert que dice si la prueba PASA o FALLA.
    # assert es la forma correcta y profesional de verificar, no time.sleep()