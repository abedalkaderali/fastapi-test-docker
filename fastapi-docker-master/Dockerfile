# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000
RUN apt update && apt install -y netcat-openbsd
# Copy the entrypoint script into the container
ENV PYTHONPATH=/app

# Set executable permission inside the image (✅ this works across OS)
RUN chmod +x /app/start.sh

CMD ["./start.sh"]
