from ultralytics import YOLO

# Load a model
#model = YOLO("deep_learnin/multitask/yolov8-cls.yaml")  # build a new model from scratch
model = YOLO("yolov8n-cls.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="deep_learnin/coco126_will_multi_class.yaml", project="deep_learnin", batch=50, epochs=100)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format