import cv2
import os
import math
vidcap = cv2.VideoCapture(r'C:\Bochi_with_bin\bochi_with_bin.mp4')
success,image = vidcap.read()
count = 0
output_dir = r'C:\Bochi_with_bin\frames'
if not os.path.exists(output_dir):
  os.makedirs(output_dir)
while success:
  if count == 0:
    name = "0000"
  elif count == 1000:
    name = "1000"
  else:
    leading_0 = "0"*(3-int(math.log(count, 10)))
    name = leading_0 + str(count)
  frame_output_path = f"{output_dir}/{name}.jpg"
  cv2.imwrite(frame_output_path, image) 
  print(f"{frame_output_path} is saved")  
  success,image = vidcap.read()
  count += 1
