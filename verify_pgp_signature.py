import gnupg

def verify_pgp_signature(signature_path:str, data_path:str, public_key_path:str)->None:
    gpg = gnupg.GPG(gnupghome='/path/to/gnupg/home')

    # Import the public key
    with open(public_key_path, 'rb') as f:
        public_key_data = f.read()
    import_result = gpg.import_keys(public_key_data)
    print("Imported key fingerprint: ", import_result.fingerprints)

    # Verify the signature
    with open(signature_path, 'rb') as f:
        signature_data = f.read()
    with open(data_path, 'rb') as f:
        data = f.read()
    verify = gpg.verify(signature_data, data)
    if verify:
        print("Signature is valid!")
    else:
        print("Signature is invalid!")

verify_pgp_signature("path/to/signature.asc", "path/to/data.txt", "path/to/public_key.asc")
