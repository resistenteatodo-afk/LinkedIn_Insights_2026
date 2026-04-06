import pandas as pd
import os

# ==========================================
# 1. CONFIGURACIÓN DE RUTAS INTELIGENTES
# ==========================================
# Detectamos la carpeta donde está este script (01_Python_ETL)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Subimos un nivel para llegar a la raíz (LinkedIn_Insights_2026)
BASE_DIR = os.path.dirname(SCRIPT_DIR)

# Definimos las rutas finales para los archivos
RAW_PATH = os.path.join(BASE_DIR, "02_Data", "Raw", "linkedin_raw_2026.csv")
PROCESSED_PATH = os.path.join(
    BASE_DIR, "02_Data", "Processed", "linkedin_clean_2026.csv"
)

# Creamos las carpetas automáticamente si no existen
os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)


# ==========================================
# 2. FUNCIÓN DE EXTRACCIÓN (RAW)
# ==========================================
def generar_datos_linkedin():
    print("🚀 1/3 - Iniciando extracción de datos globales...")

    # Datos con "ruido" para practicar tu limpieza pro
    data = {
        "Pais": [
            "EE.UU.",
            " india",
            "Brasil ",
            " china",
            "Reino Unido",
            "francia",
            "México",
            "indonesia",
            "Canadá",
            "España",
        ],
        "Usuarios_M": [220, 125, 75, 65, 42, 35, 32, 28, 25, 22],
        "Region": [
            "Norteamérica",
            "Asia",
            "Latam",
            "Asia",
            "Europa",
            "Europa",
            "Latam",
            "Asia",
            "Norteamérica",
            "Europa",
        ],
        "Crecimiento": [0.05, 0.18, 0.12, 0.02, 0.04, 0.06, 0.15, 0.22, 0.05, 0.07],
    }

    df = pd.DataFrame(data)
    # Guardamos el original sucio
    df.to_csv(RAW_PATH, index=False)
    print(f"✅ Archivo RAW guardado en: {RAW_PATH}")
    return df


# ==========================================
# 3. FUNCIÓN DE LIMPIEZA Y TRANSFORMACIÓN (ETL)
# ==========================================
def sistema_limpieza_pro(df):
    print("🧹 2/3 - Ejecutando sistema de limpieza personalizado...")

    # Limpieza: Quitar espacios y estandarizar a MAYÚSCULAS
    df["Pais"] = df["Pais"].str.strip().str.upper()

    # Transformación: Usuarios en valor real (unidad completa)
    df["Total_Usuarios"] = df["Usuarios_M"] * 1_000_000

    # Cálculo: Proyección de usuarios para final de 2026
    df["Proyeccion_Final_2026"] = (
        df["Total_Usuarios"] * (1 + df["Crecimiento"])
    ).astype(int)

    # Guardar el resultado final para Power BI
    df.to_csv(PROCESSED_PATH, index=False, encoding="utf-8-sig")
    print(f"✨ 3/3 - ¡Datos PROCESADOS con éxito en: {PROCESSED_PATH}")


# ==========================================
# 4. EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    print("-" * 50)
    try:
        df_sucio = generar_datos_linkedin()
        sistema_limpieza_pro(df_sucio)
        print("-" * 50)
        print("🔥 ¡MISIÓN CUMPLIDA! Los datos están listos para Power BI.")
        print(
            "💡 Próximo paso: Abre Power BI y carga el archivo 'linkedin_clean_2026.csv'."
        )
    except Exception as e:
        print(f"❌ Error durante el proceso: {e}")
