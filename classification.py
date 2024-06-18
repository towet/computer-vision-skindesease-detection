from roboflow import Roboflow
rf = Roboflow(api_key="3qHwr0QGGcvuZ1ApfphH")
project = rf.workspace().project("dell")
model = project.version(1).model

# infer on a local image
print(model.predict("skin.jpeg").json())

# visualize your prediction
print( model.predict("skin.jpeg").save("prediction.jpg"))

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True).json())