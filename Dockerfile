FROM python:3.10-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Paso 1: actualizar y reparar paquetes básicos
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils \
    && dpkg --configure -a \
    && apt-get install -y --no-install-recommends \
        git \
        curl \
        build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Paso 2: directorio de trabajo
WORKDIR /app

# Paso 3: instalar Python packages
RUN pip install --no-cache-dir mlflow bentoml jupyterlab

# Exponer puertos comunes
EXPOSE 5000 3000 8888

# Comando por defecto
CMD ["/bin/bash"]
