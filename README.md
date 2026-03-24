# Prueba de Diagnóstico: Miner de Código en Tiempo Real

Este proyecto implementa un sistema de minería de código que analiza repositorios de GitHub para extraer palabras clave de nombres de funciones en lenguajes Python y Java, generando visualizaciones en tiempo real.

## Componentes

- **miner1.py**: Script en Python que utiliza PyDriller para analzar repositorios, extraer nombres de funciones y contar frecuencias de palabras.
- **visualizador.html**: Interfaz web con Chart.js que muestra gráficos de barras en tiempo real leyendo un archivo JSON generado por el miner.

## Requisitos

Python 3.x instalado.
Bibliotecas: PyDriller (`pip install pydriller`).
Navegador web

## Instrucciones de Ejecución

1. Instala dependencias:
   ```
   pip install pydriller
   ```

2. Ejecuta el miner:
   ```
   python miner1.py
   ```
   Esto generará `progreso_miner.json` en el directorio actual.

3. Abre `visualizador.html` en un navegador web (doble clic o servidor local abriendo un cmd en la carpeta en donde estan contenidos los archivos con `python -m http.server 8000`).

4. El visualizador se actualiza automáticamente cada 2 segundos leyendo el JSON.

## Documentación de Implementación

### Decisiones de Diseño

- **Minería limitada a HEAD**: Se analiza solo el último commit de cada repositorio para eficiencia y simplicidad, evitando procesamiento histórico completo.
- **Lenguajes soportados**: Solo Python (.py) y Java (.java) debido a la regex utilizada para extraer nombres de funciones.
- **Visualización**: Gráficos en tiempo real con Chart.js, leyendo JSON local.
