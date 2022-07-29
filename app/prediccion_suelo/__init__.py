from flask import Flask, request, jsonify
from flask_cors import CORS

from PIL import Image
import skimage.io
import base64
import io
import numpy as np
import matplotlib.pyplot as plt


import os
# from IPython.display import Image, display
import PIL
import cv2
# from PIL import ImageOps
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img

#from suelo_10 import SoilClassifier