import os
import time
import cv2
orig_vid = cv2.VideoCapture(r'null')
fps = orig_vid.get(cv2.CAP_PROP_FPS)
fps = 24
frame_dir = r"C:\Bochi_with_bin\frames"
censor_frame_dir = r"C:\Bochi_with_bin\censored"
out = cv2.VideoWriter(r"C:\Bochi_with_bin\bochi_with_bin_censored.mp4", cv2.VideoWriter_fourcc(*'DIVX'), fps, (1920, 1080))
cnt = 0
start = time.time()
filenames = sorted(list(os.listdir(frame_dir)))
for filename in filenames:
  frame_path = os.path.join(frame_dir, filename)
  censor_frame_path = os.path.join(censor_frame_dir, filename)
  if os.path.exists(censor_frame_path):
      frame_image = cv2.imread(censor_frame_path)
  else:
      frame_image = cv2.imread(frame_path)
  out.write(frame_image)
  cnt += 1
  print(f"{cnt} out of {len(filenames)} finished, take time {time.time() - start} s")
out.release()
