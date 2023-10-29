# road_sign_detection_with_audio_alert

### Detects road signs and give audio alert in realtime
______________
## Instructions :

### To train
- Download the python notebook and upload it to colab.
- Go to roboflow dataset link provided.
- Go to Dataset -> 2021-11-27 3:57pm v1 Nov 28, 2021
- Click download dataset. (you have to be logged into roboflow)
- Select format as YoloV8 and click show download code.
- Click continue and copy the jupyter code shown.
- Paste this code in the colab notebook in the cell where it is written to paste.
- Change runtime to T4 GPU.
- (optional) change model size and epoch size if you wish. The present model and epoch size took about 2 hours to train.
- Run the cells.
- You will find the model in runs folder named best.pt
- Download best.pt

### To run
- copy the best.pt to folder where you have tester.py
- change model = YOLO("best_lisa_2.pt") to model = YOLO("best.pt")
- install all required libraries
- run

## Note :
- Have used yolov8s.pt
- Trained for 25 epochs
- detects only about 10 - 12 signs reliably

## Results : 

![Results](/Images/results.png)
> Results

![confusion_matrix](/Images/confusion_matrix_normalized.png)
> Confusion Matrix Normalized

![F1_Curve](/Images/F1_curve.png)
> F1 Curve

![PR_curve](/Images/PR_curve.png)
> PR Curve

### Packages Used :
- ultralytics (YoloV8)
- OpenCV
- pyttsx3
- roboflow
- IPython
- os

### Source :
- YoloV8 : https://github.com/ultralytics/ultralytics
- Lisa Dataset : https://universe.roboflow.com/dakota-smith/lisa-road-signs
