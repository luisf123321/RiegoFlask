#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:42:47 2022

@author: juancastro
"""

import numpy as np


class SueloUtils:
    
    def __init__(self):
        pass
    
    
    def get_pixels(self, img_np):
        # pixels = set()
        # # print(img_np.shape)
        
        # for x in range(img_np.shape[0]):
        #     for y in range(img_np.shape[1]):
        #         pixels.add(img_np[x][y])
        # # print(pixels)
        
        pixels = np.unique(img_np)
        
        return pixels
    
    
    def get_bordes(self, mask):
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
    
    
    def get_height(self, img_np):
        x1, y1, x2, y2 = self.get_bordes(img_np)
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
        
        
        
        # p25 = np.percentile(heights, 25)
        # p75 = np.percentile(heights, 75)
        
        # heights = list(filter(lambda score: score >= p25, heights))
        # heights = list(filter(lambda score: score <= p75, heights))
        
            
        print(heights, len(heights), np.mean(heights), np.std(heights))
    
    
        return round(np.mean(heights),2)
    
    
    def get_components(self, height_dict):
        height_total = 0


        #calcular altura total

        for key in height_dict.keys():
            height_total += height_dict[key]
        
        height_percentage = {}

        #calcular porcentajes 
        
        for key in height_dict.keys():
             height_percentage[key] = round((height_dict[key] / height_total)*100,2)
        
        # print(height_percentage)
        
        return height_percentage
    
    
    def get_binary_image(self, img_np):
        pixels = self.get_pixels(img_np)
        print("pixels (1): ", pixels)
                
        img_np = np.where(img_np == 255, 3, img_np)
        img_np = np.where(img_np == 0, 255, img_np)
        img_np = np.where(img_np == 3, 0, img_np)
        
        img_np = np.where(img_np == 127, 0, img_np)
        
        pixels = self.get_pixels(img_np)
        print("pixels (2): ", pixels)
        
        return img_np
    
    
    
    
    
    
    
    