# ML-Zoomcamp-Midterm-Project

## Introduction
<p>This dataset contains employee information, including their demographics, job role, job satisfaction, work-life balance, and whether they have left the company (attrition).</p>

The focus of the task is to build predictive models which can identify which employees are at a higher risk of leaving the company. This could help in taking some proactive measures to retain valuable employees. This dataset is collected for a Human resource application and the source is from Kaggle: https://www.kaggle.com/datasets/itssuru/hr-employee-attrition

Attrition: Represents the measure of employees leaving a company voluntarily or involuntarily. HR uses the figure to track and understand how things are going at a company

Following these instructions, you can easily set up, run, and interact with the Flask-based prediction service.
The step-by-step instructions, start from setting up the environment with pipenv to interfacing with the prediction endpoint.

## Set up Environment and Component Testing
### Clone the Application Code
Please ensure you have the application code (including Pipfile, Pipfile.lock, and app.py) in your working directory. If it's in a repository, clone it:

* $ git clone <(https://github.com/Emmanuel-Ayeni/mlzoomcamp-midterm-project)>
* $ cd <repository_directory>

### Install pipenv
* $ pip install pipenv

### Set Up the Virtual Environment
Run pipenv install to create a virtual environment and install all dependencies specified in the Pipfile.lock:
* $ pipenv install

### Activate the Virtual Environment
Enter the pipenv shell to work within the virtual environment:
* $ pipenv shell

### Run the attrition-final.py
Extract the dataset from Kaggle via API, generate an XGBoost model and download the attrition model by running the attrition-final.py script:
* Ensure you set up a Kaggle API before running the script.
* $ python attrition-final.py

### Run the Flask Application
Start the Flask application by running the app.py script:
* $ python app.py
This will start the Flask application, and you should see an output similar to:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

  ![image](https://github.com/user-attachments/assets/d3b9e392-700f-4da8-b12f-9dcac744a672)

* Open a new terminal window to interact with the web service.
* Start up a Jupyter notebook.
* Open up the predict_test.ipynb and use the test to run JSON formatted data for the prediction service.

  ![image](https://github.com/user-attachments/assets/e1c3539b-36ca-4664-addb-0eb323a80db9)

* Prediction result is noted after the last cell.
* Check the Service log message as 200: OK or indicates a successful request.
![image](https://github.com/user-attachments/assets/af0d84f2-adcc-43bd-8689-25bd558535e5)

  
### Interfacing with the Prediction Endpoint
#### Using Python
#### Using Curl
#### Using Postman

## Deploying with Docker

### Build the Docker image:
* $ docker build -t attrition-predict-app .
![image](https://github.com/user-attachments/assets/47f85cf6-59fa-4504-a502-91a352c6b7e0)

### Run the container:
* $ docker run -p 9696:9696 attrition-predict-app
  ![image](https://github.com/user-attachments/assets/71bb161c-9191-4ad4-8f4a-c9b718f2a91c)

### Use the same steps above (curl, Postman, or Python) to interact with the application.
