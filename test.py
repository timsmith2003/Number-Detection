from ultralytics import YOLO

# Load your trained model (adjust the path to your saved weights)
model = YOLO('best.pt')  # Adjust path as necessary

# Test on a single image
results = model.predict(source='dog.jpg', save=True)  # Replace with your image path



