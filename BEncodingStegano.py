from PIL import Image
import Main as m
global savemessage

def encode(data):
    global savemessage, en_msg
    img = input("\nEnter the Randomly chosen image : ") 
    image = Image.open(img, 'r')
    image.show()
    compress = image.resize((2048, 2048))
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