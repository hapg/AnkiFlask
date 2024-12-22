# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables to ensure Python runs optimally in Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask requests

# Install UV and set up the environment
RUN pip install --no-cache-dir uv
RUN uv init flask-env && uv install

# Expose the port the Flask app runs on
EXPOSE 443

# Activate the UV environment and run the Flask server
CMD ["uv", "run", "flask"]