import requests

base_url = "http://localhost:11434/api/chat"
myModel = "qwen2.5:3b"

def consultar_llm(texto):
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

    body = {
        "model": myModel,
        "messages": [
            {
                "role": "system", "content": prompt
            },
            {
                "role": "user", "content": texto
            }
        ],
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }

    response = requests.post(base_url, json=body)

    response.raise_for_status()
    datos= response.json()
    return datos["message"]["content"]