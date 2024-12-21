# (Alpine is not supported by packages in LlamaIndex)
# Use Red Hat Universal Base Image with Python (Large Image, only for Production)
# FROM registry.access.redhat.com/ubi9/python-39
# Just use 3.12-slim it just works and is smaller
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
ADD requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy the application code
COPY . .

# Command to run the application
CMD ["python", "run.py"]
