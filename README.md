# Chatbot RAG con PDF usando Langchain y Ollama

Este proyecto es un chatbot que responde preguntas basadas en el contenido de un documento PDF. Utiliza la técnica de Recuperación Aumentada con Generación (RAG) para encontrar los fragmentos más relevantes del texto y generar una respuesta con un modelo de lenguaje local.

La aplicación permite al usuario subir un archivo PDF, procesarlo, generar embeddings utilizando el modelo `nomic-embed-text` y almacenar la información en una base vectorial con Chroma. Luego, cuando se realiza una pregunta, se recupera el contexto más relevante y se genera una respuesta usando el modelo `qwen:7b-chat` a través de Ollama. Todo esto ocurre de forma local, sin necesidad de enviar datos a la nube.

Para la interfaz gráfica se utiliza Streamlit. La aplicación también está integrada con Langsmith, lo que permite monitorear las preguntas realizadas, los fragmentos utilizados y las respuestas generadas. Esto facilita el análisis del rendimiento del sistema.

Para usar este proyecto necesitas tener Python 3.10 o superior, tener instalado Ollama y haber descargado los modelos `qwen:7b-chat` y `nomic-embed-text`. También es necesario configurar un archivo `.env` con tu clave de API de Langsmith y un nombre de proyecto. El archivo `pyproject.toml` ya contiene todas las dependencias necesarias para instalar con `uv`.

Una vez configurado todo, puedes ejecutar la aplicación con el comando `streamlit run src/app.py`. Esto abrirá una página web donde podrás subir tu PDF y comenzar a hacer preguntas relacionadas con su contenido.

Ejemplos de preguntas que puedes hacer: “¿De qué trata el documento?”, “¿Quién es el personaje principal?”, “¿Qué descubrió el profesor Angell?” o “¿Qué representa la ciudad de R’lyeh?”. El chatbot responderá basándose exclusivamente en el contenido del documento que hayas cargado (En este caso LOVECRAFT.PDF).
