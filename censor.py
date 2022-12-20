import cv2
import numpy as np
import keyboard
import time
import os
import sys
import json

drawing = False
x1, y1 = -1,-1
x2, y2 = -1, -1
src_dir = r"C:\Bochi_with_bin\frames"
dst_dir = r"C:\Bochi_with_bin\censored"
map_path = r"C:\Bochi_with_bin\map.json"
if not os.path.exists(dst_dir):
   os.makedirs(dst_dir)

def draw_rectangle(event, x, y, flags, param):
   global x1, y1, x2, y2, drawing, img, orig_img
   if event == cv2.EVENT_LBUTTONDOWN:
      drawing = True
      x1 = x
      y1 = y
   elif event == cv2.EVENT_MOUSEMOVE:
      if drawing == True:
         img = orig_img.copy()
         cv2.rectangle(img, (x1, y1), (x, y),(0, 0, 255),1)
      else:
         if x1 + y1 + x2 + y2 != -4:
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
   elif event == cv2.EVENT_LBUTTONUP:
      drawing = False
      img = orig_img.copy()
      cv2.rectangle(img, (x1, y1), (x, y), (0, 0, 255), 1)
      x2 = x
      y2 = y

if os.path.exists(map_path):
   with open(map_path, "r") as read_file:
      mapping = json.load(read_file)
else:
   mapping = {}

for src_file in os.listdir(src_dir):
   if src_file in mapping:
      continue
   cv2.namedWindow(src_file, cv2.WINDOW_FULLSCREEN)
   cv2.moveWindow(src_file, 0, 0)
   cv2.setMouseCallback(src_file, draw_rectangle)
   src_file_path = os.path.join(src_dir, src_file)
   dst_file_path = os.path.join(dst_dir, src_file)
   orig_img = cv2.imread(src_file_path)
   img = orig_img.copy()
   while True:
      cv2.imshow(src_file, img)
      cv2.waitKey(200)
      if keyboard.is_pressed("y"):
         cv2.destroyAllWindows()
         img = orig_img.copy()
         ROI = img[y1:y2, x1:x2]
         blur = cv2.GaussianBlur(ROI, (17, 17), cv2.BORDER_DEFAULT) 
         img[y1:y2, x1:x2] = blur
         cv2.imwrite(dst_file_path, img)
         mapping[src_file] = (x1, y1, x2, y2)
         with open(map_path, "w") as write_file:
            json.dump(mapping, write_file)
         break
      elif keyboard.is_pressed("n"):
         cv2.destroyAllWindows()
         img = orig_img.copy()
         cv2.imwrite(dst_file_path, img)
         mapping[src_file] = None
         with open(map_path, "w") as write_file:
            json.dump(mapping, write_file)
         break
      elif keyboard.is_pressed("q"):
         cv2.destroyAllWindows()
         sys.exit()
         

