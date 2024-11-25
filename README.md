# ML-Zoomcamp-Midterm-Project
Following these instructions, you can easily set up, run, and interact with the Flask-based prediction service.
The step-by-step instructions, start from setting up the environment with pipenv to interfacing with the prediction endpoint.

## Set up Environment and Component Testing
### Clone the Application Code
Please ensure you have the application code (including Pipfile, Pipfile.lock, and app.py) in your working directory. If it's in a repository, clone it:

* git clone <(https://github.com/Emmanuel-Ayeni/mlzoomcamp-midterm-project)>
* cd <repository_directory>

### Install pipenv
* pip install pipenv

### Set Up the Virtual Environment
Run pipenv install to create a virtual environment and install all dependencies specified in the Pipfile.lock:
* pipenv install

### Activate the Virtual Environment
Enter the pipenv shell to work within the virtual environment:
* pipenv shell

### Run the Model code
Download the attrition model by running the attrition-final.py script:
* python attrition-final.py

### Run the Flask Application
Start the Flask application by running the app.py script:
* python app.py
This will start the Flask application, and you should see an output similar to:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

### Interfacing with the Prediction Endpoint
#### Using Python
#### Using Curl
#### Using Postman
## ..................................................................................................

## Deploying with Docker

### Build the Docker image:
* docker build -t attrition-predict-app .

### Run the container:
* docker run -p 9696:9696 attrition-predict-app
### Use the same steps as above (curl, Postman, or Python) to interact with the application.







