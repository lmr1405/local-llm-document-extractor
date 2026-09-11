import os
import csv

from pdf_reader import extraer_texto_del_pdf
from llm_client import consultar_llm

def obtener_facturas(directorio):
    archivos_factura = []

    for archivo in os.listdir(directorio):
        if "factura" in archivo.lower() and archivo.lower().endswith(".pdf"):
            ruta_completa = os.path.join(directorio, archivo)
            archivos_factura.append(ruta_completa)

    return archivos_factura



def procesar_factura(ruta_pdf):
    texto = extraer_texto_del_pdf(ruta_pdf)
    resultado = consultar_llm(texto)

    return resultado


def exportar_csv(resultados, ruta_salida):
    with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo, delimiter=":")

        writer.writerow(["Cliente", "Fecha", "Importe total"])

        for resultado in resultados:
            datos = [campo.strip() for campo in resultado.split(",")]
            writer.writerow(datos)