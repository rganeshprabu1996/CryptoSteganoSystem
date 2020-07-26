import AAA_Encryption_Elgamal as ee
import AAB_Optimization_EPSO as ep
import AAC_Embedding_QStegano as es
import AAD_Retrieval_QStegano as ds
import AAE_Decryption_Elgamal as de

from math import pow
import random
import csv
import PIL
a = random.randint(2, 5) 
import sys
global user, passwrd
global user, passwrd
def register(): 
    print("\nWelcome to Inter Defence Communication Registration form")
    org=str(input("\nEnter your organization name: "))
    identitys=str(input("\nEnter your organization ID: "))
    user=str(input("\nEnter your new user name: "))
    passwrd=str(input("\nEnter your new password: "))
    print("\nVerify your details:")
    print("\nOrganization name: ", org)
    print("\nOrganization ID: ", identitys)
    print("\nUser name: ", user)
    print("\nPassword: ",passwrd)
    selects=str(input("\nDetails verified and are correct (Y or N):  \n"))
    if (selects=='Y' or 'y'):
        print("\nAccount Registered Successfully")
    else:
        print("\nUser Terminated")
        sys.exit()
        
    print("\nWelcome to Inter Defence Communication Login page")
    us=str(input("\nEnter your user name: "))
    pw=str(input("\nEnter your password: "))
    if(us==user and pw==passwrd):
        print("\nAdmin Login successfully")
    elif(us=='default' and pw=='default'):
        print("\nGuest Login successfully")
    else:
        print("\nEnter correct user name or password")
        sys.exit()
def user():
    return(user)
def passwrd():
    return (passwrd)
def login():
    print("\nWelcome to Inter Defence Communication Login page")
    us=str(input("\nEnter your user name: "))
    pw=str(input("\nEnter your password: "))
    if(us==user and pw==passwrd):
        print("\nAdmin Login successfully")
    elif(us=='default' and pw=='default'):
        print("\nGuest Login successfully")
    else:
        print("\nEnter correct user name or password")
        sys.exit()

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
    sys.exit()
def home():
    choose=int(input("\nSelect the Operation\n 1.Register \n 2.Login\n"))
    if (choose==1):
        register()
    else:
        login()
def orglist(ret):
    print("\nSelect the Sender Organization (India)")
    print("\n1.Aeronotical Development Agency\n2.Defence Exhibition Organization\n3.Defence Intelligence Agency\n4.Defence Planning Committee\n5.Defence Research and Development Organization\n6.Directorate of Air Intelligence\n7.Directorate of Military Intelligence\n8.Directorate of Naval Intelligence\n9.Indian Air Force\n10.Indian Army\n11.Indian Coastal Gaurd\n12.Indian Combined Defence Service\n13.Indian Navy\n14.Indigenous Defence Equipment Exporters Association\n15.Indian Space Research Organization\n16.MARCOS\n17.Military Engineer Services\n18.National Defence Acadamy\n19.Ordnance Factory Board\n20.Samtel Avionics\n")
    sel=int(input("Choose the Sender Defence agency: "))
    if sel==1:
        print("Sender Organization: Aeronotical Development Agency")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def01') and (pw=='def@01')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==2:
        print("Sender Organization: Defence Exhibition Organization")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def02') and (pw=='def@02')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==3:
        print("Sender Organization: Defence Intelligence Agency")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def03') and (pw=='def@03')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==4:
        print("Sender Organization: Defence Planning Committee")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def04') and (pw=='def@04')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==5:
        print("Sender Organization: Defence Research Development Organization")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def05') and (pw=='def@05')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==6:
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def06') and (pw=='def@06')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
        print("Sender Organization: Directorate of Air Intelligence") 
    if sel==7:
        print("Sender Organization: Directorate of Military Intelligence")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def07') and (pw=='def@07')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==8:
        print("Sender Organization: Directorate of Naval Intelligence")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def08') and (pw=='def@08')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==9:
        print("Sender Organization: Indian Air Force") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def09') and (pw=='def@09')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==10:
        print("Sender Organization: Indian Army")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def10') and (pw=='def@10')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==11:
        print("Sender Organization: Indian Coast Gaurd")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def11') and (pw=='def@11')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password") 
            sys.exit() 
    if sel==12:
        print("Sender Organization: Indian Combined Defence Service") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def12') and (pw=='def@12')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==13:
        print("Sender Organization: Indian Navy")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def13') and (pw=='def@13')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==14:
        print("Sender Organization: Indigenous Defence Equipment Exporters Association")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def14') and (pw=='def@14')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password") 
            sys.exit()  
    if sel==15:
        print("Sender Organization: Indian Space research Organization") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def15') and (pw=='def@15')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==16:
        print("Sender Organization: MARCOS")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def16') and (pw=='def@16')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==17:
        print("Sender Organization: Military Engineer Services")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def17') and (pw=='def@17')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==18:
        print("Sender Organization: National Defence Acadamy") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def18') and (pw=='def@18')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==19:
        print("Sender Organization: Ordnance Factory Board")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def19') and (pw=='def@19')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==20:
        print("Sender Organization: Samtel Avionics")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def20') and (pw=='def@20')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
