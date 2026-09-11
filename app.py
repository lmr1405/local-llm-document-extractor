from file_manager import obtener_facturas, procesar_factura, exportar_csv

def main():
    facturas = obtener_facturas("data")
    destino = "resultados_facturas.csv"
    resultados = []
   
    for factura in facturas:
        resultado = procesar_factura(factura)
        resultados.append(resultado)

    exportar_csv(resultados, destino)

  


if __name__ == "__main__":
    main()