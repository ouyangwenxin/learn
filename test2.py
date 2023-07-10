import cv2 as cv
import numpy as np



def main():
    
    video_caputre = cv.VideoCapture(r"1.mp4")
 
   
    fps = video_caputre.get(cv.CAP_PROP_FPS)
    width = video_caputre.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video_caputre.get(cv.CAP_PROP_FRAME_HEIGHT)
 
    print("fps:", fps)
    print("width:", width)
    print("height:", height)
 
    
    size = (int(height), int(width / 2))
 
    
    videp_write = cv.VideoWriter("videoFrameTarget.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
 
    
    success, frame_src = video_caputre.read()
    while success and not cv.waitKey(1) == 27: 
 
        
        frame_target = frame_src[0:int(width/2), 0:int(height)]
        
        videp_write.write(frame_target)
 
        
        
       
        
        cv.imshow("video", frame_target)
        
        
        success, frame_src = video_caputre.read()
 
    print("视频裁剪完成")
 
    
    cv.destroyWindow("video")
    
    video_caputre.release()
 
 
if __name__=="__main__":
    main()
