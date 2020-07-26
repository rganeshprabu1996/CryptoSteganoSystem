from PIL import Image
import os
import random
import AAF_Main as m
global savemessage
import math
global compress
def encode(data):
    global savemessage, en_msg
    count = 1    
    while count < 300:
        path = r"E:\M.E. C.S.E. PROJECT\Project\MEProject\Dataset\FlagDataset/"
        random_filename=random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path,x))])
        image=Image.open(r"E:\M.E. C.S.E. PROJECT\Project\MEProject\Dataset\FlagDataset/" +str(random_filename))        
        image.show()
        string = random_filename
        print(("The Randomly chosen image is: " ) + string.replace(".png",""))
        count +=1
        break
    compress = image.resize((2000, 2000))
    t = input("Enter the name of Compressed image   : ")
    compress.save(t, str(t.split(".")[1].upper())) 
    compress.show()   
    print("Embedded data in Image          :",data)    
    if (len(str(data)) == 0): 
        raise ValueError('Data is empty') 
    newimg = compress.copy()
    m.encode_enc(newimg, data)     
    new_img_name = input("Enter the name of Sender Steganographed image   : ") 
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper())) 
    newimg.show()             
    print("Encoded Successfully\n")
    print("Sender Operation completed successfully\n")