# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install streamlit requests

# Expose the port the app runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]