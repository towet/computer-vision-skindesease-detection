# classy.py
from roboflow import Roboflow

# Define the classification model loading function
def load_classification_model():
    rf = Roboflow(api_key="3qHwr0QGGcvuZ1ApfphH")
    project = rf.workspace().project("dell")
    model = project.version(1).model
    return model

# Export the model object with the correct variable name
classification_model = load_classification_model()