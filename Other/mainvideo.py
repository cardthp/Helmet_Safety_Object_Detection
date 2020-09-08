# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import importlib
import pdf
import mailpdf

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Import from Other file
import Object_detection_webcam_inference as obj
import build_model


# Initialize webcam feed
video = cv2.VideoCapture(0)
ret = video.set(3,1280)
ret = video.set(4,720)

#Set Sequence for each image
count = 0

#Set If found things it will set to True
flagjer = False

#Set Delay Time for Not Save Image every seconds 
c = 0 

sess, category_index, detection_boxes, image_tensor, detection_scores, detection_classes, num_detections = build_model.build()

while(True):

    # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    ret, frame = video.read()
    frame_expanded = np.expand_dims(frame, axis=0)

    # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes, num) = obj.inference1(sess, detection_boxes, image_tensor, detection_scores, detection_classes, num_detections, frame_expanded)
    
        #if classes == 1:
        #    print("Found")

    print(f"Num: {num}"+"is Found")
    #print(f"Classes: {classes}"+"is Found")
    #print(f"Boxes: {boxes}")
    #print(f"Score: {scores}")


    # Draw the results of the detection (aka 'visulaize the results')
    vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)

    c += 1
    if c >= 10:
        if (np.squeeze(scores)[0]>0.5) & (np.squeeze(classes)[0]==1):
            cv2.putText(frame,"Pass!", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,128,0))
            if flagjer == False :
                #cv2.imwrite('C:/Tensorflow/models/research/object_detection/zresult/image%d.jpg' % count, frame)
                cv2.imwrite('C:/Tensorflow/models/research/object_detection/zresult/image.jpg', frame)
                #count += 1
                flagjer = True
                pdf.create_pdf()
                mailpdf.send_mail()
                
        elif np.squeeze(scores)[0]<0.5:
            flagjer = False
        c = 0

    #print(np.squeeze(classes)[0])
    #print(np.squeeze(scores)[0])
    #print(f"Classes: {classes}"+"is Found")
    #print(f"cate: {category_index}"+"is Found")

    # All the results have been drawn on the frame, so it's time to display it.
    cv2.imshow('Object detector', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Clean up
video.release()
cv2.destroyAllWindows()