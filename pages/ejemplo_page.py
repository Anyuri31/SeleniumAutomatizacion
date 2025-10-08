from selenium.webdriver.common.by import By

class NombreDeLaPagina:
    """Clase: La plantilla para mapear una página específica (ej: LoginPage, HomePage)."""
    
    # === A. LOCALIZADORES (Las coordenadas de los elementos) ===
    
    # Buena práctica: Usar variables de clase para las URLs
    URL = "https://www.ejemplo.com/pagina"
    
    # Localizadores: Siempre en tuplas (By.TIPO, "VALOR")
    CAMPO_USUARIO = (By.ID, "user-input")
    BOTON_LOGIN = (By.CSS_SELECTOR, "button.submit")
    
    # === B. CONSTRUCTOR (Donde se recibe el navegador) ===
    
    def __init__(self, driver):
        """Constructor: Se ejecuta al crear el objeto."""
        # TÉCNICO: Recibe el driver abierto y lo guarda en la instancia (self)
        self.driver = driver # <--- ESTO ES VITAL: Le da el control del navegador al objeto.

    # === C. MÉTODOS DE ACCIÓN (Las acciones del usuario) ===
    
    def cargar_pagina(self):
        """Método: Navega a la URL base de la página."""
        self.driver.get(self.URL)

    def ingresar_credenciales(self, usuario, contrasena):
        """Método: Escribe en los campos de usuario y contraseña."""
        
        # 1. Encontrar y usar el localizador guardado
        self.driver.find_element(*self.CAMPO_USUARIO).send_keys(usuario)
        
        # Aquí iría el código para el campo de contraseña
        # self.driver.find_element(*self.CAMPO_CONTRASENA).send_keys(contrasena)
        
        # 2. Llamar al siguiente método de acción
        self.hacer_clic_en_login() # <--- Buena práctica: enlazar métodos internos
        
    def hacer_clic_en_login(self):
        """Método: Simplemente hace clic en el botón de login."""
        self.driver.find_element(*self.BOTON_LOGIN).click()
        
    # === D. MÉTODOS DE OBTENCIÓN DE DATOS (Para Asersiones) ===
    
    def obtener_titulo(self):
        """Método: Devuelve el título para que la prueba lo verifique."""
        return self.driver.title