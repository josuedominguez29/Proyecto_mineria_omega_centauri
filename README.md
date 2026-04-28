# Proyecto 1: Arqueología Galáctica y Omega Centauri

## Descripción
Este proyecto tiene como objetivo analizar el movimiento de estrellas (cinemática) para distinguir cuáles pertenecen al cúmulo Omega Centauri y cuáles son estrellas de la Vía Láctea en primer plano.

## Parte 1: Obtención de coordenadas

Se consultó la base de datos astronómica SIMBAD para obtener las coordenadas precisas del objeto Omega Centauri (NGC 5139).

## Coordenadas (grados decimales)
- Ascensión Recta (RA): 201.697 
- Declinación (DEC): -47.479

## Herramientas utilizadas
- WSL (Linux)
- Python
- Git & GitHub
- SIMBAD
## Análisis de Resultados

### Gráfica 1: Movimiento Propio

Se construyó un diagrama de movimiento propio (pmRA vs pmDE) para todas las estrellas en la región de Omega Centauri. En esta gráfica se observa una distribución dispersa correspondiente a estrellas de la Vía Láctea, y un grupo compacto desplazado que representa las estrellas del cúmulo.

Mediante un filtro SQL en el espacio de movimiento propio, se logró aislar este grupo, identificando estrellas que comparten un movimiento coherente.

### Gráfica 2: Diagrama HR

Utilizando únicamente las estrellas filtradas cinemáticamente, se construyó el diagrama Color-Magnitud (BP - RP vs Gmag).

Este diagrama muestra una secuencia estelar bien definida, característica de un cúmulo globular.

A diferencia del conjunto completo de datos, donde el diagrama estaría contaminado por estrellas de la Vía Láctea, el filtrado mediante SQL permite obtener una población estelar más pura, evidenciando claramente la estructura evolutiva del cúmulo.

### Conclusión

El uso de criterios cinemáticos permite separar de manera efectiva las estrellas pertenecientes a Omega Centauri de aquellas que solo están en la línea de visión. Esto confirma que el cúmulo posee una identidad dinámica propia, consistente con su origen como posible núcleo remanente de una galaxia enana.
