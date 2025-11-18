# --- Use official lightweight Python image
FROM python:3.11-slim

# --- Set working directory
WORKDIR /app

# --- Copy code into container
COPY main.py .

# --- Set the default command to run your script
CMD ["python", "main.py"]
