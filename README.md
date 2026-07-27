# BimBamBuy Agent

Asistente para responder preguntas sobre políticas de devolución y reembolso de BimBamBuy usando Gemini, LangChain y Gradio.

## Objetivo

Construir un agente capaz de leer la política de devoluciones y reembolsos de BimBamBuy y responder preguntas en lenguaje natural con base en el PDF provisto.

## Arquitectura

1. Se carga el PDF con la política de BimBamBuy.
2. Se divide el contenido en fragmentos pequeños.
3. Se crean embeddings con Gemini.
4. Se construye o carga el índice FAISS.
5. Se recuperan los fragmentos más relevantes según la pregunta.
6. Gemini genera la respuesta usando solo ese contexto.
7. Gradio muestra la conversación en una interfaz web.

## Tecnologías

- Python
- LangChain
- Gemini API
- Gradio
- FAISS
- PyPDF

## Instalación local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Ejecución

```bash
python app.py
```

## Ejemplos de preguntas

- ¿Cuánto tiempo tengo para solicitar un retracto?
- ¿Qué pasa si recibo un producto incorrecto?
- ¿En cuánto tiempo se procesa un reembolso aprobado?
- ¿Qué evidencias debo enviar si el producto llegó dañado?

## Ejemplos de respuestas

- El retracto puede solicitarse dentro de los 10 días corridos posteriores a la recepción.
- Si el producto llegó incorrecto, la solicitud debe ingresarse dentro de las 48 horas.
- Un reembolso aprobado se procesa entre 5 y 10 días hábiles.
- El soporte puede solicitar foto, video, etiqueta de envío o comprobante de recepción según el caso.

## Evidencia de despliegue

- Captura de la interfaz en Gradio.
- Enlace público de la app desplegada en OCI.