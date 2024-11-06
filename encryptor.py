import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

def encrypt_symmetric_key(public_key_file, symmetric_key):
    with open(public_key_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_symmetric_key = cipher_rsa.encrypt(symmetric_key)
    return encrypted_symmetric_key

def encrypt_file(input_file, output_file, symmetric_key):
    cipher_aes = AES.new(symmetric_key, AES.MODE_EAX)
    with open(input_file, 'rb') as f:
        file_data = f.read()
    ciphertext, tag = cipher_aes.encrypt_and_digest(file_data)
    
    with open(output_file, 'wb') as f:
        f.write(cipher_aes.nonce)
        f.write(tag)
        f.write(ciphertext)

def main():
    parser = argparse.ArgumentParser(description="Encryptor")
    parser.add_argument("--receiver_pub_key", required=True)
    parser.add_argument("--input_file", required=True)
    parser.add_argument("--output_encrypted_file", required=True)
    parser.add_argument("--output_encrypted_symmetric_key", required=True)

    args = parser.parse_args()

    symmetric_key = get_random_bytes(16)  # Generate random 128-bit symmetric key

    encrypted_symmetric_key = encrypt_symmetric_key(args.receiver_pub_key, symmetric_key)
    with open(args.output_encrypted_symmetric_key, 'wb') as f:
        f.write(encrypted_symmetric_key)
    
    encrypt_file(args.input_file, args.output_encrypted_file, symmetric_key)
    print("Encryption complete.")

if __name__ == "__main__":
    main()
