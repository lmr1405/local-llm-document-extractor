import requests

# URL del endpoint de chat de la API local de Ollama.
# Ollama escucha por defecto en el puerto 11434.
base_url = "http://localhost:11434/api/chat"
# Modelo que utilizará Ollama para procesar la petición.
myModel = "qwen2.5:3b"

def consultar_llm(texto):
    """
    Envía el texto de una factura al modelo LLM local mediante la API de Ollama
    y devuelve la información extraída por el modelo.

    Args:
        texto (str): Texto extraído previamente del archivo PDF.

    Returns:
        str: Respuesta generada por el modelo con los datos solicitados.
    """

    # Prompt de sistema.
    # Aquí indicamos al modelo qué tarea debe realizar y en qué formato
    # queremos que devuelva la respuesta.
    prompt = """
    Vas a recibir el texto de una factura.

    Extrae únicamente los siguientes datos:

    - Cliente
    - Fecha
    - Importe total

    Devuelve la respuesta en una sola línea y separada por una coma

    Cliente, Fecha, Importe total

   La fecha ponla en forma dd/mm/yyyy
    No añadas ninguna explicación adicional.
    """


    # Cuerpo de la petición que se enviará a la API de Ollama.
    # Es un diccionario de Python que requests convertirá a JSON.
    body = {
        # Indicar qué modelo debe utilizar Ollama.
        "model": myModel,
        # Lista de mensajes que forman la conversación con el modelo.
        "messages": [
            # El mensaje con rol "system" define el comportamiento
            # y las instrucciones generales que debe seguir el modelo.
            {
                "role": "system", "content": prompt
            },
            # El mensaje con rol "user" contiene los datos reales
            # que queremos que el modelo procese.
            {
                "role": "user", "content": texto
            }
        ],
        # False indica que queremos recibir la respuesta completa
        # de una sola vez, en lugar de recibirla fragmentada.
        "stream": False,
        # Opciones adicionales de generación del modelo.
        "options": {
            # Una temperatura baja hace que la respuesta sea
            # más predecible y menos creativa.
            # Esto es conveniente para tareas de extracción de datos.
            "temperature": 0.2
        }
    }

    # Realizar una petición HTTP POST al servidor local de Ollama.
    # json=body convierte automáticamente el diccionario a JSON.
    response = requests.post(base_url, json=body)

    # Si la API devuelve un código de error HTTP
    # (por ejemplo 404 o 500), se genera una excepción.
    response.raise_for_status()

    # Convertir la respuesta JSON recibida de Ollama
    # en un diccionario de Python.
    datos= response.json()

    # Acceder únicamente al contenido textual generado por el modelo.
    return datos["message"]["content"]