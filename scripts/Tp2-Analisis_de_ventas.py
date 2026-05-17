
"""=== TP2 - Análisis de Ventas ===

- Autor: Gualla Mariano
- Rol actual: P-2 (Desarrollador)

"""

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

# ----------------------------------------------------------------
# BLOQUE 2: Cálculo de ventas totales del período
# csv.DictReader devuelve strings, por eso se convierte a int.
# Se abre el archivo en un nuevo contexto para reiniciar el cursor.
# ----------------------------------------------------------------
print("\\n=== Indicadores del período ===")
with open(ruta, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        ventas_totales += int(fila["ventas"])

print(f"- Ventas totales del período: ${ventas_totales:,}")
