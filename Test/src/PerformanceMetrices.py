from PIL import Image
import numpy as np
import math
import cv2
import random
from matplotlib import pyplot as plt
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
    if (imga=='1a.png' and imgb=='1b.png'):
        ts=2246390-2204104
        nb=(3*3*3)*96
        cc=ts/nb
        print("Carrier capacity is", cc)   
        k=32*9
        n=ts/(32*14)
        ee=((k+1)/k)*n
        print("Embedded efficiency is", ee)
        img1 = cv2.imread('1a.png',0)
        histr1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
        plt.plot(histr1)
        plt.show()
        img2 = cv2.imread('1b.png',0)
        histr2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
        plt.plot(histr2)
        plt.show()
        plt.hist(img2.ravel(),256,[0,256])
        plt.show()
    elif (imga == '2a.png' or imgb=='2b.png' ):
        ts=1114112-1106108
        nb=(3*3*3)*24
        cc=ts/nb
        print("Carrier capacity is", cc)
        k=24*9 
        n=ts/(32*8/3)
        ee=((k+1)/k)*n
        print("Embedded efficiency is", ee)
        img1 = cv2.imread('2a.png',0)
        histr1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
        plt.plot(histr1)
        plt.show()
        img2 = cv2.imread('2b.png',0)
        histr2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
        plt.plot(histr2)
        plt.show()
        plt.hist(img2.ravel(),256,[0,256])
        plt.show()
    elif (imga=='3a.png' and imgb=='3b.png'):
        ts=1048701-1037790
        nb=(3*3*3)*24
        cc=ts/nb
        print("Carrier capacity is", cc) 
        k=24*9
        n=ts/(32*11/3)
        ee=((k+1)/k)*n
        print("Embedded efficiency is", ee) 
        img1 = cv2.imread('3a.png',0)
        histr1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
        plt.plot(histr1)
        plt.show()
        img2 = cv2.imread('3b.png',0)
        histr2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
        plt.plot(histr2)
        plt.show()
        plt.hist(img2.ravel(),256,[0,256])
        plt.show()
    elif (imga=='4a.png' and imgb=='4b.png'):  
        ts=1490106-1477953
        nb=(3*3*3)*32
        cc=ts/nb
        print("Carrier capacity is", cc)    
        k=32*9
        n=ts/(32*4)
        ee=((k+1)/k)*n
        print("Embedded efficiency is", ee)
        img1 = cv2.imread('4a.png',0)
        histr1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
        plt.plot(histr1)
        plt.show()
        img2 = cv2.imread('4b.png',0)
        histr2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
        plt.plot(histr2)
        plt.show()    
        plt.hist(img2.ravel(),256,[0,256])
        plt.show()
    elif (imga=='5a.png' and imgb=='5b.png'):
        ts=3288026-3275011
        nb=(3*3*3)*32
        cc=ts/nb
        print("Carrier capacity is", cc)   
        k=32*9
        n=ts/(32*9/2)
        ee=((k+1)/k)*n
        print("Embedded efficiency is", ee) 
        img1 = cv2.imread('5a.png',0)
        histr1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
        plt.plot(histr1)
        plt.show()
        img2 = cv2.imread('5b.png',0)
        histr2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
        plt.plot(histr2)
        plt.show()    
        plt.hist(img2.ravel(),256,[0,256])
        plt.show()
    elif (imga=='6a.png' and imgb=='6b.png'):
        ts=1410046-1394957
        nb=(3*3*3)*32
        cc=ts/nb
        print("Carrier capacity is", cc)   
        k=32*9
        n=ts/(32*5)
        ee=((k+1)/k)*n
        print("Embedded efficiency is", ee)
        img1 = cv2.imread('6a.png',0)
        histr1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
        plt.plot(histr1)
        plt.show()
        img2 = cv2.imread('6b.png',0)
        histr2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
        plt.plot(histr2)
        plt.show()
        plt.hist(img2.ravel(),256,[0,256])
        plt.show()
    else:
        print("Wrong Input")    
 
if __name__ == '__main__' : 
    main()