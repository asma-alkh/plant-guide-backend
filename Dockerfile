# Base Image
FROM python:3.13

# Working directory inside the container
WORKDIR /usr/src/backend

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Download wait-for-it.sh to ensure DB is ready
RUN apt-get update && apt-get install -y curl && \
    curl -o /usr/src/backend/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /usr/src/backend/wait-for-it.sh

# Copy project files
COPY . .

EXPOSE 8000

# Default command (runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]