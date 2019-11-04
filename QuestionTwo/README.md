# Object Tracking with OpenCV

## Requirements
sys should be usable when Python is installed
imutils ```pip install imutils```
cv2 ```pip install opencv-contrib-python```
Note: sudo may be required

## How To Run
Usage from the command line.
```
python ObjectTracking.py Bolt.mp4
python ObjectTracking.py Verstappen.mp4
python ObjectTracking.py Bike.mp4
python ObjectTracking.py McGregor.mp4
```
This can also be added to the configurations easily within PyCharm

### Selecting a bounding box
1. press ```s``` to initiate a bounding box selection
2. Click and drag to cover the desired area. A crosshair will appear to help make the selection more accurate
3. press ```ENTER``` or ```SPACE``` after selecting the target area

An error occurs if a singular pixel is selected. for example only clicking and not dragging

### Quit
Press ```q``` to quit

### Example Output
[YouTube Link](https://youtu.be/dw0BsDgDXos)