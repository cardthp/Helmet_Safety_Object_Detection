# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import importlib

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util


def inference1(sess,detection_boxes,image_tensor, detection_scores, detection_classes, num_detections,frame_expanded):
    inf = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: frame_expanded})

    return inf