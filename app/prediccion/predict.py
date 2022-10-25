
from IPython.display import Image, display
from tensorflow.keras.preprocessing.image import load_img
import PIL
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from .usco_suelo import UscoSuelo

def get_pixels(img_np):
    pixels = set()
    print(img_np.shape)
    
    for x in range(img_np.shape[0]):
        for y in range(img_np.shape[1]):
            pixels.add(img_np[x][y])
    print(pixels)
    return pixels

def get_bordes(mask):
    x1 = 0
    x2 = mask.shape[1]-1
    y1 = 0
    y2 = mask.shape[0]-1
    
    for y in range(mask.shape[0]-1):
        line = mask[y:y+1,:] 
        info = np.sum(line)
        if info > 0:
            y1 = y
            # print(info,y1)
            break
        
    for y in range(mask.shape[0]-1, 0, -1):
        line = mask[y-1:y,:] 
        info = np.sum(line)
        
        # print(info,y)
        
        if info > 0:
            y2 = y
            # print(info,y2)
            break        
    
    for x in range(mask.shape[1]-1):
        line = mask[:,x:x+1] 
        # print(line.shape)
        info = np.sum(line)
        # print(info, x, x+1)
        if info > 0:
            x1 = x
            # print(info,x1)
            break
    
    for x in range(mask.shape[1]-1,0,-1):
        line = mask[:,x-1:x] 
        info = np.sum(line)
        
        if info > 0:
            x2 = x
            # print(info,x2)
            break
        
    return x1, y1, x2, y2   
    

def predict(ruta):
    height_dict = {}    
    img_size = (480,320)

    class_names = ["arcilla", "limo", "arena"]

    i = 0
    batch_size = 1
    for clase in class_names:

        # clase = "arcilla"
        # clase = "limo"
        # clase = "arena"
        
        
        
        model_filename = "app/prediccion/segmentation_model_" + clase + ".h5"
        #model.save(model_filename)
        
        model = keras.models.load_model(model_filename)
               
        val_input_img_paths = [ruta]
        val_target_img_paths = val_input_img_paths
        
        val_gen = UscoSuelo(batch_size, img_size, val_input_img_paths, val_target_img_paths)
        
        #val_gen = OxfordPets(batch_size, img_size, val_input_img_paths, val_target_img_paths)
        
        val_preds = model.predict(val_gen)
        
        """Quick utility to display a model's prediction."""
        mask = np.argmax(val_preds[i], axis=-1)
        mask = np.expand_dims(mask, axis=-1)
        img = PIL.ImageOps.autocontrast(keras.preprocessing.image.array_to_img(mask))
        # print(img.size())
        #display(img)
        img_np = np.asarray(img)
        # print(img_np)
        # plt.title(clase)
        # plt.imshow(img_np,cmap="gray")
        # plt.show()
        
        
        # print(img_np.shape)
        
        
        pixels2 = get_pixels(img_np)
        pixels = np.unique(img_np)
        print("pixels: ", pixels, pixels2)
    
        
        img_np = np.where(img_np == 255, 3, img_np)
        img_np = np.where(img_np == 0, 255, img_np)
        img_np = np.where(img_np == 3, 0, img_np)
        
        
        img_np = np.where(img_np == 127, 0, img_np)
        
        
        pixels2 = get_pixels(img_np)
        pixels = np.unique(img_np)
        print("pixels (2): ", pixels, pixels2)
        
        
        
        plt.title(clase)
        
        x1, y1, x2, y2 = get_bordes(img_np)
        print(x1, y1, x2, y2)
        
        
        parts = 20
        width = x2 - x1
        step = int(width / parts)
        print("width: ", width)
        
        
        heights = []
        
        for x in range(x1, x2, step):
            img_line = img_np[y1:y2,x+1]
            # img_line.shape
            # print(img_line)
            whites = 0
            for y in range(len(img_line)):
                # print(x, y, img_line[y])
                if img_line[y] == 255:
                    whites += 1  
            heights.append(whites)
            # print(whites)        
        
        
        print(heights, sorted(heights), len(heights), np.mean(heights), np.std(heights))
        
        heights = sorted(heights)
        
        
        heights = heights[2:-2]  
            
        print(heights, len(heights), np.mean(heights), np.std(heights))


        height_dict[clase] = np.mean(heights)

    print(height_dict)
    height_total = 0
    for key in height_dict.keys():
        height_total += height_dict[key]

    height_percentage = {}
    for key in height_dict.keys():
        height_percentage[key] = round((height_dict[key] / height_total)*100,2)
    print(height_percentage)
    return height_percentage
