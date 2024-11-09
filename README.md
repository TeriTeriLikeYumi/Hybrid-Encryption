
# Installation Guide

Follow these steps to set up and run the Hybrid Encryption system.

## 1. Install Required Libraries

Ensure you have the required libraries installed. Run the following commands:

```bash
pip install pycryptodome==3.21.0
pip install argparse==1.4.0
```

## 2. Generate RSA Key Pair

To create the RSA key pair for encryption and decryption, run:

```bash
python keygen.py
```

- This will generate two files: 
  - **`receiver_private_key.key`** – your private key for decryption
  - **`receiver_pub_key.pub`** – your public key for encryption

## 3. Encrypt a File

To encrypt a file using the generated public key, execute the following command:

```bash
python encryptor.py --receiver_pub_key=receiver_pub_key.pub \
--input_file=sample.txt \
--output_encrypted_file=output_encrypted_file.txt \
--output_encrypted_symmetric_key=encrypted_key.key
```

- Replace **`file_to_encrypt.txt`** with the path to the file you want to encrypt.
- **Output Files:**
  - **`output_encrypted_file.txt`** – the encrypted content of the input file
  - **`encrypted_key.key`** – the encrypted symmetric key used for decryption

## 4. Decrypt the Encrypted File

To decrypt the file using your private key, use the command below:

```bash
python decryptor.py --receiver_private_key=receiver_private_key.key \
--encrypted_key=encrypted_key.key \
--input_file=output_encrypted_file.txt \
--output_decrypted_file=output_decrypted_file.txt
```

- Replace **`output_encrypted_file.txt`** with the path to the encrypted file.
- **Output:** **`output_decrypted_file.txt`** – the decrypted version of your original file.
