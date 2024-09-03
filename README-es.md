# RAG from scratch

Este proyecto implementa un asistente de seguros utilizando un modelo de Recuperación Aumentada de Generación (RAG) para responder preguntas relacionadas con seguros.
Puede ser usado para responder preguntas sobre cualquier tema que se le pase.

## Características

- Utiliza la API de OpenAI para generar respuestas.
- Implementa la similitud de Jaccard para seleccionar los documentos más relevantes.
- Preprocesa los documentos para mejorar la comparación.
- Selecciona los k documentos más relevantes para cada consulta.

## Requisitos

- OpenAI API key

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/miguelozaalon/RAG-from-scratch.git
   cd RAG-from-scratch
   ```

2. Instala las dependencias:
   ```
   pip install python-dotenv openai
   ```

3. Crea un archivo `.env` en el directorio raíz y añade tu clave API de OpenAI:
   ```
   OPENAI_API_KEY=tu-clave-api-aqui
   ```

## Uso

Ejecuta el script principal:

```
python rag.py
```

Ingresa tu consulta cuando se te solicite y el asistente generará una respuesta basada en la información de seguros proporcionada.

## Estructura del Código

- `rag.py`: Contiene toda la lógica del asistente, incluyendo:
  - Carga de documentos
  - Cálculo de similitud de Jaccard
  - Preprocesamiento de documentos
  - Selección de documentos relevantes
  - Generación de respuestas utilizando la API de OpenAI

## Funcionamiento

1. El usuario ingresa una consulta.
2. El sistema calcula la similitud entre la consulta y los documentos disponibles.
3. Se seleccionan los k documentos más relevantes.
4. Se genera un prompt para la API de OpenAI incluyendo los documentos seleccionados.
5. La API de OpenAI genera una respuesta basada en el prompt y la consulta del usuario.
6. Se muestra la respuesta al usuario.


## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
