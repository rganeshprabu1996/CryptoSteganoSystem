import AEncryptionElgamal as ee
import DDecryptionElgamal as de
import BEncodingStegano as es
import CDecodingStegano as ds

from math import pow
import random
import csv
a = random.randint(2, 5) 

def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b) 
    
def gen_key(q): 
    key = random.randint(pow(2, 5), q) 
    while gcd(q, key) != 1: 
        key = random.randint(pow(2, 5), q) 
    return key 

def power(a, b, c): 
    x = 1
    y = a 
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c; 
        y = (y * y) % c 
        b = int(b / 2) 
    return x % c 

def genData(data): 
        newd = []         
        for i in data: 
            newd.append(format(ord(i), '08b')) 
        return newd

def modPix(pix, data):    
    datalist = genData(data) 
    lendata = len(datalist) 
    imdata = iter(pix) 
    for i in range(lendata): 
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]] 
        for j in range(0, 8): 
            if (datalist[i][j]=='0') and (pix[j]% 2 != 0):                 
                if (pix[j]% 2 != 0): 
                    pix[j] -= 1                    
            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
                pix[j] -= 1
        if (i == lendata - 1): 
            if (pix[-1] % 2 == 0): 
                pix[-1] -= 1
        else: 
            if (pix[-1] % 2 != 0): 
                pix[-1] -= 1
        pix = tuple(pix) 
        yield pix[0:3] 
        yield pix[3:6] 
        yield pix[6:9] 

def encode_enc(newimg, data): 
    w = newimg.size[0] 
    (x, y) = (0, 0)     
    for pixel in modPix(newimg.getdata(), data): 
        newimg.putpixel((x, y), pixel) 
        if (x == w - 1): 
            x = 0
            y += 1
        else: 
            x += 1  

def sender():
    global en_msg,msg,p,q,h,g,key,i
    q = random.randint(pow(2,5),pow(2,6))
    g = random.randint(2,q)
    print("\n$$$$$$$$$$$$$$$$$$$   SENDER OPERATION   $$$$$$$$$$$$$$$$$$$$")
    sel=int(input("\n1.Enter the Secret Message\n2.Enter the Secret Dataset\n"))
    if (sel==1):
        message = input("\nEnter the Secret Message :   ")
        msg=message
        key = gen_key(q)
        h = power(g, key, q)
        print("g used                   :  ", g) 
        print("g^a used                 :  ", h)
        en_msg, p = ee.encrypt(msg,q,h,g)
        ee.save(en_msg)
        return(en_msg)
    elif(sel==2):
        message = input("\nEnter the Secret Dataset :   ")
        with open(message) as f:
            reader=csv.reader(f)
            for row in reader:
                print(row)
            with open(message) as f:
                s = f.read() + '\n' 
            l=(repr(s))
        msg=l
        key = gen_key(q)
        h = power(g, key, q)
        print("\ng used                   :  ", g) 
        print("g^a used                 :  ", h)
        en_msg, p = ee.encrypt(msg,q,h,g)
        ee.save(en_msg)
        return(en_msg)

def decod():
    result = ds.decode()
    print("Decoded Encrypted Message  :  ", result)
    print("Decoded Successfully") 

def receiver():
    dr_msg = de.decrypt(en_msg,p,key,q) 
    dmsg = ''.join(dr_msg)
    print("\nDecrypted Message          :  ", dmsg)
    print("Decrypted Successfully")   
    print("***Secret Message has been receiver from the sender***")

def wrong():
    print("\nWrong Input")

def main(): 
    print("::::: Welcome to Crypto Stegano System :::::")
    global en_msg
    sel=int(input("\n\nSelect the Operation\n1.Sender Operation\n2.Receiver Operation\n"))
    if (sel==1):
        sel=int(input("\n************** 1.Sender Operation************** \n1.Encryption \n2.Encoding \n"))
        if (sel==1):
            sender()
            sel=str(input("\nDo you wish to continue (Y or N):  \n"))
            if (sel=='Y' or 'y'):
                sel=int(input("\n**************1.Sender Operation**************\n1.Encryption\n2.Encoding\n"))
                if (sel==2):
                    #dat=int("".join(map(str,en_msg)))
                    data=str(en_msg) + str(p) 
                    print("Encrypted data and Key: ",data)
                    es.encode(data)
                    sel=int(input("\nSelect the Operation\n1.Sender Operation\n2.Receiver Operation\n"))
                    if (sel==2):
                        sel=int(input("\n**************2.Receiver Operation**************\n1.Decoding\n2.Decryption\n"))
                        if (sel==1):
                            decod()
                            sel=str(input("\nDo you wish to continue (Y or N):  \n"))
                            if (sel=='Y' or 'y'):
                                sel=int(input("\n**************2.Receiver Operation**************\n1.Decoding\n2.Decryption\n"))
                                if (sel==2):
                                    receiver()
                                else:
                                    wrong()
                            else:
                                wrong()
                        else:
                            wrong()
                    else:
                        wrong()
                else:
                    wrong() 
            else:
                wrong() 
        else:
            wrong() 
    else:
        wrong()            
if __name__ == '__main__' : 
    main()