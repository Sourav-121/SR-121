charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def repeat_key(key, length):
    key_str = str(key)
    return (key_str * ((length // len(key_str)) + 1))[:length]

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key_str = repeat_key(key, len(plaintext))
    k_floor = int(key) // 2
    ciphertext = []

    for i in range(len(plaintext)):
        x = charset.index(plaintext[i])                          
        n = (x + k_floor) % 36                                   

       
        ki=charset.index(key_str[i])
        shifted = (n + 121) % 36                                
        ci = (ki + shifted) % 36                                

        ciphertext.append(charset[ci])                         
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    key_str = repeat_key(key, len(ciphertext))
    k_floor = int(key) // 2
    plaintext = []

    for i in range(len(ciphertext)):
        ci = charset.index(ciphertext[i])                        

      
        ki=charset.index(key_str[i])
        shifted_n = (ci - ki) % 36                             
        n = (shifted_n - 121) % 36                           

        m = (n - k_floor) % 36                                  
        plaintext.append(charset[m])                            
    return ''.join(plaintext)



# test case
plaintext = "CSE 361"
key = 4635

encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)

print("Plaintext :", plaintext.replace(" ", ""))
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
