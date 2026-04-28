import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
# 1. Cargar datos limpios
print("Cargando datos limpios...")
df = pd.read_csv("omega_limpio.csv")

print("Número de estrellas:", len(df))

# 2. Gráfico de movimiento propio
plt.figure()

plt.scatter(df["pmRA"], df["pmDE"], s=1)

plt.xlabel("pmRA (mas/año)")
plt.ylabel("pmDE (mas/año)")
plt.title("Distribución de movimiento propio - Omega Centauri")
plt.grid()
plt.show()




# Conectar a la base de datos
conn = sqlite3.connect("arqueologia.db")

# Cargar solo el cluster
df_cluster = pd.read_sql("SELECT * FROM cluster", conn)

conn.close()

# Graficar solo el cúmulo
plt.figure()

plt.scatter(df_cluster["pmRA"], df_cluster["pmDE"], s=1)

plt.xlabel("pmRA (mas/año)")
plt.ylabel("pmDE (mas/año)")
plt.title("Estrellas del cúmulo Omega Centauri (filtradas)")

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.grid()

plt.show()


# =========================
# GRÁFICA 2: Diagrama HR
# =========================

# Calcular índice de color
df_cluster["color"] = df_cluster["BPmag"] - df_cluster["RPmag"]

plt.figure()

plt.scatter(df_cluster["color"], df_cluster["Gmag"], s=1)

plt.xlabel("Color (BP - RP)")
plt.ylabel("Magnitud G")
plt.title("Diagrama HR - Omega Centauri (filtrado)")

# 🔴 Invertir eje Y (clave en astronomía)
plt.gca().invert_yaxis()

plt.grid()

# Guardar figura
plt.savefig("HR_cluster.png", dpi=300)

plt.show()
