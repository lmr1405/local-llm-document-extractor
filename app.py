from file_manager import obtener_facturas, procesar_factura, exportar_csv

def main():
    """
    Función principal de la aplicación.

    Obtiene todas las facturas PDF de la carpeta 'data',
    procesa cada una mediante el LLM local y exporta
    los resultados a un archivo CSV.
    """

    # Busca todos los archivos PDF cuyo nombre contenga
    # la palabra "factura" dentro de la carpeta data.
    facturas = obtener_facturas("data")

    # Nombre del archivo donde se guardarán los resultados.
    destino = "resultados_facturas.csv"

    # Lista donde se almacenará el resultado obtenido
    # para cada una de las facturas procesadas.
    resultados = []

    # Recorre todas las facturas encontradas.
    for factura in facturas:

        # Procesar la factura:
        # 1. Extraer el texto del PDF.
        # 2. Enviar el texto al LLM mediante la API de Ollama.
        resultado = procesar_factura(factura)

        # Añadir la respuesta del modelo a la lista de resultados.
        resultados.append(resultado)

    # Cuando todas las facturas han sido procesadas,
    # exportar los resultados a un archivo CSV.
    exportar_csv(resultados, destino)

  

# Punto de entrada principal del programa.
if __name__ == "__main__":
    main()