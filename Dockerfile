FROM python:3.10-slim

WORKDIR /app

# System deps: curl for healthcheck, build tools for some wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl build-essential \
    && rm -rf /var/lib/apt/lists/*

# en_core_web_md is installed straight from requirements.txt (the model the code
# loads); no separate spacy download step is needed.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# Hosted demos (e.g. Hugging Face Spaces) serve the app inside an iframe behind a
# proxy; XSRF protection has to be off there or file uploads never complete.
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false \
    STREAMLIT_SERVER_ENABLE_CORS=false

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
