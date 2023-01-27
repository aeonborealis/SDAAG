import gnupg
import os

def create_pgp_key(image_path:str, name:str, email:str)->None:
    gpg = gnupg.GPG(gnupghome='/path/to/gnupg/home')
    input_data = gpg.gen_key_input(name_real=name, name_email=email)
    key = gpg.gen_key(input_data)

    #convert image to ascii
    with open(image_path, 'rb') as f:
        image_data = f.read()
    ascii_data = "".join([str(i) for i in image_data])
    print(key)
    # Add the ascii data as a subkey to the key
    subkey = gpg.add_subkey(key.fingerprint, subkey_type='RSA', key_length=2048, passphrase='passphrase', subkey_usage='S', expires='2022-12-31', 
                            key_origin=ascii_data)
    print(subkey)

create_pgp_key("path/to/image.jpg","John Doe","johndoe@example.com")
