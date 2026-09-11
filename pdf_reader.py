from pypdf import PdfReader

def extraer_texto_del_pdf(directorio):
    """
    Funcion que extrae de todas las paginas de un ficheron en PDF el texto 
    Como argumento recibe un directorio, que es donde se encuentra las facturas.
    El return es el texto completo que se extrae de los documentos.
    """
    reader = PdfReader(directorio)
    texto = ""

    for pag in reader.pages:
        contenido = pag.extract_text()
        if contenido:
            texto += contenido + "\n"
    return texto