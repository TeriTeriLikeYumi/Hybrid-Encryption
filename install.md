# Install library
```python
pip install pycryptodome==3.21.0
```

```
pip install argparse==1.4.0
```
# Generate pair of key

```bash
python keygen.py
```

# Run Encrypt file 

```bash
python encryptor.py --receiver_pub_key=receiver_pub_key.pub \
--input_file=file_to_encrypt.txt \
--output_encrypted_file=output_encrypted_file.txt \
--output_encrypted_symmetric_key=encrypted_key.key
```

# Run Decrypt file

```bash
python decryptor.py --receiver_private_key=receiver_private_key.key \
--encrypted_key=encrypted_key.key \
--input_file=encrypted_file.txt \
--output_decrypted_file=output_decrypted_file.txt \
```

