"Single-byte XOR cipher"

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

import binascii
def single_byte_xor(hex):
    hexstring = binascii.unhexlify(hex_string)
    result = (''.join(chr(num ^ key) for num in hexstring) for key in range(256))        
    return max(result, key=lambda s: s.count(' '))

print(single_byte_xor(hex_string))

# Cooking MC's like a pound of bacon