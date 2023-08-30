# Use an official Python as the base image (slim is for a lighter version)
FROM python:3.11-slim  

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

COPY dblp.json .

CMD ["python3", "app.py", "flask", "run"]


