# 🚀 LinkedIn Insights 2026: Pipeline de Datos Completo

Este proyecto transforma datos brutos sobre la demografía global de LinkedIn en un dashboard estratégico interactivo. Cubre desde la limpieza de datos con **Python**, el almacenamiento en **MySQL** hasta la visualización avanzada en **Power BI**.

## 📊 Vista Previa del Proyecto

<video src="04_Assets_Style/linkedin.mp4" width="100%" controls></video>

🛠️ Tecnologías y Herramientas

- **Lenguaje:** Python 3.x
- **Librerías:** Pandas (ETL), MySQL-Connector.
- **Base de Datos:** MySQL Server.
- **Visualización:** Power BI Desktop.

## 🏗️ Estructura del Repositorio

El proyecto está organizado de manera profesional siguiendo estándares de ingeniería de datos:

- **`01_Python_ETL`**: Contiene los scripts automatizados para la limpieza (`main_cleaner.py`) y la carga a la base de datos (`cargar_datos.py`).
- **`02_Data`**: Almacena el dataset original (Raw) y el procesado (Processed) listo para análisis.
- **`03_PowerBI_Dashboard`**: Contiene el archivo `.pbix` con el reporte visual.
- **`04_Assets_Style`**: Recursos visuales y capturas del proyecto.

## ⚙️ Cómo ejecutar este proyecto

1. Instala las dependencias: `pip install pandas mysql-connector-python`.
2. Ejecuta `main_cleaner.py` para procesar los datos.
3. Configura tu instancia de MySQL y ejecuta `cargar_datos.py`.
4. Abre el archivo en `03_PowerBI_Dashboard` para ver los resultados.

---

**Autor:** Tomass - _Data Engineering Enthusiast_
