import sys
import imutils
import cv2

OPENCV_OBJECT_TRACKERS = {
    # Operates at a much lower frame rate in comparison to other tracking algorithms.
    # Works well with all of my different videos
    "csrt": cv2.TrackerCSRT_create,

    # Was not able to maintain an accurate success rate. High frame rate is not helpful to display accuracy
    "kcf": cv2.TrackerKCF_create,

    # Performance is mediocre, as it does not always know when tracking has failed.
    "boosting": cv2.TrackerBoosting_create,

    # Not as bad as boosting but tracking failure is not reported reliably.
    "mil": cv2.TrackerMIL_create,

    # Has the ability to present lots of false positives.
    "tld": cv2.TrackerTLD_create,

    # Excellent tracking failure reporting. Works very well when the motion is predictable and there is no occlusion.
    # Struggles to keep up during the end of the McGregor.mp4 clip
    "medianflow": cv2.TrackerMedianFlow_create,

    # I have specifically picked clips that has a focus that wont move off the edge of the screen
    "mosse": cv2.TrackerMOSSE_create
    }

# grab the appropriate object tracker using our dictionary of
# OpenCV object tracker objects
tracker = OPENCV_OBJECT_TRACKERS["csrt"]()

# initialize the bounding box coordinates of the object we are going
# to track
initBB = None

# Grab a reference to the video file
video_capture = cv2.VideoCapture(sys.argv[1])

# loop over frames from the video stream
while True:
    # grab the current frame
    frame = video_capture.read()[1]

    # check to see if we have reached the end of the stream
    if frame is None:
        break

    # resize the frame for faster processing and grab the frame dimensions
    frame = imutils.resize(frame, width=750)  # Value of 750 can be changed
    (H, W) = frame.shape[:2]

    # check to see if we are currently tracking an object
    if initBB is not None:
        # grab the new bounding box coordinates of the object
        (success, box) = tracker.update(frame)

        # check to see if the tracking was a success
        if success:
            (x, y, w, h) = [int(v) for v in box]
            # Draws a green rectangle if it is a success over the target area
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # show the output frame
    cv2.imshow("Frame", frame)
    # Waits for a valid key press
    key = cv2.waitKey(1) & 0xFF

    # If the 's' key is selected, we are going to "select" a bounding box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track
        # ROI = Return On Investment
        initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)

        # start the object tracker using the given box coordinates
        tracker.init(frame, initBB)

    # if the `q` key was pressed, break from the loop to then exit
    elif key == ord("q"):
        break

# close all windows
cv2.destroyAllWindows()
