from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key_file = 'receiver_private_key.key'
public_key_file = 'receiver_pub_key.pub'

# Export the private key
with open(private_key_file, 'wb') as priv_file:
    priv_file.write(key.export_key())

# Export the public key
public_key = key.publickey()
with open(public_key_file, 'wb') as pub_file:
    pub_file.write(public_key.export_key())
    