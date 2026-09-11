from pypdf import PdfReader

def extraer_texto_del_pdf(ruta_pdf):
    """
    Funcion que extrae de todas las paginas de un ficheron en PDF el texto 

    Args:
        ruta_pdf (str): Ruta del archivo PDF que se quiere procesar.

    Returns:
        str: Texto completo extraído del documento.
    """

    # Crear un objeto PdfReader a partir del archivo PDF indicado.
    # Este objeto nos permite acceder a todas las páginas del documento.
    reader = PdfReader(ruta_pdf)
    # Variable donde iremos acumulando el texto extraído de cada una de las páginas del PDF.
    texto = ""

    # Recorrer todas las páginas del documento.
    for pag in reader.pages:

        # Extraer el texto de la página actual.
        # Si la página contiene texto reconocible, devuelve un string.
        contenido = pag.extract_text()

        # Algunas páginas pueden no contener texto extraíble.
        # Comprobamos que 'contenido' tenga algún valor antes de añadirlo.
        if contenido:

            # Añadir el texto de la página al texto total.
            # "\n" introduce un salto de línea entre páginas.
            texto += contenido + "\n"

    # Devolver todo el texto extraído del PDF.
    return texto