def receiverorganization():
    print("\nSelect the Receiver Organization (India)")
    print("\n1.Aeronotical Development Agency\n2.Defence Exhibition Organization\n3.Defence Intelligence Agency\n4.Defence Planning Committee\n5.Defence Research and Development Organization\n6.Directorate of Air Intelligence\n7.Directorate of Military Intelligence\n8.Directorate of Naval Intelligence\n9.Indian Air Force\n10.Indian Army\n11.Indian Coastal Gaurd\n12.Indian Combined Defence Service\n13.Indian Navy\n14.Indigenous Defence Equipment Exporters Association\n15.Indian Space Research Organization\n16.MARCOS\n17.Military Engineer Services\n18.National Defence Acadamy\n19.Ordnance Factory Board\n20.Samtel Avionics\n")
    sel=int(input("Choose the Receiver Defence agency: "))
    if sel==1:
        print("Receiver Organization: Aeronotical Development Agency")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def01') and (pw=='def@01')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==2:
        print("Receiver Organization: Defence Exhibition Organization")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def02') and (pw=='def@02')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==3:
        print("Receiver Organization: Defence Intelligence Agency")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def03') and (pw=='def@03')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==4:
        print("Receiver Organization: Defence Planning Committee")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def04') and (pw=='def@04')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==5:
        print("Receiver Organization: Defence Research Development Organization")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def05') and (pw=='def@05')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==6:
        print("Receiver Organization: Directorate of Air Intelligence") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def06') and (pw=='def@06')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==7:
        print("Receiver Organization: Directorate of Military Intelligence")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def07') and (pw=='def@07')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password") 
            sys.exit()
    if sel==8:
        print("Receiver Organization: Directorate of Naval Intelligence")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def08') and (pw=='def@08')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==9:
        print("Receiver Organization: Indian Air Force") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def09') and (pw=='def@09')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==10:
        print("Receiver Organization: Indian Army")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def10') and (pw=='def@10' or pw)):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")  
            sys.exit()
    if sel==11:
        print("Receiver Organization: Indian Coast Gaurd")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def11') and (pw=='def@11')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==12:
        print("Receiver Organization: Indian Combined Defence Service") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def12') and (pw=='def@12')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit() 
    if sel==13:
        print("Receiver Organization: Indian Navy")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def13') and (pw=='def@13')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password") 
            sys.exit()
    if sel==14:
        print("Receiver Organization: Indigenous Defence Equipment Exporters Association")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def14') and (pw=='def@14')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password") 
            sys.exit()
    if sel==15:
        print("Receiver Organization: Indian Space research Organization") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def15') and (pw=='def@15')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==16:
        print("Receiver Organization: MARCOS")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def16') and (pw=='def@16')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==17:
        print("Receiver Organization: Military Engineer Services")  
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def17') and (pw=='def@17')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==18:
        print("Receiver Organization: National Defence Acadamy") 
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def18') and (pw=='def@18')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==19:
        print("Receiver Organization: Ordnance Factory Board")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def19') and (pw=='def@19')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
    if sel==20:
        print("ReceiverOrganization: Samtel Avionics")
        us=str(input("\nEnter your user name: "))
        pw=str(input("\nEnter your password: "))
        if ((us=='def20') and (pw=='def@20')):
            print("\nLogin successfully")
        else:
            print("\nEnter correct user name or password")
            sys.exit()
def main(): 
    print("::::: Welcome to Indian Defence Organization Home Page")
    home()
    orglist(1)
    
    print("\n\n::::: Welcome to Crypto Stegano System :::::")
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
                    data=str(en_msg) + str(p) 
                    print("Encrypted data and Key: ",data)
                    es.encode(data)
                    sel=int(input("\nSelect the Operation\n1.Sender Operation\n2.Receiver Operation\n"))
                    if (sel==2):
                        receiverorganization()
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