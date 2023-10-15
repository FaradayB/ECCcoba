from tinyec import registry
import secrets

def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

Ka = secrets.randbelow(curve.field.n)
X = Ka * curve.g
print("X:", compress(X))
Kb = secrets.randbelow(curve.field.n)
Y = Kb * curve.g
print("Y:", compress(Y))
print("Currently exchange the public keys (e.g., through the Internet)")

A_SharedKey = Ka * Y
print("A shared key:", compress(A_SharedKey))
B_SharedKey = Kb * X
print("(B) shared key:", compress(B_SharedKey))
print("Equal shared keys:", A_SharedKey == B_SharedKey)

# Input the message you want to encrypt
message = input("Enter the message to encrypt: ")

# Convert the shared key to bytes
shared_key_bytes = int(A_SharedKey.x).to_bytes((A_SharedKey.x.bit_length() + 7) // 8, byteorder='big')

# Use the shared key to encrypt the message
message_bytes = bytearray(message.encode())
encrypted_message = bytes(message_byte ^ key_byte for message_byte, key_byte in zip(message_bytes, shared_key_bytes))

print("Encrypted message (bytes):", encrypted_message)

# To decrypt the message, the recipient can use the shared key in a similar manner.
