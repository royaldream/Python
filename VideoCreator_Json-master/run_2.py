import cv2
import numpy as np
import os
 
from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    print(files)
    files.sort(key = lambda x: int(x[0:-4]))
 
    for i in range(len(files)):
        filename=pathIn+files[i]
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
def main():
    pathIn= './images/'
    pathOut = 'final_output.avi'
    fps = 1
    convert_frames_to_video(pathIn, pathOut, fps)
 
if __name__=="__main__":
    main()
