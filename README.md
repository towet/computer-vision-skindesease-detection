
## Skin Disease Detection Using computer vission and openAI llm to describe the desease 
 
 This project utilizes YOLOv5, a cutting-edge object detection algorithm, to identify and classify various skin diseases from images. Designed for dermatologists, healthcare professionals, and researchers, this tool enhances preliminary screening and diagnosis, offering high accuracy and efficiency. It is particularly beneficial for telemedicine applications, especially in remote or underserved areas with limited access to dermatological expertise.


## Authors

- [@franklin](https://github.com/towet)


## Badges

 [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Appendix


: Data Collection and Preprocessing
Data Sources: datasets used for training and testing the model. Sources  include dermatological image databases, publicly available medical image repositories

Image Annotation: T manual annotation using Roboflow, ensuring that each image is accurately labeled with the correct skin disease class. It also discusses the criteria and guidelines followed to maintain consistency and accuracy in annotations.


## Documentation

Overview
This project combines YOLOv5, a powerful object detection algorithm, with Streamlit, a Python library for creating interactive web applications, to detect and classify various skin diseases from images. It serves as a tool for dermatologists, healthcare professionals, and researchers to efficiently screen and diagnose skin conditions based on uploaded images.

Features
Object Detection: Utilizes resnet's efficient object detection capabilities to identify skin lesions and diseases in images.

Interactive Web Application: Built with Streamlit to provide a user-friendly interface for uploading images, viewing predictions, and exploring detection results.

Real-Time Inference: Enables quick and accurate inference, making it suitable for rapid clinical decision-making and telemedicine applications.

Customizable Deployment: Easily deployable on various platforms, including local machines, cloud services, and Streamlit Sharing for online accessibility.

Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/towet/machinelearning-skindesease-detection
cd your_repo
Install Dependencies:

Ensure Python 3.6+ is installed.
Install required packages:
install openai
bash
Copy code
pip install -r requirements.txt
Download  Weights:


Usage
Run the Streamlit App:

bash
Copy code
streamlit run app.py
Open your web browser and go to http://localhost:8501 to interact with the application.
Upload an Image:

Click on the file uploader and select an image file (JPEG or PNG).
View Results:

Once the image is uploaded, the application will display the uploaded image and the detected skin diseases along with confidence scores.
 the application will leverage open ai to discrie the skin infection and possile solutions

