# Implementing repeating-key XOR

text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = "ICE"

ciphertexts = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

def repeating_key_xor(plaintext, key):
    key_bytes = key.encode()
    plaintext_bytes = plaintext.encode()
    
    ciphertext = bytearray()
    for i in range(len(plaintext_bytes)):
        ciphertext.append(plaintext_bytes[i] ^ key_bytes[i % len(key_bytes)])
    
    return ciphertext.hex()

cipher = repeating_key_xor(text, key)

if(cipher == ciphertexts):
    print("Success!")
else:
    print("Failure!")
