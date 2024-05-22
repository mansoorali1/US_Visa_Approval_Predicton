# US Visa Approval Predicton
This project provides an end-to-end MLOps solution for predicting US visa approvals. Given specific input features such as education level, job experience, wage and etc., the model predicts whether a visa will be approved or denied. The solution is fully hosted on AWS, leveraging various AWS services for seamless deployment and scalability.

## Table of Contents
- [Architecture](#-architecture)
- [Languages & Tools](#-languages--tools)
- [Directory Structure](#-directory-structure)
- [Data](#-data)
- [Output](#-output)
  
## Architecture
**1. Data Ingestion:**  The data is stored in a MongoDB database and is fetched from there for processing

**2. Data Preprocessing:** Data cleaning and transformation are performed to prepare the data for model training

**3. Model Training:** Various models are trained on the preprocessed data. The models evaluated include K-Nearest Neighbors (KNN) and Random Forest

**4. Model Evaluation:** Among the different models, KNN and Random Forest were the top performers. The KNN model has an accuracy of 96.66%

**5. Deployment:** In the deployment phase, the selected model is uploaded to an AWS S3 bucket. FastAPI is used to build the API. A containerized application is created using Github Action, and the Docker image is pushed to Amazon Elastic Container Registry (ECR). This image is then pulled into an EC2 instance, which is connected to GitHub via a self-hosted runner. Whenever code changes or new code is pushed to GitHub, the CI/CD pipeline is triggered, ensuring that the model is continuously integrated and deployed on AWS

## Languages & Tools
<div align="">
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
  </a>
  <a href="https://www.mongodb.com" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="60" height="60"/>
  </a>
  <a href="https://code.visualstudio.com" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" alt="vscode" width="60" height="60"/>
  </a>
  <a href="https://aws.amazon.com/s3/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws s3" width="60" height="60"/>
  </a>
  <a href="https://www.docker.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="60" height="60"/>
  </a>
  <a href="https://fastapi.tiangolo.com" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" alt="fastapi" width="60" height="60"/>
  </a>
  <a href="https://github.com/features/actions" target="_blank" rel="noreferrer">
    <img src="https://avatars.githubusercontent.com/u/44036562?s=200&v=4" alt="github actions" width="60" height="60"/>
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html" width="60" height="60"/>
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css" width="60" height="60"/>
  </a>
</div>

## Directory Structure

```
C:.
|   .dockerignore
|   .gitignore
|   app.py
|   demo.py
|   demo2.py
|   Dockerfile
|   LICENSE
|   README.md
|   requirements.txt
|   setup.py
|   template.py
|
+---.github
|   \---workflows
|           aws.yaml
|
+---config
|       model.yaml
|       schema.yaml
|
+---flowcharts
|
+---notebook
|   |   1_EDA_US_visa.ipynb
|   |   2_Feature_Engineering_and_Model_Training.ipynb
|   |   data_drift_demo_evidently.ipynb
|   |   mongoDB_demo.ipynb
|   |   prediction_trial.ipynb
|   |   trial_aws_connection.ipynb
|   |   trial_mongo.ipynb
|   |   Visadataset.csv
|   |
+---static
|   \---css
|           style.css
|
+---templates
|       usvisa.html
|
+---us_visa
    |   __init__.py
    |
    +---cloud_storage
    |   |   aws_storage.py
    |   |   __init__.py
    |
    +---components
    |   |   data_ingestion.py
    |   |   data_transformation.py
    |   |   data_validation.py
    |   |   model_evaluation.py
    |   |   model_pusher.py
    |   |   model_trainer.py
    |   |   __init__.py
    |   
    |
    +---configuration
    |   |   aws_connection.py
    |   |   mongo_db_connection.py
    |   |   __init__.py
    |
    +---constants
    |   |   __init__.py
    |
    +---data_access
    |   |   usvisa_data.py
    |   |   __init__.py
    |
    +---entity
    |   |   artifact_entity.py
    |   |   config_entity.py
    |   |   estimator.py
    |   |   s3_estimator.py
    |   |   __init__.py
    |
    +---exception
    |   |   __init__.py
    |
    +---logger
    |   |   __init__.py
    |
    +---pipeline
    |   |   prediction_pipeline.py
    |   |   training_pipeline.py
    |   |   __init__.py
    |
    +---utils
        |   main_utils.py
        |   __init__.py
```
## Data
https://www.kaggle.com/datasets/moro23/easyvisa-dataset?resource=download
## Output
![US_Visa_Prediction_App](https://github.com/mansoorali1/US_Visa_Approval_Predicton/assets/73877240/9ce44d98-6038-476c-a57b-15b2354f0b2f)

**Youtube URL Deployment**

**Youtube URL Application Demo**
