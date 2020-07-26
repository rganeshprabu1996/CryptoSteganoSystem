import Main as m

def decrypt(en_msg,p,key,q):
    dr_msg = []
    h = m.power(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h)))         
    return dr_msg 