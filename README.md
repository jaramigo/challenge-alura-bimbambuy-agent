# BimBamBuy Agent

Asistente para responder preguntas sobre políticas de devolución y reembolso de BimBamBuy usando Gemini, LangChain y Gradio.

## Objetivo

Construir un agente capaz de leer la política de devoluciones y reembolsos de BimBamBuy y responder preguntas en lenguaje natural con base en el PDF provisto.

## Arquitectura

PDF -> Loader -> Splitter -> Embeddings -> FAISS -> Retriever -> Gemini -> Gradio

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