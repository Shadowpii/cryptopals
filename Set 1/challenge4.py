# Detect single-character XOR

import binascii
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Challenge04.txt")

def score_english(text):
    # Frequency-based English scoring
    frequency = 'ETAOIN SHRDLUetaoinshrdlu '
    return sum(text.count(c) for c in frequency)

def single_byte_xor(cipher_bytes):
    best_score = 0
    best_result = ""
    best_key = 0
    for key in range(256):
        decoded = ''.join(chr(b ^ key) for b in cipher_bytes)
        score = score_english(decoded)
        if score > best_score:
            best_score = score
            best_result = decoded
            best_key = key
    return best_score, best_result, best_key

best_overall = (0, "", 0)

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        cipher_bytes = binascii.unhexlify(line)
        score, result, key = single_byte_xor(cipher_bytes)
        if score > best_overall[0]:
            best_overall = (score, result, key)

print("Decrypted message:\n", best_overall[1])

# print("Key used:", best_overall[2])
# Answer: Now that the party is jumping