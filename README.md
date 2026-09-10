# Local LLM Document Extractor
Aplicacion desarrollada en Python que utiliza un modelo de lenguaje local mediante  
la API de Ollama para extraer informacion estructurada de documentos PDF.
  
## Descripcion
Este proyecto muestra como ejecutar un modelo de lenguaje de gran tamaño (LLM) de forma local  
e interactuar con el mediante una API.
  
## Objetivo
El objetivo principal es explorar el uso de modelos de lenguajes locales para el procesamiento  
de documentos sin depender de servicios externos en la nube.  

## Funcionalidades
- Ejecucion de un LLM en local mediante Ollama
- Comunicacion con el modelo mediante una API local
- Extracion de texto desde archivos PDF
- Extracion automatica de informacion relevante
- Generacion de resultados estructurados
- Procesamiento local de los documentos.

## Uso
### Instalar Ollama
Descargar e instalar Ollama desde su pagina oficial  
[Web Oficial de Ollama](https://ollama.com/)  
Una vez instalado, comprobar que funciona correctamente
```bash
ollama --version
```
### Instalar el modelo
Para este proyecto se utiliza el modelo qwen2.5:3b descargalo con:
```bash
ollama pull qwen2.5:3b
```
Comprobamos que el modelo esta instalado
```bash
ollama list
```
### Ejecutar el modelo
Para iniciar el modelo
```bash
ollama run qwen2.5:3b
```
### Instalar dependencias de Python
Desde la carpeta del proyecto:
```bash
pip install -r requirements.txt
```
### Ejecutar la aplicacion
```bash
python app.py
```