FROM python:3.9-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
EXPOSE 8080





# FROM python:3.9-slim-buster

# # Update and install awscli
# RUN apt-get update && apt-get install -y awscli && rm -rf /var/lib/apt/lists/*

# # Set the working directory
# WORKDIR /app

# # Copy requirements.txt first to leverage Docker cache
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Command to run the application
# CMD ["python3", "app.py"]
