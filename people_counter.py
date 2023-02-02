import cv2
import imutils
from imutils.object_detection import non_max_suppression
import numpy as np
import argparse


# Opencv pre-trained SVM with HOG people features
# Initialize the HOG descriptor/person detector
#(Note1)
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def MainDetector(image):
    #(Note2)
    (rects, weights) = HOGCV.detectMultiScale(image, winStride=(4, 4),padding=(7, 7), scale=1.05)
    # Converting image parts(x,y,w,h) into numpy array
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    # Applies non-max supression from imutils package to kick-off overlapped boxes
    #(Note3)
    result = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    return result



# Giving the arguments function (in this func we just set an image argument)
#(Note4)
def ArgParser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default=None, help="path to image test file directory")
    args = vars(ap.parse_args())
    return args


# Detector, Counter and Rectangle drawer function
# (Detection is done with using the MainDetector function )
def People_Detector_Counter(image_path):
    result = []
    # read image and resize it
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    clone = image.copy()
    if len(image) <= 0:
        print("[ERROR] Could not read your local image")
        return result
    print("[INFO] Detecting people")
    result = MainDetector(image)
    
    # Drawing rectangle around the people and count them with a loop
    counter = 0
    for (xA, yA, xB, yB) in result:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
        counter += 1

    print(f"[INFO] People Count : {counter}")
    cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Saving the result image after the drawing rectangles
    #(Note5) 
    cv2.imwrite("result.png", np.hstack((clone, image)))
    return (result, image)



# Giving the image path then check it and also run People_Detector_Counter function
def Check_Save(args):
    image_path = args["image"]

    if image_path != None:
        print("[INFO] Attempting to read image")
        (result, image) = People_Detector_Counter(image_path)
        print("[INFO] Saving result image")



#main function (for running other functions)
def main():
    args = ArgParser()
    Check_Save(args)


# when we want a file that can be run as the main program
#(Note6)
if __name__ == '__main__':
    main()