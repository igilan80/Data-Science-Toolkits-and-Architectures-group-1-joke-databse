
# Base Image
FROM python:3.9-slim

# Set a non-root user for security
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies and clean up to reduce image size
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache

# Copy the rest of the application code
COPY . .

# Switch to non-root user
USER appuser

# Use environment variables for secrets (e.g., W&B token)
ENV SECRET_API_KEY="your_api_key"

# Expose necessary ports (if applicable)
EXPOSE 8000

# Set the default command for the container
CMD ["python3", "main.py"]

