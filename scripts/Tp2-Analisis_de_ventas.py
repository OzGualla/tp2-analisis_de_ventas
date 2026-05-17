
"""=== TP2 - Análisis de Ventas ===

- Autor: Gualla Mariano
- Rol actual: P-2 (Desarrollador)

"""

# ================================================================

import csv
import matplotlib
matplotlib.use('Agg')  # modo sin pantalla, guarda el archivo correctamente
import matplotlib.pyplot as plt


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

# ----------------------------------------------------------------
# BLOQUE 3: Identificación del día con mayor venta registrada
# El dataset no contiene columna de producto, por lo que el análisis
# se enfoca en la dimensión temporal como indicador de rendimiento.
# Se recorre el archivo comparando cada registro contra el máximo.
# ----------------------------------------------------------------
mejor_dia = None
mejor_venta = 0

with open(ruta, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        venta_dia = int(fila["ventas"])
        if venta_dia > mejor_venta:
            mejor_venta = venta_dia
            mejor_dia = fila["fecha_venta"]

print(f"- Día con mayor venta: {mejor_dia} (${mejor_venta:,})")
print("\n=== Análisis finalizado ===")

# ----------------------------------------------------------------
# BLOQUE 4: Generación del gráfico de evolución de ventas
# Se exporta como PNG en /resultados para garantizar persistencia
# del resultado más allá de la sesión de Google Colab.
# ----------------------------------------------------------------

ruta = "datos/ventas.csv"
fechas = []
ventas = []

with open(ruta, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fechas.append(fila["fecha_venta"])
        ventas.append(int(fila["ventas"]))

plt.figure(figsize=(14, 5))
plt.plot(fechas, ventas, color="steelblue", linewidth=1)
plt.title("Evolución de Ventas Diarias - Tienda de Luminaria 2024")
plt.xlabel("Fecha")
plt.ylabel("Ventas ($)")
plt.xticks(fechas[::30], rotation=45)
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado correctamente")