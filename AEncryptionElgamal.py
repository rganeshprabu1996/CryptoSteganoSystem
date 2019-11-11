import Main as m
global savemessage

def encrypt(msg,q,h,g): 
    en_msg = []
    k = m.gen_key(q)
    s = m.power(h, k, q) 
    p = m.power(g, k, q) 
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
    print("g^k used                 :  ", p) 
    print("g^ak used                :  ", s) 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
    return en_msg, p 

def save(en_msg):
    savemessage=en_msg
    for i in range(0, len(savemessage)):
        savemessage[i]
    print("Encrypted Message        :  " , savemessage)
    return savemessage