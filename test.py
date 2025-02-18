from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("deep_learnin/coco126_copy_30_clean_70/weights/best.pt")  # load a pretrained model (recommended for training)

# Use the model
# model.train(data="coco128.yaml", project="deep_learnin", batch=32, epochs=100)  # train the model
#metrics = model.val(data="/home/kyle/adversarial_deep_learning_v8/deep_learnin/coco126_kyle_noise.yaml")  # evaluate model performance on the validation set
metrics = model.val(data="/Users/wsolow/Desktop/OSU HW/AI535/Final_Project/adversarial_deep_learning_v8/deep_learnin/coco126_kyle_noise.yaml")
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
