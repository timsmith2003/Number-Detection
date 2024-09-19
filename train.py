from ultralytics import YOLO

# Load the correct YOLO model, adjust the model architecture or path if needed
model = YOLO("yolov8n.yaml")  # Change to the correct model file if custom

# Train the model with the specified data file
model.train(data="data.yaml", epochs=6)
