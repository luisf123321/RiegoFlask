
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

from .suelo_sequence import SueloSequence
from .suelo_sequence_np import SueloSequenceNP
from .suelo_utils import SueloUtils    
    
suelo_utils = SueloUtils()

class SoilClassifier:
    
    def __init__(self):
        self.image = None
        self.countours_dict = {}
        self.height_dict = {}    
        self.img_size = (480,320)
        self.class_names = ["arcilla", "limo", "arena"]
        self.countours_dict = {}
        self.i = 0
        self.batch_size = 1
                
        
    def get_image(self):
        return self.image
    
    
    def get_contours(self):
        return self.countours_dict
        
        
    def get_soil_class(self, image_filename):
        self.image_filename = image_filename
        self.val_input_img_paths = [self.image_filename]
        self.val_target_img_paths = self.val_input_img_paths
                
        # self.val_target_img_paths = "*"
        
        img_raw = plt.imread(self.val_input_img_paths[self.i])
        
        #plt.imshow(img_raw)
        #plt.show()
        
        img_resized = load_img(self.image_filename, target_size=self.img_size)
        img_resized = np.asarray(img_resized)
        
        return self.get_soil_class_np(img_resized)
                    
    
    def get_soil_class_np(self, img_resized):
        # img_raw = img_raw[1000:,:]
        image_numpy = img_resized
        image_pil = Image.fromarray(np.uint8(image_numpy)).convert('RGB')
        
        new_size = (self.img_size[1], self.img_size[0])
        image_pil = image_pil.resize(new_size)
        
        img_resized = np.asarray(image_pil)
        
        
        self.image = img_resized
        
        
        print(img_resized.shape)
        #plt.imshow(img_resized)
        #plt.show()
        
        
        # val_gen = SueloSequence(self.batch_size,
        #                         self.img_size,
        #                         self.val_input_img_paths,
        #                         self.val_target_img_paths)
        
        
        val_gen = SueloSequenceNP(self.batch_size,
                                self.img_size,
                                image_pil)
        
                                # self.val_input_img_paths)
                                # ,self.val_target_img_paths)
        
        print(type(val_gen))
        
        
        img_masks = []
            
        for clase in self.class_names:
            try:
                #model_filename = "C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask\\app\\prediccion\\suelo_segmentation_" + clase + ".h5"
                model_filename = "app/prediccion/suelo_segmentation_" + clase + ".h5"
                
                print("*"*40)
                print(model_filename)
                
                model = keras.models.load_model(model_filename)
                print("*"*40)
                print("modelo", model)
                
                val_preds = model.predict(val_gen)
                print("*"*40)
                print("val_preds", val_preds)
                """Quick utility to display a model's prediction."""
                mask = np.argmax(val_preds[self.i], axis=-1)
                mask = np.expand_dims(mask, axis=-1)
                print("*"*40)
                print("img_np", img_np)
                img = PIL.ImageOps.autocontrast(keras.preprocessing.image.array_to_img(mask))
                img_np = np.asarray(img)
                print("*"*40)
                print("img_np", img_np)
                
                # plt.title(clase)
                # plt.imshow(img_np,cmap="gray")
                # plt.show()
                
                
                img_np = suelo_utils.get_binary_image(img_np)
                
                #plt.title(clase)
                #plt.imshow(img_np,cmap="gray")
                #plt.show()
                    
                
                # img_seg = img_resized + img_np
                # img_resized /= 255.0
                # img_np /= 255.0
                
                # print(img_resized.shape, np.max(img_resized))
                # print(img_np.shape, np.max(img_np))
                
                
                self.height_dict[clase] = suelo_utils.get_height(img_np)
                
                
                # img_mask = img_np
                img_mask = np.zeros(img_resized.shape, dtype=np.uint8)
                
                img_np = np.where(img_np == 0, 127, img_np)
                img_np = np.where(img_np == 255, 0, img_np)
                img_np = np.where(img_np == 127, 255, img_np)
                
                
                ret, binary = cv2.threshold(img_np,0,255,cv2.THRESH_BINARY_INV)
                contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                # print(len(contours), contours)
                self.countours_dict[clase] = contours
                
                img_mask[:,:,0] = img_np
                img_mask[:,:,1] = img_np
                img_mask[:,:,2] = img_np
                
                img_masks.append(img_mask)
                print("*"*20,"fin","*"*20)
            except Exception as ex:
                print("error image", ex)
            # self.height_dict[clase] = suelo_utils.get_height(img_np)
         
        
        for index , img_mask in enumerate(img_masks):
            # Mask input image with binary mask
            img_resized = cv2.bitwise_and(img_resized, img_mask)
            
            # Color background white
            if index == 0:
                img_resized[np.all(img_resized == (0, 0, 0), axis=-1)] = (255,0,0)
            if index == 1:
                img_resized[np.all(img_resized == (0, 0, 0), axis=-1)] = (0,255,0)
            if index == 2:
                img_resized[np.all(img_resized == (0, 0, 0), axis=-1)] = (0,0,255)
                
        #plt.imshow(img_resized)
        #plt.show()

            
        # print(self.height_dict)
        
        print("*"*20,"componentes","*"*20)
        components = suelo_utils.get_components(self.height_dict)
        # print(height_percentage)
        
        polygons, thresholds = self.get_polygons()
        #print(components)
        print({"components":components,
                "thresholds":thresholds,
                "polygons":polygons})
        return {"components":components,
                "thresholds":thresholds,
                "polygons":polygons}
        
        # return {'thresholds':thresholds}
        # return {'components':components}
    
    
    def get_polygons(self):
        data_dict = {}
        
        contours_dict = self.get_contours()
        
        threshold_dict = {}
        
        for key in contours_dict.keys():
            contours = contours_dict[key]
            # print(key, len(contours))
            # cv2.drawContours(image, contours, -1, (0,255,0),1)
        
            polygon_list = []
            _id = 0
            y_list = []
            
            for countour in contours:
                if len(countour) >= 3:
                    _id += 1
                    # print(len(countour))
                    polygon = []
                    for c in countour:
                        x = c[0][0]
                        y = c[0][1]
                        # print(x, y)
                        y_list.append(float(y))
                        polygon.append({"x":float(x),
                                        "y":float(y)})
                        if _id > 3:
                            break
                    polygon_dict = {'id':_id,
                                    'polygon':polygon}
                    polygon_list.append(polygon_dict)
                    # break
            
            if key == "arena":
                threshold_dict[key + "_bottom"] = np.max(y_list)
            threshold_dict[key + "_top"] = np.min(y_list)
                
            # data_obj = {"polygons":polygon_list}
            data_dict[key] = polygon_list
        
        # data_dict["thresholds"] = threshold_dict
        
        return data_dict, threshold_dict



