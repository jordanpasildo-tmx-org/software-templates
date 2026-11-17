# Internal Nexus mirror: ise-linux-container-release.releasevault.tmx.cloud/redhat-access-proxy/ubi9/ubi-minimal:latest
FROM registry.access.redhat.com/ubi9/ubi-minimal:latest

# Install Python 3.11, pip, and shadow-utils, then clean package cache immediately
RUN microdnf install -y --nodocs python3.11 python3.11-pip shadow-utils \
    && microdnf clean all \
    && rm -rf /var/cache/yum

# Prevent Python from writing .pyc bytecode and force unbuffered standard I/O for real-time logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:$PATH"

WORKDIR /app

# Create unprivileged user (UID 1001, GID 0 for OpenShift arbitrary UID compatibility)
RUN useradd -u 1001 -g 0 -m -s /sbin/nologin appuser \
    && chown -R 1001:0 /app \
    && chmod -R 0755 /app

# Copy dependency manifest and install dependencies without caching wheel archives
COPY src/requirements.txt /app/requirements.txt
RUN pip3.11 install --no-cache-dir --upgrade pip \
    && pip3.11 install --no-cache-dir -r /app/requirements.txt

# Copy application source code into working directory
COPY src/main.py /app/main.py

# Strictly enforce non-root execution
USER 1001

EXPOSE 8080

# Run FastAPI app with Uvicorn server on port 8080
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
