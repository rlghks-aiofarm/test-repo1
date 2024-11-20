# Base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy app code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port and run app
EXPOSE 5000
CMD ["python", "app.py"]
