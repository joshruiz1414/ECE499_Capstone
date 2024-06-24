from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="local_env.yaml", epochs=1, imgsz=1280, plots=True)  # train the model