# soil_classifier = SoilClassifier()
# image_filename = os.path.join("/home/juancastro/usal", "img_2.jpeg")

# # soil_class = soil_classifier.get_soil_class(image_filename)

# image_np = plt.imread(image_filename)
# soil_class = soil_classifier.get_soil_class_np(image_np)

# print(soil_class)



# image_directory = "/media/juancastro/data1/suelo/imagenes_prueba-20220721T201009Z-001"
# image_filename = os.path.join(image_directory,
#                               "imagenes_prueba",
#                               "EN8-In2D0L2A1-7.jpg")





# contours_dict = soil_classifier.get_contours()
# image = soil_classifier.get_image()
# print(image.shape)





# polygons = soil_classifier.get_polygons()


    
# contours[1]

# plt.imshow(image)
# plt.show()



# _class = "arena"



# import cv2
# import numpy as np

# # Load image, create mask, and draw white circle on mask
# image = cv2.imread('McS9K.png')
# mask = np.zeros(image.shape, dtype=np.uint8)
# mask = cv2.circle(mask, (260, 300), 225, (255,255,255), -1) 

# # Mask input image with binary mask
# result = cv2.bitwise_and(image, mask)
# # Color background white
# result[mask==0] = 255 # Optional

# # cv2.imshow('image', image)
# # cv2.imshow('mask', mask)
# # cv2.imshow('result', result)
# # cv2.waitKey()


