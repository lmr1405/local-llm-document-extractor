import os
import csv

from pdf_reader import extraer_texto_del_pdf
from llm_client import consultar_llm

def obtener_facturas(directorio):
    """
    Busca dentro de un directorio todos los archivos PDF cuyo nombre
    contenga la palabra 'factura'.

    Args:
        directorio (str): Ruta de la carpeta donde se encuentran los documentos.

    Returns:
        list: Lista con las rutas completas de los archivos PDF encontrados.
    """

    # Lista donde se almacenarán las rutas de las facturas encontradas.
    archivos_factura = []

    # Recorrer todos los archivos contenidos en el directorio indicado.
    for archivo in os.listdir(directorio):

        # Comprobar dos condiciones:
        # 1. Que el nombre del archivo contenga la palabra "factura".
        # 2. Que el archivo tenga extensión .pdf.
        #
        # lower() convierte el texto a minúsculas para evitar problemas
        # con nombres como "Factura1.PDF" o "FACTURA2.pdf".
        if "factura" in archivo.lower() and archivo.lower().endswith(".pdf"):

            # Crear la ruta completa combinando la carpeta y el nombre del archivo.
            ruta_completa = os.path.join(directorio, archivo)
            
            # Añadir la ruta del PDF a la lista de facturas.
            archivos_factura.append(ruta_completa)

    # Devolver todas las rutas encontradas.
    return archivos_factura



def procesar_factura(ruta_pdf):
    """
    Procesa una factura PDF utilizando el LLM local.

    Primero extrae el texto del documento y posteriormente lo envía
    al modelo mediante la API de Ollama.

    Args:
        ruta_pdf (str): Ruta del archivo PDF que se quiere procesar.

    Returns:
        str: Datos extraídos de la factura por el modelo LLM.
    """

    # Extraer el texto completo del archivo PDF.
    texto = extraer_texto_del_pdf(ruta_pdf)

    # Enviar el texto al modelo LLM para identificar
    # cliente, fecha e importe total.
    resultado = consultar_llm(texto)

    # Devolver la respuesta obtenida del modelo.
    return resultado


def exportar_csv(resultados, ruta_salida):
    """
    Exporta los resultados obtenidos del LLM a un archivo CSV.

    Args:
        resultados (list): Lista de respuestas generadas por el modelo.
        ruta_salida (str): Ruta donde se guardará el archivo CSV.
    """

    # Abrir o crear el archivo de salida.
    # "w" indica modo escritura.
    # newline="" evita líneas en blanco adicionales en Windows.
    # utf-8 permite almacenar correctamente caracteres como tildes o ñ.
    with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:

        # Crear el escritor CSV.
        # Se utiliza ":" como separador entre columnas.
        writer = csv.writer(archivo, delimiter=":")

        # Escribe la primera fila del archivo con los nombres de las columnas.
        writer.writerow(["Cliente", "Fecha", "Importe total"])

        # Recorre cada respuesta obtenida del modelo.
        for resultado in resultados:

            # El modelo devuelve los campos separados por comas.
            # split(",") divide la respuesta en tres elementos.
            #
            # strip() elimina espacios en blanco al principio y al final de cada campo.
            datos = [campo.strip() for campo in resultado.split(",")]

            # Escribir los datos como una nueva fila del CSV.
            writer.writerow(datos)