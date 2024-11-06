import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

def decrypt_symmetric_key(private_key_file, encrypted_symmetric_key_file):
    with open(private_key_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    with open(encrypted_symmetric_key_file, 'rb') as f:
        encrypted_symmetric_key = f.read()
    symmetric_key = cipher_rsa.decrypt(encrypted_symmetric_key)
    return symmetric_key

def decrypt_file(input_file, output_file, symmetric_key):
    with open(input_file, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    
    cipher_aes = AES.new(symmetric_key, AES.MODE_EAX, nonce=nonce)
    file_data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    with open(output_file, 'wb') as f:
        f.write(file_data)

def main():
    parser = argparse.ArgumentParser(description="Decryptor")
    parser.add_argument("--receiver_private_key", required=True)
    parser.add_argument("--encrypted_key", required=True)
    parser.add_argument("--input_file", required=True)
    parser.add_argument("--output_decrypted_file", required=True)

    args = parser.parse_args()

    symmetric_key = decrypt_symmetric_key(args.receiver_private_key, args.encrypted_key)
    decrypt_file(args.input_file, args.output_decrypted_file, symmetric_key)
    print("Decryption complete.")

if __name__ == "__main__":
    main()
