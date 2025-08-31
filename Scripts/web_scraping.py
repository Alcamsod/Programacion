from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# # Configuramos Selenium
# options = Options()
# options.add_argument("--headless")  
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")


# Alternativa

options = Options()
# options.add_argument("--headless")  # ❌ comentado para que se vea
options.add_argument("--start-maximized")  # abre ventana en grande


# Iniciamos el web driver
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Introducimos la url.
url = "https://naturmetica.com/tienda/?gad_source=1&gad_campaignid=22550522311&gbraid=0AAAAAoih_1sicPVCz99LlZDEoTqOuweR_&gclid=Cj0KCQjw5c_FBhDJARIsAIcmHK9uiumLugXG8wzOJSlc9Cip_3ADwtCFMk-CQ_YZFiFeK5QqW8pL2I8aAuu4EALw_wcB"
driver.get(url)

productos_data = []

# Obtenemos para todos los objetos visibles
productos = driver.find_elements(By.CSS_SELECTOR, "li.product")
while True:
    # Obtener todos los productos visibles
    productos = driver.find_elements(By.CSS_SELECTOR, "li.product")

    for producto in productos:
        try:
            # Nombre
            nombre = producto.find_element(By.CSS_SELECTOR, "h2.woocommerce-loop-product__title").text.strip()
        except:
            nombre = "N/A"

        try:
            # Precio
            precio = producto.find_element(By.CSS_SELECTOR, "span.woocommerce-Price-amount").text.strip()
        except:
            precio = "N/A"

        try:
            # Reseñas (rating + nº reseñas)
            reseña_div = producto.find_element(By.CSS_SELECTOR, "div.jdgm-prev-badge")
            estrellas = reseña_div.get_attribute("data-average-rating")
            num_reseñas = reseña_div.get_attribute("data-number-of-reviews")
        except:
            estrellas = "N/A"
            num_reseñas = "0"

        productos_data.append({
            "Nombre": nombre,
            "Precio": precio,
            "Estrellas": estrellas,
            "Nº Reseñas": num_reseñas
        })

    # Intentar pasar a la siguiente página
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "a.next.page-numbers")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)  # Esperar carga
    except:
        print("No hay más páginas.")
        break

# Guardamos en un CSV
df = pd.DataFrame(productos_data)
path = "./Scripts/informacion_productos.csv"
df.to_csv(path, index=False, encoding="utf-8-sig")

print(f"✅ Scraping completado. Datos guardados en '{path}'.")

driver.quit()
