from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import load_img

class SueloSequenceNP(keras.utils.Sequence):
    """Helper to iterate over the data (as Numpy arrays)."""

     # def __init__(self, batch_size, img_size, input_img_paths):
    def __init__(self, batch_size, img_size, input_img):
        # , target_img_paths):
        self.batch_size = batch_size
        self.img_size = img_size
        self.input_img = input_img
        # self.input_img_paths = input_img_paths
        # self.target_img_paths = target_img_paths

    def __len__(self):
        # return len(self.target_img_paths) // self.batch_size
        return 1  #len(self.input_img_paths) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, target) correspond to batch #idx."""
        i = idx * self.batch_size
        
        # batch_input_img_paths = self.input_img_paths[i : i + self.batch_size]
        # batch_target_img_paths = self.target_img_paths[i : i + self.batch_size]
        
        x = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")      
        x[0] = self.input_img 
        
        
        
        # for j, path in enumerate(batch_input_img_paths):
        #     img = load_img(path, target_size=self.img_size)
        #     print("x", type(img), img)
        #     x[j] = img
            
        
        
        y = np.zeros((self.batch_size,) + self.img_size + (1,), dtype="uint8")
        y[0] = np.zeros((self.batch_size,) + self.img_size + (1,), dtype="uint8")
            
            
        # y = np.zeros((self.batch_size,) + self.img_size + (1,), dtype="uint8")
        # for j, path in enumerate(batch_target_img_paths):
        #     img = load_img(path, target_size=self.img_size, color_mode="grayscale")
        #     y[j] = np.expand_dims(img, 2)
        #     # Ground truth labels are 1, 2, 3. Subtract one to make them 0, 1, 2:
        #     y[j] -= 1
            
        #     y1 = np.zeros((self.batch_size,) + self.img_size + (1,), dtype="float32")
        #     print("y1", type(y1), y1.shape, y1)
            
            
        # print("y", type(y), y.shape, y)
            
        return x, y