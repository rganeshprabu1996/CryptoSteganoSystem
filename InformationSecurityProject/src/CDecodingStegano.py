from PIL import Image

def decode(): 
    img = input("\nEnter the name of Receiver Steganographed image : ") 
    image = Image.open(img, 'r')    
    data = '' 
    imgdata = iter(image.getdata())     
    while (True): 
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]] 
        binstr = ''        
        for i in pixels[:8]: 
            if (i % 2 == 0): 
                binstr += '0'
            else: 
                binstr += '1'               
        data += chr(int(binstr, 2)) 
        if (pixels[-1] % 2 != 0): 
            en_msg=data
            return en_msg