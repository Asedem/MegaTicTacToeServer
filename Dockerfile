FROM python:3.12

# Set the workdirectory in the container
WORKDIR /usr/src/app

# Copy the dependency file
COPY dependencies.txt .

# install the dependencies
RUN pip install -r dependencies.txt

# Copy the code from the source Folder
COPY src/ .

# Run the Python script
CMD ["python", "main.py"]