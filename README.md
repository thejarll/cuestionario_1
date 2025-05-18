# Chatbot RAG con PDF usando Langchain y Ollama

Este proyecto es un chatbot que responde preguntas basadas en el contenido de un documento PDF. Utiliza la técnica de Recuperación Aumentada con Generación (RAG) para encontrar los fragmentos más relevantes del texto y generar una respuesta con un modelo de lenguaje local.

La aplicación permite al usuario subir un archivo PDF, procesarlo, generar embeddings utilizando el modelo `nomic-embed-text` y almacenar la información en una base vectorial con Chroma. Luego, cuando se realiza una pregunta, se recupera el contexto más relevante y se genera una respuesta usando el modelo `qwen:7b-chat` a través de Ollama. Todo esto ocurre de forma local, sin necesidad de enviar datos a la nube.

Para la interfaz gráfica se utiliza Streamlit. La aplicación también está integrada con Langsmith, lo que permite monitorear las preguntas realizadas, los fragmentos utilizados y las respuestas generadas. Esto facilita el análisis del rendimiento del sistema.

Para usar este proyecto necesitas tener Python 3.10 o superior, tener instalado Ollama y haber descargado los modelos `qwen:7b-chat` y `nomic-embed-text`. También es necesario configurar un archivo `.env` con tu clave de API de Langsmith y un nombre de proyecto. El archivo `pyproject.toml` ya contiene todas las dependencias necesarias para instalar con `uv`.

Una vez configurado todo, puedes ejecutar la aplicación con el comando `streamlit run src/app.py`. Esto abrirá una página web donde podrás subir tu PDF y comenzar a hacer preguntas relacionadas con su contenido.

Ejemplos de preguntas que puedes hacer: “¿De qué trata el documento?”, “¿Quién es el personaje principal?”, “¿Qué descubrió el profesor Angell?” o “¿Qué representa la ciudad de R’lyeh?”. El chatbot responderá basándose exclusivamente en el contenido del documento que hayas cargado (En este caso LOVECRAFT.PDF).

Algunas preguntas y su respuesta:

1. ¿De qué trata el cuento La llamada de Cthulhu?
El cuento narra el descubrimiento gradual y fragmentado de una aterradora verdad: la existencia de Cthulhu, una entidad cósmica que duerme en la ciudad sumergida de R’lyeh, y cuya influencia se manifiesta a través de sueños, cultos secretos y eventos inexplicables.

2. ¿Quién es el profesor Angell y qué papel tiene en la historia?
El profesor George Gammell Angell era un experto en lenguas semíticas de la Universidad de Brown. Es quien recopila los primeros indicios del culto a Cthulhu y deja notas detalladas que su sobrino (el narrador) descubre tras su misteriosa muerte.

3. ¿Qué descubrió el joven Wilcox en sus sueños?
Wilcox, un joven escultor sensible, comenzó a tener sueños extraños sobre estructuras ciclópeas y lenguas desconocidas. Estas visiones coincidieron con una ola global de pesadillas similares, lo que alertó al profesor Angell sobre una posible conexión con el culto de Cthulhu.

4. ¿Qué descubrió el inspector Legrasse en el pantano?
Legrasse descubrió una secta primitiva que realizaba rituales sangrientos en un pantano de Luisiana. Capturó una figura de piedra que representaba a Cthulhu y, al investigar, encontró que culturas separadas por miles de kilómetros compartían el mismo símbolo y adoración.
