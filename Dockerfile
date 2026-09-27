FROM python:3.11.6-slim

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers AS ROOT
RUN playwright install --with-deps chromium

# Create non-root user
RUN useradd -m pwuser

# Copy browser binaries from root to pwuser
RUN mkdir -p /home/pwuser/.cache/ms-playwright \
    && cp -r /root/.cache/ms-playwright/* /home/pwuser/.cache/ms-playwright/ \
    && chown -R pwuser:pwuser /home/pwuser/.cache

# Create logs directory with correct permissions
RUN mkdir -p /app/logs && chmod -R 777 /app/logs

# Create quarantine directory for flaky test quarantine
RUN mkdir -p /app/quarantine && chmod -R 777 /app/quarantine

# Copy project code
COPY src/ /app/src/
COPY tests/ /app/tests/
COPY pytest.ini /app/pytest.ini

# Fix permissions for project folder
RUN chown -R pwuser:pwuser /app

# -----------------------------
# CI METADATA (added correctly)
# -----------------------------
RUN echo "BUILD_TIME=$(date)" > /app/metadata.txt \
    && echo "BROWSER=chromium" >> /app/metadata.txt

# Switch to non-root user
USER pwuser

CMD ["pytest",