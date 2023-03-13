from ecdsa import SigningKey, SECP256k1
# Generate a new private key
sk = SigningKey.generate(curve=SECP256k1)
print(sk)
# Get the public key
vk = sk.verifying_key
print(vk)
# Sign a message
signature = sk.sign(b"Not your keys, not your coins!")
print(signature)
# Verify the signature
assert vk.verify(signature, b"Not your keys, not your coins!")
# If your script runs to this point without an error, congrats, you successfully validated the signature!
print("If your script runs to this point without an error, congrats, you successfully validated the signature!")