
"""=== TP2 - Análisis de Ventas ===

- Autor: Gualla Mariano
- Rol actual: P-3 (Revisor y QA)

- Revisión: Mejora de documentación interna y legibilidad del código """

# ================================================================

import csv

# ----------------------------------------------------------------
# CONFIGURACIÓN GENERAL
# Ruta relativa al dataset — garantiza reproducibilidad en Colab
# sin depender de rutas absolutas del sistema de archivos local
# ----------------------------------------------------------------
ruta = "datos/ventas.csv"

# ----------------------------------------------------------------
# Importación del dataset y verificación de estructura
# Se utiliza el módulo csv de la biblioteca estándar de Python
# para evitar dependencias externas y asegurar compatibilidad.
# ----------------------------------------------------------------

print("=== Verificación de estructura del dataset ===")

with open(ruta, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        print(fila)

# Acumulador inicializado en 0 antes del cálculo del siguiente bloque
ventas_totales = 0
