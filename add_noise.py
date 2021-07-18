import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import util
import cv2
import os

def add_noise(img, noise_type, coeff):

    img = np.array(img)
    noise_gs_img = util.random_noise(img,mode="gaussian",mean=coeff)
    noise_salt_img = util.random_noise(img,mode="salt")
    noise_pepper_img = util.random_noise(img,mode="pepper",amount=coeff)
    noise_speckle_img = util.random_noise(img,mode="speckle")

    if (noise_type == "Gaussian"):
        return noise_gs_img
    elif (noise_type == "Salt"):
        return noise_salt_img
    elif (noise_type == "Pepper"):
        return noise_pepper_img
    elif (noise_type == "Speckle"):
        return noise_speckle_img

def compute_video_noise(type_of_noise, coeff):
    i = 0
    while i< 300:
        saveByImage(i,type_of_noise, i/100000)
        
        i = i + 1
    

def saveByImage(sample_name,type_of_noise, coeff):

    cap = cv2.VideoCapture("my_video/stego.avi")

    count = 1
    # Read until video is completed
    while(count<2):
    
    # Capture frame-by-frame
        ret, frame = cap.read()
    
        if ret == True:
            frame1 = add_noise(frame, type_of_noise, coeff)
            frame1 = np.uint8(255 * frame1)
            # Display the resulting frame
            cv2.imshow('Frame', frame1)
            print(frame1)
            cv2.imwrite('my_video/image_decomposition/stego_noise/stego_bruite_sample'+str(sample_name)+'.png', frame1)
            count = count + 1

        # Press Q on keyboard to  exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else :
            break
    # When everything done, release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()


