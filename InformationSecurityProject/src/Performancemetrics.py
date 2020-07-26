from PIL import Image
import cv2
import numpy as np
import math
#import matplotlib.pyplot as plt

def main():
    imga = input("\nEnter the Original image : ") 
    image1 = Image.open(imga, 'r')
    image1.show()
    imgb = input("\nEnter the Stegano image : ") 
    image2 = Image.open(imgb, 'r')
    image2.show()
    
    MSE = np.square(np.subtract(image1,image2)).mean()
    print("MSE:", MSE)

    PSNR = 10*math.log(255*255/MSE) / math.log(10)
    print("PSNR:",PSNR)
    ts=373
    nb=(3*3)*3
  
    cc=ts/nb
    print("Carrier capacity is", cc)
    k=1 
    n=ts/8
    
    ee=((k+1)*n)/k
    print("Embedded efficiency is", ee)
  
    img1 = cv2.imread('steganoimage.png',0)
   # histr1 = cv2.calcHist([img1a],[0],None,[256],[0,256]) 
    #plt.plot(histr1)
    #plt.show()
    img2 = cv2.imread('compressedimage.png',0)
    histr2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
    #plt.plot(histr2)
   # plt.show()

if __name__ == '__main__' : 
    main()