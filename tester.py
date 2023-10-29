from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2
import pyttsx3
engine = pyttsx3.init()


model = YOLO("best_lisa_2.pt")

results = model.predict(source="0", show=True, stream=True, conf=0.4)
names = model.names

print(names)

probs = None
masks = None
prev_sign = None

for r in results:
    for c in r.boxes.cls:
        print(names[int(c)])

        curr_sign = names[int(c)]
        if prev_sign != curr_sign:
            if curr_sign == "stop":
                engine.say("Stop the vehicle")
            elif curr_sign == "merge":
                engine.say("Roads Merging Ahead")
            elif curr_sign == "laneEnds":
                engine.say("Current Lane Ending Ahead")
            elif curr_sign == "school":
                engine.say("Be careful school zone ahead")
            elif curr_sign == "addedLane":
                engine.say("Added Lane ahead")
            elif curr_sign == "pedestrianCrossing":
                engine.say("Beware pedestrian Crossing ahead")
            elif curr_sign == "signalAhead":
                engine.say("Upcoming signal")
            elif curr_sign.lower().count("speedlimit") > 0:
                engine.say("New speed limit up ahead")
            elif curr_sign == "keepRight":
                engine.say("Keep Right")
            elif curr_sign == "stopAhead":
                engine.say("Stop sign ahead")
            else:
                engine.say(curr_sign)

            engine.runAndWait()
            prev_sign = curr_sign
