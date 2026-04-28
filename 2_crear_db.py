import pandas as pd
import sqlite3

# 1. Cargar datos
print("Cargando datos...")
df = pd.read_csv("omega_bruto.csv")

print("Dimensiones iniciales:", df.shape)

# 2. Verificar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# 3. Limpiar datos (eliminar filas con NaN en columnas clave)
columnas_clave = ["pmRA", "pmDE", "Gmag", "BPmag", "RPmag"]

df_limpio = df.dropna(subset=columnas_clave)

print("\nDimensiones después de limpieza:", df_limpio.shape)

# 4. Guardar nuevo archivo limpio
df_limpio.to_csv("omega_limpio.csv", index=False)

print("\nArchivo limpio guardado como omega_limpio.csv")



# parte de slite
print("\nCreando base de datos SQLite...")

# 1. Crear conexión (esto crea el archivo .db)
conn = sqlite3.connect("arqueologia.db")

# 2. Transferir DataFrame a SQL
df_limpio.to_sql("estrellas", conn, if_exists="replace", index=False)

print("Tabla 'estrellas' creada en arqueologia.db")

# 3. Cerrar conexión
conn.close()

print("Conexión cerrada.")
