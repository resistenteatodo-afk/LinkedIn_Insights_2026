import mysql.connector
import pandas as pd
import os

# 1. Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "02_Data", "Processed", "linkedin_clean_2026.csv")

try:
    # 2. Conectar a la base de datos que ya creamos
    print("🔗 Conectando a la base de datos...")
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="thedria31",  # Pon tu contraseña si tienes
        database="datos_linkedin",
    )
    cursor = conexion.cursor()

    # 3. Leer los datos del CSV (El que limpiamos con Python)
    print("📖 Leyendo datos del CSV...")
    df = pd.read_csv(CSV_PATH)

    # 4. Insertar fila por fila en MySQL
    print("🚀 Insertando datos en la tabla 'usuarios_globales'...")
    for index, row in df.iterrows():
        sql = "INSERT INTO usuarios_globales (pais, usuarios_m, region, total_usuarios) VALUES (%s, %s, %s, %s)"
        val = (row["Pais"], row["Usuarios_M"], row["Region"], row["Total_Usuarios"])
        cursor.execute(sql, val)

    conexion.commit()  # ¡Importante para guardar los cambios!
    print(f"✅ ¡Éxito! Se han insertado {cursor.rowcount} registros.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
except FileNotFoundError:
    print(f"❌ Error: No se encontró el archivo CSV en {CSV_PATH}")
finally:
    if "conexion" in locals() and conexion.is_connected():
        conexion.close()
