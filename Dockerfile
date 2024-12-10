


































# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set up W&B Token Login
ENTRYPOINT ["/app/docker_entrypoint.sh"]

# Default command to run the training script
CMD ["python3", "main.py"]

